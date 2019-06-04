# Python Configuration File Parser
# configparser — Configuration file parser
# This module provides the ConfigParser class which implements a basic configuration language which provides a structure similar to what’s found in
# Microsoft Windows INI files. You can use this to write Python programs which can be customized by end users easily.
#
# readfp(fp, filename=None). 
# readfp() now iterates on fp instead of calling fp.readline().
# For existing code calling readfp() with arguments which don’t support iteration, the following generator may be used as a wrapper around the file-like
# object:
# 

def readline_generator(fp):
    line = fp.readline()

    while line:
        yield line

        line = fp.readline()
 
#
# Instead of parser.readfp(fp) use parser.read_file(readline_generator(fp)).
#