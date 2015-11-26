#!/usr/bin/python
#   Written against python 2.7
#   Matasano Problem 1
#
#   Created by 404 on 15/11/26.
#
#   Copyright (c) 2015 404. All rights reserved.


from base64 import b64encode

c = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
# decode with hex
m = c.decode('hex')
# encode with base64
print b64encode(m)
