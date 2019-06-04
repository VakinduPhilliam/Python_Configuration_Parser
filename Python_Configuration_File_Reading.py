# Python Configuration File Parser
# configparser — Configuration file parser
# This module provides the ConfigParser class which implements a basic configuration language which provides a structure similar to what’s found in
# Microsoft Windows INI files. You can use this to write Python programs which can be customized by end users easily.
#
# An example of reading the configuration file:
# 

import configparser

config = configparser.RawConfigParser()
config.read('example.cfg')

# getfloat() raises an exception if the value is not a float
# getint() and getboolean() also do this for their respective types

a_float = config.getfloat('Section1', 'a_float')
an_int = config.getint('Section1', 'an_int')

print(a_float + an_int)

# Notice that the next output does not interpolate '%(bar)s' or '%(baz)s'.
# This is because we are using a RawConfigParser().

if config.getboolean('Section1', 'a_bool'):
    print(config.get('Section1', 'foo'))
