table = 'PyLucid_style'
fields = ['id', 'name', 'createtime', 'lastupdatetime', 'createby_id', 'lastupdateby_id', 'description', 'content']
#default item format: "fieldname":("type", "value")
default = {}
records = [
[1, u'main', '2007-06-22 09:48:29', '2007-12-07 08:53:15', None, None, u'default Stylesheet', u'* { color: #000000 }\r\n\r\nbody{\r\n  font-size:0.9em;\r\n  font-family: tahoma, arial, sans-serif;\r\n  background: #FFFFF9;\r\n  margin: 15px 10% 15px 10%;\r\n  min-width:802px;\r\n}\r\n\r\n/*\r\n headline definition if you use a picture:\r\n----------------------------------------------\r\n#headline {\r\n  background: #C9C573;\r\n  text-align: center;\r\n  height: 70px;\r\n  margin: 0px;\r\n  padding: 0px;\r\n  border: 1px solid black;\r\n  border-bottom: 0px;\r\n}\r\n#headline img {\r\n  border: 0px;\r\n  overflow:hidden;\r\n}\r\n----------------------------------------------\r\n*/\r\n\r\n/*\r\n headline definition with text only:\r\n*/\r\n#headline {\r\n  background: #C9C573;\r\n  font-size: 30px;\r\n  margin: 0px;\r\n  padding: 10px;\r\n  border: 1px solid black;\r\n  border-bottom: 0px;\r\n}\r\n#headline a {\r\n  text-decoration:none;\r\n  color: white;\r\n}\r\n/*\r\n----------------------------------------------\r\n*/\r\n\r\n#back_links {\r\n  font-size:0.8em;\r\n}\r\n\r\n#the_menu {\r\n  background: #FFFFDB;\r\n  border: 1px solid #B1B08B;\r\n  float: right;\r\n  padding: 15px;\r\n  margin: 10px;\r\n}\r\n#the_menu img {\r\n  text-align: center;\r\n}\r\n\r\n#main_menu {\r\n  font-size:0.9em;\r\n}\r\n\r\n#searching input, #searching button {\r\n  font-size: 0.85em;\r\n  border: 1px solid #444;\r\n  padding: 1px;\r\n}\r\n\r\n#main_content {\r\n  min-height:400px;\r\n  background: #FFFFE5;\r\n  padding: 5px;\r\n  border: 1px solid black;\r\n}\r\n\r\na:hover, a .current {\r\n  background-color: #C9C573;\r\n  color: white;\r\n}\r\n\r\npre {\r\n  border:1px solid grey;\r\n  background-color: white;\r\n}\r\n\r\n#footer {\r\n  font-size:0.75em;\r\n  border: 1px solid black;\r\n  padding: 5px;\r\n  text-align: center;\r\n}\r\n\r\n/* ---------------------------------------------------------------------- */\r\ntextarea {\r\n  width: 100%;\r\n}\r\n.back_links, #permalink {\r\n  font-size: 0.8em;\r\n}\r\n#permalink {\r\n  text-align: right;\r\n  padding: 10px;\r\n}\r\n/* ----------------------------------------------------------------------\r\n   Pygments syntax highlighter\r\n---------------------------------------------------------------------- */\r\n.pygments_code, .pygments_code table, .pygments_code .code, .pygments_code pre {\r\n  background: #ffffff;\r\n  padding: 0;\r\n  margin: 0;\r\n}\r\n.pygments_code pre {\r\n border: 1px;\r\n}\r\n.pygments_code .code {\r\n  width: 100%;\r\n}\r\n.pygments  { background: #ffffff; }\r\n.pygments .c { color: #808080 } /* Comment */\r\n.pygments .err { color: #F00000; background-color: #F0A0A0 } /* Error */\r\n.pygments .k { color: #008000; font-weight: bold } /* Keyword */\r\n.pygments .o { color: #303030 } /* Operator */\r\n.pygments .cm { color: #808080 } /* Comment.Multiline */\r\n.pygments .cp { color: #507090 } /* Comment.Preproc */\r\n.pygments .c1 { color: #808080 } /* Comment.Single */\r\n.pygments .cs { color: #cc0000; font-weight: bold } /* Comment.Special */\r\n.pygments .gd { color: #A00000 } /* Generic.Deleted */\r\n.pygments .ge { font-style: italic } /* Generic.Emph */\r\n.pygments .gr { color: #FF0000 } /* Generic.Error */\r\n.pygments .gh { color: #000080; font-weight: bold } /* Generic.Heading */\r\n.pygments .gi { color: #00A000 } /* Generic.Inserted */\r\n.pygments .go { color: #808080 } /* Generic.Output */\r\n.pygments .gp { color: #c65d09; font-weight: bold } /* Generic.Prompt */\r\n.pygments .gs { font-weight: bold } /* Generic.Strong */\r\n.pygments .gu { color: #800080; font-weight: bold } /* Generic.Subheading */\r\n.pygments .gt { color: #0040D0 } /* Generic.Traceback */\r\n.pygments .kc { color: #008000; font-weight: bold } /* Keyword.Constant */\r\n.pygments .kd { color: #008000; font-weight: bold } /* Keyword.Declaration */\r\n.pygments .kp { color: #003080; font-weight: bold } /* Keyword.Pseudo */\r\n.pygments .kr { color: #008000; font-weight: bold } /* Keyword.Reserved */\r\n.pygments .kt { color: #303090; font-weight: bold } /* Keyword.Type */\r\n.pygments .m { color: #6000E0; font-weight: bold } /* Literal.Number */\r\n.pygments .s { background-color: #fff0f0 } /* Literal.String */\r\n.pygments .na { color: #0000C0 } /* Name.Attribute */\r\n.pygments .nb { color: #007020 } /* Name.Builtin */\r\n.pygments .nc { color: #B00060; font-weight: bold } /* Name.Class */\r\n.pygments .no { color: #003060; font-weight: bold } /* Name.Constant */\r\n.pygments .nd { color: #505050; font-weight: bold } /* Name.Decorator */\r\n.pygments .ni { color: #800000; font-weight: bold } /* Name.Entity */\r\n.pygments .ne { color: #F00000; font-weight: bold } /* Name.Exception */\r\n.pygments .nf { color: #0060B0; font-weight: bold } /* Name.Function */\r\n.pygments .nl { color: #907000; font-weight: bold } /* Name.Label */\r\n.pygments .nn { color: #0e84b5; font-weight: bold } /* Name.Namespace */\r\n.pygments .nt { color: #007000 } /* Name.Tag */\r\n.pygments .nv { color: #906030 } /* Name.Variable */\r\n.pygments .ow { color: #000000; font-weight: bold } /* Operator.Word */\r\n.pygments .w { color: #bbbbbb } /* Text.Whitespace */\r\n.pygments .mf { color: #6000E0; font-weight: bold } /* Literal.Number.Float */\r\n.pygments .mh { color: #005080; font-weight: bold } /* Literal.Number.Hex */\r\n.pygments .mi { color: #0000D0; font-weight: bold } /* Literal.Number.Integer */\r\n.pygments .mo { color: #4000E0; font-weight: bold } /* Literal.Number.Oct */\r\n.pygments .sb { background-color: #fff0f0 } /* Literal.String.Backtick */\r\n.pygments .sc { color: #0040D0 } /* Literal.String.Char */\r\n.pygments .sd { color: #D04020 } /* Literal.String.Doc */\r\n.pygments .s2 { background-color: #fff0f0 } /* Literal.String.Double */\r\n.pygments .se { color: #606060; font-weight: bold; background-color: #fff0f0 } /* Literal.String.Escape */\r\n.pygments .sh { background-color: #fff0f0 } /* Literal.String.Heredoc */\r\n.pygments .si { background-color: #e0e0e0 } /* Literal.String.Interpol */\r\n.pygments .sx { color: #D02000; background-color: #fff0f0 } /* Literal.String.Other */\r\n.pygments .sr { color: #000000; background-color: #fff0ff } /* Literal.String.Regex */\r\n.pygments .s1 { background-color: #fff0f0 } /* Literal.String.Single */\r\n.pygments .ss { color: #A06000 } /* Literal.String.Symbol */\r\n.pygments .bp { color: #007020 } /* Name.Builtin.Pseudo */\r\n.pygments .vc { color: #306090 } /* Name.Variable.Class */\r\n.pygments .vg { color: #d07000; font-weight: bold } /* Name.Variable.Global */\r\n.pygments .vi { color: #3030B0 } /* Name.Variable.Instance */\r\n.pygments .il { color: #0000D0; font-weight: bold } /* Literal.Number.Integer.Long */\r\n']
[3, u'old_main', '2007-06-22 09:48:29', '2007-12-07 08:52:47', None, None, u'the old default ghastly design... ;) You should never use this ugly thing!', u'* { color: #000000 }\r\nbody {\r\n  margin:0;\r\n  padding:0;\r\n  padding-left:15em;\r\n  padding-top:120px;\r\n\r\n  font-family: tahoma, arial, sans-serif;\r\n  color: #000;\r\n  font-size: 0.9em;\r\n  background-color: #C9C573;\r\n}\r\n\r\nbody > #sidebar, body > #headline, body > #adsense {\r\n  /* Kopf und Navi feststehend machen */\r\n  position:fixed;\r\n}\r\n\r\nhtml, body {\r\n  margin: 5px;\r\n  padding: 0;\r\n}\r\ntextarea {\r\n  background-color: #FFFFF5;\r\n}\r\n#page_msg, pre, .code, .SourceCode, fieldset legend {\r\n  font-family: Courier New,Courier,monospace,mono;\r\n  background-color: #FAFAFD;\r\n  color: #000;\r\n  padding: 10px;\r\n  border: 1px solid #C9C573;\r\n  font-size: 0.8em;\r\n}\r\n.SourceCode {\r\n  white-space:nowrap;\r\n}\r\nfieldset legend {\r\n  font-size: 1em;\r\n  padding: 3px;\r\n}\r\n#page_msg {\r\n  border-color: #F00;\r\n  color: #A00;\r\n}\r\n\r\n/* -----------------------------------------------------\r\n?berschrift ?ber die gesammte Seite\r\n----------------------------------------------------- */\r\n#headline {\r\n  position:absolute;\r\n  width: 100%;\r\n  left:0em;\r\n  top:0em;\r\n  z-index:3;\r\n\r\n  margin:0;\r\n  padding:0;\r\n\r\n  white-space:pre;\r\n  background-color:inherit;\r\n  overflow:hidden;\r\n}\r\n#headline h2 {\r\n  font-size: 2em;\r\n  margin: 0.5em;\r\n  padding-left: 1.5em;\r\n  color: #FFF;\r\n}\r\n\r\n/* -----------------------------------------------------\r\ngoogle AdSense\r\n----------------------------------------------------- */\r\n\r\n#adsense {\r\n  position:absolute;\r\n  top: 0px;\r\n  right: 3px;\r\n  z-index:99;\r\n}\r\n\r\n/* -----------------------------------------------------\r\nMenu\r\n----------------------------------------------------- */\r\n#sidebar {\r\n  position:absolute;\r\n  top: 100px;\r\n  left: 3px;\r\n  width: 17em;\r\n  height: auto;\r\n  z-index: 10;\r\n\r\n  background-color: #FFFFDB;\r\n  border: 1px solid #B1B08B;\r\n  font-size: 0.9em;\r\n  color: #000;\r\n\r\n  text-align:left;\r\n\r\n  padding: 0em;\r\n  padding-top: 1em;\r\n  margin: 0px;\r\n}\r\n#sidebar a {\r\n  text-decoration:none;\r\n  margin: 0px;\r\n  padding: 0px;\r\n  padding-left: 0.5em;\r\n  padding-right: 0.5em;\r\n}\r\n#sidebar a:hover, #sidebar a .current {\r\n  /* hover + Aktuell angeklickter Men?punkt */\r\n  background-color: #C9C573;\r\n  color: #FFF;\r\n  margin: 0px;\r\n  padding: 0px;\r\n  padding-left: 0.5em;\r\n  padding-right: 0.5em;\r\n}\r\n#sidebar ul {\r\n  margin: 1.5em;\r\n  margin-right: 0px;\r\n  margin-top: 0.2em;\r\n  margin-bottom: 1.5em;\r\n\r\n  padding: 0px;\r\n\r\n  list-style-type: none;\r\n  border:0px;\r\n}\r\n#sidebar li {\r\n  white-space: nowrap;\r\n  margin: 0px;\r\n  margin-right: 0px;\r\n  padding: 0px;\r\n}\r\n#sidebar img {\r\n  margin: 5px 0px 5px 5px;\r\n  padding: 5px 0px 5px 5px;\r\n}\r\n\r\n/* -----------------------------------------------------\r\nCMS Page\r\n----------------------------------------------------- */\r\n#main-content {\r\n  /* Rahmen f?r main-content + footer_nav */\r\n  position:absolute;\r\n  top: 60px;\r\n  left: 12em;\r\n  min-width: 50em;\r\n  min-height: 600px;\r\n  z-index: 1;\r\n  margin: 5px;\r\n  padding: 20px;\r\n  padding-left: 6em;\r\n  background-color: #FFFFE5;\r\n  border:1px solid black;\r\n}\r\n#main-content h2 {\r\n  border-bottom: 1px solid #000;\r\n}\r\n#nav_footer, #nav_link {\r\n  font-size: 0.6em;\r\n}\r\n#nav_footer, #nav_footer a, #nav_link, #nav_link a {\r\n  border-top: 1px solid #B1B08B;\r\n  color: #B1B08B;\r\n  text-decoration: none;\r\n  text-align: right;\r\n}\r\n#nav_link, #nav_link a {\r\n  text-align: left;\r\n  border: 0px;\r\n}\r\n\r\n/* -----------------------------------------------------\r\nAdmin Menu\r\n----------------------------------------------------- */\r\n.adminmenu {\r\npadding: 5px;\r\nbackground-color: #C9C573;\r\n}\r\n\r\n/* -----------------------------------------------------\r\nLinks aus dem breadcrumbs-Plugin\r\n----------------------------------------------------- */\r\n#breadcrumbs {\r\nwidth: 80%;\r\nmargin:1em auto;\r\ntext-align:left;\r\nmax-width: 1024px;\r\n}\r\n\r\n/* -----------------------------------------------------\r\nZusatzmodule\r\n----------------------------------------------------- */\r\n.Gallery ul {\r\ntext-align: center;\r\nmargin: 0px;\r\npadding: 0px;\r\n}\r\n.Gallery li {\r\nfloat: left;\r\nborder: 1px solid #EAECFF;\r\nheight: 150px;\r\nwidth: auto;\r\ntext-align: center;\r\nmargin: 5px;\r\npadding: 5px;\r\nlist-style-type: none;\r\nbackground-color: #EDF1FF;\r\n}\r\n.clear {\r\nclear: both;\r\nmargin: 5px;\r\npadding: 5px;\r\nborder: none;\r\n}\r\n\r\n/* -----------------------------------------------------\r\nEdit Look\r\n----------------------------------------------------- */\r\n#edit_style_select, #edit_template_select {\r\nborder-spacing: 0.5em;\r\n}\r\n#edit_style_select .name, #edit_template_select .name {\r\nfont-weight:bold\r\n\r\n}\r\n#edit_style_select .description, #edit_template_select .description {\r\nfont-style: italic;\r\n}\r\n#page_edit_preview {\r\nborder: 1px solid #C9C573;\r\n}\r\n.resize_buttons a {\r\ntext-decoration:none;\r\n}\r\n\r\n/* -----------------------------------------------------\r\nPage Edit\r\n----------------------------------------------------- */\r\n#page_content {\r\nwidth: 100%;\r\n}\r\n\r\n\r\n/* -----------------------------------------------------\r\nsearch\r\n----------------------------------------------------- */\r\n#search_form input, #search_form button {\r\nfont-size: 0.9em;\r\nborder: 1px solid #444;\r\npadding: 1px;\r\n}\r\n\r\n/* -----------------------------------------------------\r\nlucidFunction:RSS\r\n----------------------------------------------------- */\r\n.RSS {\r\nmargin: 1em;\r\npadding: 1em;\r\nborder: 1px solid;\r\n}\r\n.RSS li {\r\nlist-style-type: none;\r\n}\r\n.RSS h1 {\r\nfont-size: 1em;\r\nfont-weight: bold;\r\nmargin: 0px;\r\n}\r\n\r\n/* -----------------------------------------------------\r\nresize buttons for textarea\r\n----------------------------------------------------- */\r\n#resize_buttons * {\r\ntext-decoration:none;\r\nmargin: 0px;\r\npadding: 0.1em 2em 0.1em 2em;\r\nfont-family:Verdana;\r\nfont-weight:bold;\r\nline-height:2em;\r\n}\r\n#resize_buttons a:link {\r\ncolor: #000;\r\nbackground-color: #f5f5f5;\r\nborder: 1px solid;\r\nborder-color: #ddd #555 #555 #ddd;\r\n}\r\n#resize_buttons a:hover{\r\ncolor: #fff;\r\nbackground-color: #aaa;\r\nborder-color: #555 #ddd #ddd #555;\r\n}\r\n\r\n/* ---------------------------------------------------------------------- */\r\ntextarea {\r\n  width: 100%;\r\n}\r\n.back_links, #permalink {\r\n  font-size: 0.8em;\r\n}\r\n#permalink {\r\n  text-align: right;\r\n  padding: 10px;\r\n}\r\n/* ----------------------------------------------------------------------\r\n   Pygments syntax highlighter\r\n---------------------------------------------------------------------- */\r\n.pygments_code, .pygments_code table, .pygments_code .code, .pygments_code pre {\r\n  background: #ffffff;\r\n  padding: 0;\r\n  margin: 0;\r\n}\r\n.pygments_code pre {\r\n border: 1px;\r\n}\r\n.pygments_code .code {\r\n  width: 100%;\r\n}\r\n.pygments  { background: #ffffff; }\r\n.pygments .c { color: #808080 } /* Comment */\r\n.pygments .err { color: #F00000; background-color: #F0A0A0 } /* Error */\r\n.pygments .k { color: #008000; font-weight: bold } /* Keyword */\r\n.pygments .o { color: #303030 } /* Operator */\r\n.pygments .cm { color: #808080 } /* Comment.Multiline */\r\n.pygments .cp { color: #507090 } /* Comment.Preproc */\r\n.pygments .c1 { color: #808080 } /* Comment.Single */\r\n.pygments .cs { color: #cc0000; font-weight: bold } /* Comment.Special */\r\n.pygments .gd { color: #A00000 } /* Generic.Deleted */\r\n.pygments .ge { font-style: italic } /* Generic.Emph */\r\n.pygments .gr { color: #FF0000 } /* Generic.Error */\r\n.pygments .gh { color: #000080; font-weight: bold } /* Generic.Heading */\r\n.pygments .gi { color: #00A000 } /* Generic.Inserted */\r\n.pygments .go { color: #808080 } /* Generic.Output */\r\n.pygments .gp { color: #c65d09; font-weight: bold } /* Generic.Prompt */\r\n.pygments .gs { font-weight: bold } /* Generic.Strong */\r\n.pygments .gu { color: #800080; font-weight: bold } /* Generic.Subheading */\r\n.pygments .gt { color: #0040D0 } /* Generic.Traceback */\r\n.pygments .kc { color: #008000; font-weight: bold } /* Keyword.Constant */\r\n.pygments .kd { color: #008000; font-weight: bold } /* Keyword.Declaration */\r\n.pygments .kp { color: #003080; font-weight: bold } /* Keyword.Pseudo */\r\n.pygments .kr { color: #008000; font-weight: bold } /* Keyword.Reserved */\r\n.pygments .kt { color: #303090; font-weight: bold } /* Keyword.Type */\r\n.pygments .m { color: #6000E0; font-weight: bold } /* Literal.Number */\r\n.pygments .s { background-color: #fff0f0 } /* Literal.String */\r\n.pygments .na { color: #0000C0 } /* Name.Attribute */\r\n.pygments .nb { color: #007020 } /* Name.Builtin */\r\n.pygments .nc { color: #B00060; font-weight: bold } /* Name.Class */\r\n.pygments .no { color: #003060; font-weight: bold } /* Name.Constant */\r\n.pygments .nd { color: #505050; font-weight: bold } /* Name.Decorator */\r\n.pygments .ni { color: #800000; font-weight: bold } /* Name.Entity */\r\n.pygments .ne { color: #F00000; font-weight: bold } /* Name.Exception */\r\n.pygments .nf { color: #0060B0; font-weight: bold } /* Name.Function */\r\n.pygments .nl { color: #907000; font-weight: bold } /* Name.Label */\r\n.pygments .nn { color: #0e84b5; font-weight: bold } /* Name.Namespace */\r\n.pygments .nt { color: #007000 } /* Name.Tag */\r\n.pygments .nv { color: #906030 } /* Name.Variable */\r\n.pygments .ow { color: #000000; font-weight: bold } /* Operator.Word */\r\n.pygments .w { color: #bbbbbb } /* Text.Whitespace */\r\n.pygments .mf { color: #6000E0; font-weight: bold } /* Literal.Number.Float */\r\n.pygments .mh { color: #005080; font-weight: bold } /* Literal.Number.Hex */\r\n.pygments .mi { color: #0000D0; font-weight: bold } /* Literal.Number.Integer */\r\n.pygments .mo { color: #4000E0; font-weight: bold } /* Literal.Number.Oct */\r\n.pygments .sb { background-color: #fff0f0 } /* Literal.String.Backtick */\r\n.pygments .sc { color: #0040D0 } /* Literal.String.Char */\r\n.pygments .sd { color: #D04020 } /* Literal.String.Doc */\r\n.pygments .s2 { background-color: #fff0f0 } /* Literal.String.Double */\r\n.pygments .se { color: #606060; font-weight: bold; background-color: #fff0f0 } /* Literal.String.Escape */\r\n.pygments .sh { background-color: #fff0f0 } /* Literal.String.Heredoc */\r\n.pygments .si { background-color: #e0e0e0 } /* Literal.String.Interpol */\r\n.pygments .sx { color: #D02000; background-color: #fff0f0 } /* Literal.String.Other */\r\n.pygments .sr { color: #000000; background-color: #fff0ff } /* Literal.String.Regex */\r\n.pygments .s1 { background-color: #fff0f0 } /* Literal.String.Single */\r\n.pygments .ss { color: #A06000 } /* Literal.String.Symbol */\r\n.pygments .bp { color: #007020 } /* Name.Builtin.Pseudo */\r\n.pygments .vc { color: #306090 } /* Name.Variable.Class */\r\n.pygments .vg { color: #d07000; font-weight: bold } /* Name.Variable.Global */\r\n.pygments .vi { color: #3030B0 } /* Name.Variable.Instance */\r\n.pygments .il { color: #0000D0; font-weight: bold } /* Literal.Number.Integer.Long */\r\n']
[4, u'small_dark', '2007-06-22 09:48:29', '2007-12-07 09:05:00', None, None, u"The 'small dark' design.", u'/* Kopfgrafik */\r\nhead {\r\n  width: 639px;\r\n}\r\n/* Allgemein */\r\n* {\r\n  color: #8F8F8F;\r\n  font-family:sans-serif;\r\n  font-size:0.95em;\r\n}\r\n\r\na {\r\n  text-decoration:none;\r\n}\r\na img, img {\r\n  border: 0;\r\n  padding: 0px;\r\n  margin: 0px;\r\n}\r\n\r\nbody {\r\n  background-color: #1A252F;\r\n  text-align:center;\r\n}\r\n\r\n#content {\r\n  width: 639px;\r\n  margin:auto;\r\n  text-align:left;\r\n}\r\n\r\n\r\n/* Headlines */\r\n#head {\r\n  font-size: 2em;\r\n  margin: 0.5em;\r\n  padding-left: 1.5em;\r\n  color: #FFF;\r\n}\r\nh1, h2 {\r\n  text-transform:uppercase;\r\n  font-size:0.95em;\r\n  color: white;\r\n}\r\nh2 {\r\n  border-bottom: 1px solid #8F8F8F;\r\n}\r\n\r\n\r\n/* linien */\r\nhr {\r\n  clear: both;\r\n  border-width:1px;\r\n  height:1px;\r\n  padding: 0px;\r\n  margin: 2px 0px 2px 0px;\r\n}\r\nhr.big {\r\n  border-width: 3px;\r\n  height:3px;\r\n  border-style: solid\r\n}\r\nhr.small {\r\n  border-style:dotted;\r\n}\r\n\r\n#nav_footer {\r\n  font-size:0.9em;\r\n}\r\n\r\n\r\n\r\n\r\n/* Hauptmenu */\r\n.main_menu, #footer {\r\n  text-align:center;\r\n  width: 639px;\r\n  padding: 0px;\r\n  margin: 0px;\r\n}\r\n.main_menu ul {\r\n  list-style:none;\r\n}\r\n.main_menu li {\r\n  display:inline;\r\n  padding: 5px;\r\n}\r\n.main_menu a .current, .main_menu a:hover, #footer a {\r\n  color: white;\r\n}\r\n\r\n/* ---------------------------------------------------------------------- */\r\ntextarea {\r\n  width: 100%;\r\n}\r\n.back_links, #permalink {\r\n  font-size: 0.8em;\r\n}\r\n#permalink {\r\n  text-align: right;\r\n  padding: 10px;\r\n}\r\n/* ----------------------------------------------------------------------\r\n   Pygments syntax highlighter\r\n---------------------------------------------------------------------- */\r\n.pygments_code, .pygments_code table, .pygments_code .code, .pygments_code pre {\r\n  background: #ffffff;\r\n  padding: 0;\r\n  margin: 0;\r\n}\r\n.pygments_code pre {\r\n border: 1px;\r\n}\r\n.pygments_code .code {\r\n  width: 100%;\r\n}\r\n.pygments  { background: #ffffff; }\r\n.pygments .c { color: #808080 } /* Comment */\r\n.pygments .err { color: #F00000; background-color: #F0A0A0 } /* Error */\r\n.pygments .k { color: #008000; font-weight: bold } /* Keyword */\r\n.pygments .o { color: #303030 } /* Operator */\r\n.pygments .cm { color: #808080 } /* Comment.Multiline */\r\n.pygments .cp { color: #507090 } /* Comment.Preproc */\r\n.pygments .c1 { color: #808080 } /* Comment.Single */\r\n.pygments .cs { color: #cc0000; font-weight: bold } /* Comment.Special */\r\n.pygments .gd { color: #A00000 } /* Generic.Deleted */\r\n.pygments .ge { font-style: italic } /* Generic.Emph */\r\n.pygments .gr { color: #FF0000 } /* Generic.Error */\r\n.pygments .gh { color: #000080; font-weight: bold } /* Generic.Heading */\r\n.pygments .gi { color: #00A000 } /* Generic.Inserted */\r\n.pygments .go { color: #808080 } /* Generic.Output */\r\n.pygments .gp { color: #c65d09; font-weight: bold } /* Generic.Prompt */\r\n.pygments .gs { font-weight: bold } /* Generic.Strong */\r\n.pygments .gu { color: #800080; font-weight: bold } /* Generic.Subheading */\r\n.pygments .gt { color: #0040D0 } /* Generic.Traceback */\r\n.pygments .kc { color: #008000; font-weight: bold } /* Keyword.Constant */\r\n.pygments .kd { color: #008000; font-weight: bold } /* Keyword.Declaration */\r\n.pygments .kp { color: #003080; font-weight: bold } /* Keyword.Pseudo */\r\n.pygments .kr { color: #008000; font-weight: bold } /* Keyword.Reserved */\r\n.pygments .kt { color: #303090; font-weight: bold } /* Keyword.Type */\r\n.pygments .m { color: #6000E0; font-weight: bold } /* Literal.Number */\r\n.pygments .s { background-color: #fff0f0 } /* Literal.String */\r\n.pygments .na { color: #0000C0 } /* Name.Attribute */\r\n.pygments .nb { color: #007020 } /* Name.Builtin */\r\n.pygments .nc { color: #B00060; font-weight: bold } /* Name.Class */\r\n.pygments .no { color: #003060; font-weight: bold } /* Name.Constant */\r\n.pygments .nd { color: #505050; font-weight: bold } /* Name.Decorator */\r\n.pygments .ni { color: #800000; font-weight: bold } /* Name.Entity */\r\n.pygments .ne { color: #F00000; font-weight: bold } /* Name.Exception */\r\n.pygments .nf { color: #0060B0; font-weight: bold } /* Name.Function */\r\n.pygments .nl { color: #907000; font-weight: bold } /* Name.Label */\r\n.pygments .nn { color: #0e84b5; font-weight: bold } /* Name.Namespace */\r\n.pygments .nt { color: #007000 } /* Name.Tag */\r\n.pygments .nv { color: #906030 } /* Name.Variable */\r\n.pygments .ow { color: #000000; font-weight: bold } /* Operator.Word */\r\n.pygments .w { color: #bbbbbb } /* Text.Whitespace */\r\n.pygments .mf { color: #6000E0; font-weight: bold } /* Literal.Number.Float */\r\n.pygments .mh { color: #005080; font-weight: bold } /* Literal.Number.Hex */\r\n.pygments .mi { color: #0000D0; font-weight: bold } /* Literal.Number.Integer */\r\n.pygments .mo { color: #4000E0; font-weight: bold } /* Literal.Number.Oct */\r\n.pygments .sb { background-color: #fff0f0 } /* Literal.String.Backtick */\r\n.pygments .sc { color: #0040D0 } /* Literal.String.Char */\r\n.pygments .sd { color: #D04020 } /* Literal.String.Doc */\r\n.pygments .s2 { background-color: #fff0f0 } /* Literal.String.Double */\r\n.pygments .se { color: #606060; font-weight: bold; background-color: #fff0f0 } /* Literal.String.Escape */\r\n.pygments .sh { background-color: #fff0f0 } /* Literal.String.Heredoc */\r\n.pygments .si { background-color: #e0e0e0 } /* Literal.String.Interpol */\r\n.pygments .sx { color: #D02000; background-color: #fff0f0 } /* Literal.String.Other */\r\n.pygments .sr { color: #000000; background-color: #fff0ff } /* Literal.String.Regex */\r\n.pygments .s1 { background-color: #fff0f0 } /* Literal.String.Single */\r\n.pygments .ss { color: #A06000 } /* Literal.String.Symbol */\r\n.pygments .bp { color: #007020 } /* Name.Builtin.Pseudo */\r\n.pygments .vc { color: #306090 } /* Name.Variable.Class */\r\n.pygments .vg { color: #d07000; font-weight: bold } /* Name.Variable.Global */\r\n.pygments .vi { color: #3030B0 } /* Name.Variable.Instance */\r\n.pygments .il { color: #0000D0; font-weight: bold } /* Literal.Number.Integer.Long */\r\n']
[5, u'elementary', '2007-06-22 09:48:29', '2007-12-07 09:04:06', None, None, u"The 'elementary' design. Ideal as a basis for your own design.", u'body{\r\n  font-size:0.9em;\r\n  background: snow;\r\n  margin: 15px 10% 15px 10%;\r\n}\r\n\r\n#headline {\r\n  background: moccasin;\r\n  padding: 10px;\r\n  border: 1px solid black;\r\n}\r\n\r\n.main_menu {\r\n  background: navajowhite;\r\n  float: left;\r\n  padding: 15px;\r\n  margin: 10px;\r\n}\r\n.main_menu ul {\r\n  padding: 0;\r\n}\r\n.main_menu ul ul {\r\n  /* indent submenu */\r\n  padding-left: 1.5em;\r\n  font-size:0.9em; /* smaller font for subitems */\r\n}\r\n.main_menu li {\r\n  list-style:none;\r\n}\r\na {\r\n  color: slategray;\r\n  text-decoration: none;\r\n}\r\na:hover, a .current {\r\n  background-color: orange;\r\n  text-decoration: underline;\r\n}\r\n#main_content {\r\n  background: lightyellow;\r\n  padding: 5px;\r\n  border: 1px solid black;\r\n}\r\n\r\n#footer {\r\n  border: 1px solid black;\r\n  padding: 5px;\r\n  font-size: 0.9em;\r\n  text-align: center;\r\n}\r\n\r\n/* ---------------------------------------------------------------------- */\r\ntextarea {\r\n  width: 100%;\r\n}\r\n.back_links, #permalink {\r\n  font-size: 0.8em;\r\n}\r\n#permalink {\r\n  text-align: right;\r\n  padding: 10px;\r\n}\r\n/* ----------------------------------------------------------------------\r\n   Pygments syntax highlighter\r\n---------------------------------------------------------------------- */\r\n.pygments_code, .pygments_code table, .pygments_code .code, .pygments_code pre {\r\n  background: #ffffff;\r\n  padding: 0;\r\n  margin: 0;\r\n}\r\n.pygments_code pre {\r\n border: 1px;\r\n}\r\n.pygments_code .code {\r\n  width: 100%;\r\n}\r\n.pygments  { background: #ffffff; }\r\n.pygments .c { color: #808080 } /* Comment */\r\n.pygments .err { color: #F00000; background-color: #F0A0A0 } /* Error */\r\n.pygments .k { color: #008000; font-weight: bold } /* Keyword */\r\n.pygments .o { color: #303030 } /* Operator */\r\n.pygments .cm { color: #808080 } /* Comment.Multiline */\r\n.pygments .cp { color: #507090 } /* Comment.Preproc */\r\n.pygments .c1 { color: #808080 } /* Comment.Single */\r\n.pygments .cs { color: #cc0000; font-weight: bold } /* Comment.Special */\r\n.pygments .gd { color: #A00000 } /* Generic.Deleted */\r\n.pygments .ge { font-style: italic } /* Generic.Emph */\r\n.pygments .gr { color: #FF0000 } /* Generic.Error */\r\n.pygments .gh { color: #000080; font-weight: bold } /* Generic.Heading */\r\n.pygments .gi { color: #00A000 } /* Generic.Inserted */\r\n.pygments .go { color: #808080 } /* Generic.Output */\r\n.pygments .gp { color: #c65d09; font-weight: bold } /* Generic.Prompt */\r\n.pygments .gs { font-weight: bold } /* Generic.Strong */\r\n.pygments .gu { color: #800080; font-weight: bold } /* Generic.Subheading */\r\n.pygments .gt { color: #0040D0 } /* Generic.Traceback */\r\n.pygments .kc { color: #008000; font-weight: bold } /* Keyword.Constant */\r\n.pygments .kd { color: #008000; font-weight: bold } /* Keyword.Declaration */\r\n.pygments .kp { color: #003080; font-weight: bold } /* Keyword.Pseudo */\r\n.pygments .kr { color: #008000; font-weight: bold } /* Keyword.Reserved */\r\n.pygments .kt { color: #303090; font-weight: bold } /* Keyword.Type */\r\n.pygments .m { color: #6000E0; font-weight: bold } /* Literal.Number */\r\n.pygments .s { background-color: #fff0f0 } /* Literal.String */\r\n.pygments .na { color: #0000C0 } /* Name.Attribute */\r\n.pygments .nb { color: #007020 } /* Name.Builtin */\r\n.pygments .nc { color: #B00060; font-weight: bold } /* Name.Class */\r\n.pygments .no { color: #003060; font-weight: bold } /* Name.Constant */\r\n.pygments .nd { color: #505050; font-weight: bold } /* Name.Decorator */\r\n.pygments .ni { color: #800000; font-weight: bold } /* Name.Entity */\r\n.pygments .ne { color: #F00000; font-weight: bold } /* Name.Exception */\r\n.pygments .nf { color: #0060B0; font-weight: bold } /* Name.Function */\r\n.pygments .nl { color: #907000; font-weight: bold } /* Name.Label */\r\n.pygments .nn { color: #0e84b5; font-weight: bold } /* Name.Namespace */\r\n.pygments .nt { color: #007000 } /* Name.Tag */\r\n.pygments .nv { color: #906030 } /* Name.Variable */\r\n.pygments .ow { color: #000000; font-weight: bold } /* Operator.Word */\r\n.pygments .w { color: #bbbbbb } /* Text.Whitespace */\r\n.pygments .mf { color: #6000E0; font-weight: bold } /* Literal.Number.Float */\r\n.pygments .mh { color: #005080; font-weight: bold } /* Literal.Number.Hex */\r\n.pygments .mi { color: #0000D0; font-weight: bold } /* Literal.Number.Integer */\r\n.pygments .mo { color: #4000E0; font-weight: bold } /* Literal.Number.Oct */\r\n.pygments .sb { background-color: #fff0f0 } /* Literal.String.Backtick */\r\n.pygments .sc { color: #0040D0 } /* Literal.String.Char */\r\n.pygments .sd { color: #D04020 } /* Literal.String.Doc */\r\n.pygments .s2 { background-color: #fff0f0 } /* Literal.String.Double */\r\n.pygments .se { color: #606060; font-weight: bold; background-color: #fff0f0 } /* Literal.String.Escape */\r\n.pygments .sh { background-color: #fff0f0 } /* Literal.String.Heredoc */\r\n.pygments .si { background-color: #e0e0e0 } /* Literal.String.Interpol */\r\n.pygments .sx { color: #D02000; background-color: #fff0f0 } /* Literal.String.Other */\r\n.pygments .sr { color: #000000; background-color: #fff0ff } /* Literal.String.Regex */\r\n.pygments .s1 { background-color: #fff0f0 } /* Literal.String.Single */\r\n.pygments .ss { color: #A06000 } /* Literal.String.Symbol */\r\n.pygments .bp { color: #007020 } /* Name.Builtin.Pseudo */\r\n.pygments .vc { color: #306090 } /* Name.Variable.Class */\r\n.pygments .vg { color: #d07000; font-weight: bold } /* Name.Variable.Global */\r\n.pygments .vi { color: #3030B0 } /* Name.Variable.Instance */\r\n.pygments .il { color: #0000D0; font-weight: bold } /* Literal.Number.Integer.Long */\r\n']
[6, u'small_white', '2007-06-22 09:48:29', '2007-12-07 08:53:09', None, None, u"The 'small white' design.", u'/* ----------------------------------------------------------------------\r\n   based on a open source xhtml/css website layout\r\n   by Andreas Viklund  - http://andreasviklund.com\r\n   modify by Martin Bergner - www.um-gottes-willen.net\r\n   modify2 by Jens Diemer - www.jensdiemer.de\r\n---------------------------------------------------------------------- */\r\n\r\n* {\r\n  color: #000000\r\n}\r\n\r\nbody {\r\n  margin: 0;\r\n  padding: 5px 0 5px 0;\r\n  font-size:0.8em;\r\n  font-family: tahoma, arial, sans-serif;\r\n  background:#ddd;\r\n}\r\n\r\na {\r\n  text-decoration:none;\r\n  font-weight:bold;\r\n  color:#286ea0;\r\n  background-color:inherit;\r\n}\r\na:hover {\r\n  text-decoration:underline;\r\n  color:#286ea0;\r\n  background-color:inherit;\r\n}\r\na img {\r\n  border:0;\r\n}\r\n.hide {\r\n  display: none;\r\n}\r\n\r\n#header {\r\n  margin: 0;\r\n\r\n  text-align:center;\r\n  background-image:url(/_static/pylucid_logo_2_1x76.jpg)\r\n}\r\n#pylucid_logo {\r\n  border: 0;\r\n}\r\n\r\n#wrap {\r\n  background:#ffffff;\r\n  margin:0 auto;\r\n  width: 85%;\r\n}\r\n\r\n#contentwide {\r\n  margin:0 0 5px 25%;\r\n  border-left:1px solid #f0f0f0;\r\n  padding:0 0 0 10px;\r\n  line-height:1.2em;\r\n}\r\n\r\n#leftside {\r\n  /*\r\n  includes the menu + search plugin\r\n  */\r\n  float:left;\r\n  padding: 0 0 0 10px;\r\n}\r\n\r\n.search input, .search button {\r\n  font-size: 0.85em;\r\n  border: 1px solid #444;\r\n  padding: 1px;\r\n}\r\n\r\n.main_menu {\r\n  font-size:0.9em;\r\n  padding: 0;\r\n  margin: 0;\r\n}\r\n\r\n.main_menu ul {\r\n  padding: 0;\r\n}\r\n\r\n.main_menu ul ul {\r\n  /* indent submenu */\r\n  padding: 0 0 0 1.5em;\r\n  font-size:0.95em; /* smaller font for subitems */\r\n}\r\n\r\n.main_menu li {\r\n  list-style:none;\r\n  padding: 0;\r\n  margin: 0;\r\n}\r\n\r\n.main_menu li a {\r\n  display: block;\r\n  width: 140px;\r\n  background-color: #f4f4f4;\r\n  color: #505050;\r\n  font-weight: bold;\r\n  padding: 4px;\r\n  margin: 2px;\r\n  border-left: 4px solid #cccccc;\r\n  text-decoration: none;\r\n}\r\n\r\n.main_menu li a:hover {\r\n  background-color: #eaeaea;\r\n  border-left: 4px solid #286ea0;\r\n  color: #505050;\r\n}\r\n.main_menu li a .current {\r\n  background-color: #ddd;\r\n}\r\n\r\n#footer * {\r\n  color: #808080;\r\n}\r\n#footer {\r\n  clear: both;\r\n  margin: 0 auto;\r\n  padding: 10px 0 20px;\r\n  border-top: 4px solid #f0f0f0;\r\n  text-align: center;\r\n  font-size: 0.8em;\r\n}\r\n#footer a {\r\n  background-color: inherit;\r\n  text-decoration: none;\r\n}\r\n\r\n#footer a:hover {\r\n  text-decoration: underline;\r\n}\r\n\r\n/* ----------------------------------------------------------------------------\r\n   internal\r\n------------------------------------------------------------------------------- */\r\ntextarea {\r\n  /* all text areas should use the full width */\r\n  width: 100%;\r\n}\r\n.PyLucidPlugins.search {\r\n  display: block;\r\n  margin: 0;\r\n  border-top: 1px solid #f0f0f0;\r\n}\r\n.back_links, #permalink {\r\n  font-size: 0.8em;\r\n}\r\n#permalink {\r\n  text-align: right;\r\n  padding: 10px;\r\n}\r\n\r\n.pygments_code, .pygments_code table, .pygments_code .code, .pygments_code pre {\r\n  background: #ffffff;\r\n  padding: 0;\r\n  margin: 0;\r\n}\r\n.pygments_code pre {\r\n border: 1px;\r\n}\r\n.pygments_code .code {\r\n  width: 100%;\r\n}\r\n\r\n/* ----------------------------------------------------------------------\r\n   Pygments syntax highlighter\r\n---------------------------------------------------------------------- */\r\n.pygments  { background: #ffffff; }\r\n.pygments .c { color: #808080 } /* Comment */\r\n.pygments .err { color: #F00000; background-color: #F0A0A0 } /* Error */\r\n.pygments .k { color: #008000; font-weight: bold } /* Keyword */\r\n.pygments .o { color: #303030 } /* Operator */\r\n.pygments .cm { color: #808080 } /* Comment.Multiline */\r\n.pygments .cp { color: #507090 } /* Comment.Preproc */\r\n.pygments .c1 { color: #808080 } /* Comment.Single */\r\n.pygments .cs { color: #cc0000; font-weight: bold } /* Comment.Special */\r\n.pygments .gd { color: #A00000 } /* Generic.Deleted */\r\n.pygments .ge { font-style: italic } /* Generic.Emph */\r\n.pygments .gr { color: #FF0000 } /* Generic.Error */\r\n.pygments .gh { color: #000080; font-weight: bold } /* Generic.Heading */\r\n.pygments .gi { color: #00A000 } /* Generic.Inserted */\r\n.pygments .go { color: #808080 } /* Generic.Output */\r\n.pygments .gp { color: #c65d09; font-weight: bold } /* Generic.Prompt */\r\n.pygments .gs { font-weight: bold } /* Generic.Strong */\r\n.pygments .gu { color: #800080; font-weight: bold } /* Generic.Subheading */\r\n.pygments .gt { color: #0040D0 } /* Generic.Traceback */\r\n.pygments .kc { color: #008000; font-weight: bold } /* Keyword.Constant */\r\n.pygments .kd { color: #008000; font-weight: bold } /* Keyword.Declaration */\r\n.pygments .kp { color: #003080; font-weight: bold } /* Keyword.Pseudo */\r\n.pygments .kr { color: #008000; font-weight: bold } /* Keyword.Reserved */\r\n.pygments .kt { color: #303090; font-weight: bold } /* Keyword.Type */\r\n.pygments .m { color: #6000E0; font-weight: bold } /* Literal.Number */\r\n.pygments .s { background-color: #fff0f0 } /* Literal.String */\r\n.pygments .na { color: #0000C0 } /* Name.Attribute */\r\n.pygments .nb { color: #007020 } /* Name.Builtin */\r\n.pygments .nc { color: #B00060; font-weight: bold } /* Name.Class */\r\n.pygments .no { color: #003060; font-weight: bold } /* Name.Constant */\r\n.pygments .nd { color: #505050; font-weight: bold } /* Name.Decorator */\r\n.pygments .ni { color: #800000; font-weight: bold } /* Name.Entity */\r\n.pygments .ne { color: #F00000; font-weight: bold } /* Name.Exception */\r\n.pygments .nf { color: #0060B0; font-weight: bold } /* Name.Function */\r\n.pygments .nl { color: #907000; font-weight: bold } /* Name.Label */\r\n.pygments .nn { color: #0e84b5; font-weight: bold } /* Name.Namespace */\r\n.pygments .nt { color: #007000 } /* Name.Tag */\r\n.pygments .nv { color: #906030 } /* Name.Variable */\r\n.pygments .ow { color: #000000; font-weight: bold } /* Operator.Word */\r\n.pygments .w { color: #bbbbbb } /* Text.Whitespace */\r\n.pygments .mf { color: #6000E0; font-weight: bold } /* Literal.Number.Float */\r\n.pygments .mh { color: #005080; font-weight: bold } /* Literal.Number.Hex */\r\n.pygments .mi { color: #0000D0; font-weight: bold } /* Literal.Number.Integer */\r\n.pygments .mo { color: #4000E0; font-weight: bold } /* Literal.Number.Oct */\r\n.pygments .sb { background-color: #fff0f0 } /* Literal.String.Backtick */\r\n.pygments .sc { color: #0040D0 } /* Literal.String.Char */\r\n.pygments .sd { color: #D04020 } /* Literal.String.Doc */\r\n.pygments .s2 { background-color: #fff0f0 } /* Literal.String.Double */\r\n.pygments .se { color: #606060; font-weight: bold; background-color: #fff0f0 } /* Literal.String.Escape */\r\n.pygments .sh { background-color: #fff0f0 } /* Literal.String.Heredoc */\r\n.pygments .si { background-color: #e0e0e0 } /* Literal.String.Interpol */\r\n.pygments .sx { color: #D02000; background-color: #fff0f0 } /* Literal.String.Other */\r\n.pygments .sr { color: #000000; background-color: #fff0ff } /* Literal.String.Regex */\r\n.pygments .s1 { background-color: #fff0f0 } /* Literal.String.Single */\r\n.pygments .ss { color: #A06000 } /* Literal.String.Symbol */\r\n.pygments .bp { color: #007020 } /* Name.Builtin.Pseudo */\r\n.pygments .vc { color: #306090 } /* Name.Variable.Class */\r\n.pygments .vg { color: #d07000; font-weight: bold } /* Name.Variable.Global */\r\n.pygments .vi { color: #3030B0 } /* Name.Variable.Instance */\r\n.pygments .il { color: #0000D0; font-weight: bold } /* Literal.Number.Integer.Long */\r\n']
]