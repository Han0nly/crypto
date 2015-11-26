# !/usr/bin/python
#   Written against python 2.7
#   Matasano Problem 9
#
#   Created by 404 on 15/11/26.
#
#   Copyright (c) 2015 404. All rights reserved.


def pkcs7pad(message, key):
    message_len = len(message)
    pad = chr(key - message_len % key) * (key - message_len % key)
    return message + pad


plaintext = "YELLOW SUBMARINE"
k = 20
print pkcs7pad(plaintext, k).encode('hex')
