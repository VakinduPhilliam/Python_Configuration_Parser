# Python Configuration File Parser
# configparser — Configuration file parser
# This module provides the ConfigParser class which implements a basic configuration language which provides a structure similar to what’s found in
# Microsoft Windows INI files. You can use this to write Python programs which can be customized by end users easily.
#
# Fallback Values.
# As with a dictionary, you can use a section’s get() method to provide fallback values:
# 

topsecret.get('Port')

# OUTPUT: '50022'

topsecret.get('CompressionLevel')

# OUTPUT: '9'

topsecret.get('Cipher')
topsecret.get('Cipher', '3des-cbc')

# OUTPUT: '3des-cbc'
 
#
# Please note that default values have precedence over fallback values.
# For instance, in our example the 'CompressionLevel' key was specified only in the 'DEFAULT' section.
# If we try to get it from the section 'topsecret.server.com', we will always get the default, even if we specify a fallback:
# 

topsecret.get('CompressionLevel', '3')

# OUTPUT: '9'
 
#
# One more thing to be aware of is that the parser-level get() method provides a custom, more complex interface, maintained for backwards compatibility.
# When using this method, a fallback value can be provided via the fallback keyword-only argument:
# 

config.get('bitbucket.org', 'monster',
               fallback='No such things as monsters')

# OUTPUT: 'No such things as monsters'

# 
# The same fallback argument can be used with the getint(), getfloat() and getboolean() methods, for example:
# 

'BatchMode' in topsecret

# OUTPUT: 'False'

topsecret.getboolean('BatchMode', fallback=True)

# OUTPUT: 'True'

config['DEFAULT']['BatchMode'] = 'no'

topsecret.getboolean('BatchMode', fallback=True)

# OUTPUT: 'False'
