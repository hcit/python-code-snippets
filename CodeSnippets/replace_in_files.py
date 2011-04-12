#!/usr/bin/python -O
# -*- coding: UTF-8 -*-

"""
-replace string in files (recursive)
-display the difference.

v0.2
 - search_string can be a re.compile() object -> use re.sub for replacing
 
v0.1
 - initial version

:copyleft: 2009-2011 by Jens Diemer
"""

__author__ = "Jens Diemer"
__license__ = """GNU General Public License v3 or above -
 http://www.opensource.org/licenses/gpl-license.php"""
__url__ = "http://www.jensdiemer.de"
__version__ = "0.2"



import os, re, time, fnmatch, difflib


class search:
    def __init__(self, search_path, search_string, replace_string,
                                        search_only=True, file_filter=("*.*",)):
        self.search_path = search_path
        self.search_string = search_string
        self.replace_string = replace_string
        self.search_only = search_only
        self.file_filter = file_filter

        assert isinstance(self.file_filter, (list, tuple))

        # FIXME:
        self.is_re = str(type(self.search_string)) == "<type '_sre.SRE_Pattern'>"

        print "Search '%s' in [%s]..." % (
            self.search_string, self.search_path
        )
        print "_" * 80

        time_begin = time.time()

        file_count = self.walk()

        print "_" * 80
        print "%s files searched in %0.2fsec." % (
            file_count, (time.time() - time_begin)
        )

    def walk(self):
        file_count = 0
        for root, dirlist, filelist in os.walk(self.search_path):
            if ".svn" in root:
                continue
            for filename in filelist:
                for file_filter in self.file_filter:
                    if fnmatch.fnmatch(filename, file_filter):
                        self.search_file(os.path.join(root, filename))
                        file_count += 1
        return file_count

    def search_file(self, filepath):
        f = file(filepath, "r")
        old_content = f.read()
        f.close()

        if self.is_re or self.search_string in old_content:
            new_content = self.replace_content(old_content, filepath)
            if self.is_re and new_content == old_content:
                return

            print filepath
            self.display_plaintext_diff(old_content, new_content)

    def replace_content(self, old_content, filepath):
        if self.is_re:
            new_content = self.search_string.sub(self.replace_string, old_content)
        else:
            new_content = old_content.replace(
                self.search_string, self.replace_string
            )

        if self.search_only != False:
            return new_content

        print "Write new content into %s..." % filepath,
        try:
            f = file(filepath, "w")
            f.write(new_content)
            f.close()
        except IOError, msg:
            print "Error:", msg
        else:
            print "OK"
        print
        return new_content

    def display_plaintext_diff(self, content1, content2):
        """
        Display a diff.
        """
        content1 = content1.splitlines()
        content2 = content2.splitlines()

        diff = difflib.Differ().compare(content1, content2)

        def is_diff_line(line):
            for char in ("-", "+", "?"):
                if line.startswith(char):
                    return True
            return False

        print "line | text\n-------------------------------------------"
        old_line = ""
        in_block = False
        old_lineno = lineno = 0
        for line in diff:
            if line.startswith(" ") or line.startswith("+"):
                lineno += 1

            if old_lineno == lineno:
                display_line = "%4s | %s" % ("", line.rstrip())
            else:
                display_line = "%4s | %s" % (lineno, line.rstrip())

            if is_diff_line(line):
                if not in_block:
                    print "..."
                    # Display previous line
                    print old_line
                    in_block = True

                print display_line

            else:
                if in_block:
                    # Display the next line aber a diff-block
                    print display_line
                in_block = False

            old_line = display_line
            old_lineno = lineno
        print "..."


if __name__ == "__main__":
    search(
        search_path=r"./example/path",

        # e.g.: simple string replace:
        search_string='the old string',
        replace_string='the new string',

        # e.g.: Regular expression replacing (used re.sub)
        #search_string   = re.compile('{% url (.*?) %}'),
        #replace_string  = "{% url '\g<1>' %}",

        search_only=True, # Display only the difference
#        search_only     = False, # write the new content
        file_filter=("*.py",), # fnmatch-Filter
    )
