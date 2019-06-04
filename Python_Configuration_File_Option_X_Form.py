# Python Configuration File Parser
# configparser — Configuration file parser
# This module provides the ConfigParser class which implements a basic configuration language which provides a structure similar to what’s found in
# Microsoft Windows INI files. You can use this to write Python programs which can be customized by end users easily.
#
# ConfigParser.optionxform(option)> 
# This method transforms option names on every read, get, or set operation.
# The default converts the name to lowercase.
# This also means that when a configuration file gets written, all keys will be lowercase.
# Override this method if that’s unsuitable.
#
# For example:
# 

config = """
    [Section1]
    Key = Value

    [Section2]
    AnotherKey = Value
    """
typical = configparser.ConfigParser()
typical.read_string(config)

list(typical['Section1'].keys())

# OUTPUT: '['key']'

list(typical['Section2'].keys())

# OUTPUT: '['anotherkey']'

custom = configparser.RawConfigParser()

custom.optionxform = lambda option: option

custom.read_string(config)

list(custom['Section1'].keys())

# OUTPUT: '['Key']'

list(custom['Section2'].keys())

# OUTPUT: '['AnotherKey']'
