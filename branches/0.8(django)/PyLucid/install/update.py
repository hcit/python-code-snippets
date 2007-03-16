
"""
2. update

sollte ich mir mal ansehen:
http://code.djangoproject.com/wiki/CookBookScriptsMiniFlush
"""

from PyLucid.install.BaseInstall import BaseInstall
from PyLucid.settings import TABLE_PREFIX



#______________________________________________________________________________

class Update(BaseInstall):
    def view(self):
        output = ["\nupdate PyLucid database:\n"]
        
        from django.db import connection
        cursor = connection.cursor()
        
        def display_info(txt):
            output.append("\n\n")
            output.append("%s:\n" % txt)
            output.append("-"*79)
            output.append("\n")
            
        
        def verbose_execute(SQLcommand):
            output.append("%s..." % SQLcommand)
            try:
                cursor.execute(SQLcommand)
            except Exception, e:
                output.append("Error: %s\n" % e)
            else:
                output.append("OK\n")
    
        SQLcommand = "ALTER TABLE pylucid_plugin DROP plugin_cfg;"
        verbose_execute(SQLcommand)
    
        display_info("Drop obsolete tables")
    
        for tablename in ("l10n", "group", "user_group", "log", "session_data"):
            tablename = TABLE_PREFIX + tablename
            SQLcommand = "DROP TABLE %s;" % tablename
            verbose_execute(SQLcommand)
            
        display_info("rename tables")
    
        tablenames = (
            ("pages",  "page"),
            ("styles", "style"),
            ("templates", "template"),
            ("groups", "group"),
            ("markups", "markup"),
            ("md5users", "md5user"),
            ("plugins", "plugin"),
            ("preferences", "preference"),
            ("styles", "style"),
            ("template_engines", "template_engine"),
            ("templates", "template"),
        )
        for source, destination in tablenames:
            source = TABLE_PREFIX + source
            destination = TABLE_PREFIX + destination
    
            SQLcommand = "RENAME TABLE %s TO %s;" % (source, destination)
            verbose_execute(SQLcommand)
    
        output.append("\n\nupdate done. (Please go back)")
    
        return self._simple_render(output, headline="syncdb")

def update(request, install_pass):
    """
    1. update DB tables from v0.7.2 to django PyLucid v0.8
    """
    return Update(request, install_pass).view()

#______________________________________________________________________________

REPLACE_DATA = (
    ("|escapexml ", "|escape "),
)
def _convert_template(content):
    """
    simple replace some tags
    """
    changed = False
    for source, destination in REPLACE_DATA:
        if source in content:
            old_content = content
            content = content.replace(source, destination)
            if old_content != content:
                changed = True

    if changed:
        return content

UNSUPPORTED_TAGS = ("{% recurse ",)
def _display_warnings(output, content):
    """
    Waring if there is some unsupportet tags in the template
    """
    for tag in UNSUPPORTED_TAGS:
        if tag in content:
            output.append("\t - WARNING: unsupportet tag '%s' in Template!\n" % tag)


class UpdateTemplates(BaseInstall):
    def view(self):
        from PyLucid.tools.Diff import display_plaintext_diff
        from PyLucid.models import PagesInternal
        
        output = []
        for internal_page in PagesInternal.objects.all():
            name = internal_page.name
            old_content = internal_page.content_html
            
            output.append("\n==================[ %s ]==================\n\n" % name)
            _display_warnings(output, old_content)
            content = _convert_template(old_content)
            if not content:
                output.append("\t - Nothing to change.\n")
                continue
            
            output.append("\t - changed!\n\nthe diff:\n")
            display_plaintext_diff(old_content, content, response)
            
            internal_page.content_html = content
            internal_page.save()
            output.append("\t - updated and saved.\n")
            
            output.append("\n\n")
            
        return self._simple_render(output, headline="update templates")

def update_templates(request, install_pass):
    """
    2. convert jinja to django templates
    """
    return UpdateTemplates(request, install_pass).view()