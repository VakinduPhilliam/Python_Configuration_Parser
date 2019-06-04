# Python Configuration File Parser
# configparser — Configuration file parser
# This module provides the ConfigParser class which implements a basic configuration language which provides a structure similar to what’s found in
# Microsoft Windows INI files. You can use this to write Python programs which can be customized by end users easily.
# Supported Datatypes:
# Config parsers do not guess datatypes of values in configuration files, always storing them internally as strings.
# This means that if you need other datatypes, you should convert on your own:
# 

int(topsecret['Port'])

# OUTPUT: '50022'

float(topsecret['CompressionLevel'])

# OUTPUT: '9.0'

# 
# Since this task is so common, config parsers provide a range of handy getter methods to handle integers, floats and booleans.
# The last one is the most interesting because simply passing the value to bool() would do no good since bool('False') is still True.
# This is why config parsers also provide getboolean(). This method is case-insensitive and recognizes Boolean values from 'yes'/'no', 'on'/'off', 
# 'true'/'false' and '1'/'0' [1]. For example:
# 

topsecret.getboolean('ForwardX11')

# OUTPUT: 'False'

config['bitbucket.org'].getboolean('ForwardX11')

# OUTPUT: 'True'

config.getboolean('bitbucket.org', 'Compression')

# OUTPUT: 'True'
