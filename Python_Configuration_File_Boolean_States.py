# Python Configuration File Parser
# configparser — Configuration file parser
# This module provides the ConfigParser class which implements a basic configuration language which provides a structure similar to what’s found in
# Microsoft Windows INI files. You can use this to write Python programs which can be customized by end users easily.
#
# ConfigParser.BOOLEAN_STATES 
# By default when using getboolean(), config parsers consider the following values True: '1', 'yes', 'true', 'on' and the following values False: '0', 'no',
# 'false', 'off'. You can override this by specifying a custom dictionary of strings and their Boolean outcomes.
#
# For example:
# 

custom = configparser.ConfigParser()
custom['section1'] = {'funky': 'nope'}

custom['section1'].getboolean('funky')

# Traceback (most recent call last):
# ...
# ValueError: Not a boolean: nope

custom.BOOLEAN_STATES = {'sure': True, 'nope': False}

custom['section1'].getboolean('funky')

# OUTPUT: 'False'
