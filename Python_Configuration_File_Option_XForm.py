# Python Configuration File Parser
# configparser — Configuration file parser
# This module provides the ConfigParser class which implements a basic configuration language which provides a structure similar to what’s found in
# Microsoft Windows INI files. You can use this to write Python programs which can be customized by end users easily.
#
# optionxform(option). 
# Transforms the option name option as found in an input file or as passed in by client code to the form that should be used in the internal structures.
# The default implementation returns a lower-case version of option; subclasses may override this or client code can set an attribute of this name on
# instances to affect this behavior.
# 
# You don’t need to subclass the parser to use this method, you can also set it on an instance, to a function that takes a string argument and returns a 
# string. Setting it to str, for example, would make option names case sensitive:
# 

cfgparser = ConfigParser()
cfgparser.optionxform = str
 
#
# Note that when reading configuration files, whitespace around the option names is stripped before optionxform() is called.
#
