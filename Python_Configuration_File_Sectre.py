# Python Configuration File Parser
# configparser — Configuration file parser
# This module provides the ConfigParser class which implements a basic configuration language which provides a structure similar to what’s found in
# Microsoft Windows INI files. You can use this to write Python programs which can be customized by end users easily.
#
# ConfigParser.SECTCRE 
# A compiled regular expression used to parse section headers. The default matches [section] to the name "section". 
# Whitespace is considered part of the section name, thus [  larch  ] will be read as a section of name "  larch  ". 
# Override this attribute if that’s unsuitable. For example:
 
import re

config = """
    [Section 1]
    option = value

    [  Section 2  ]
    another = val
    """

typical = configparser.ConfigParser()
typical.read_string(config)

typical.sections()

# OUTPUT: '['Section 1', '  Section 2  ']'

custom = configparser.ConfigParser()
custom.SECTCRE = re.compile(r"\[ *(?P<header>[^]]+?) *\]")

custom.read_string(config)

custom.sections()

# OUTPUT: '['Section 1', 'Section 2']'
