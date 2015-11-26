# !/usr/bin/python
#   Written against python 2.7
#   Matasano Problem 5
#
#   Created by 404 on 15/11/26.
#
#   Copyright (c) 2015 404. All rights reserved.

mt = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
key = "ICE"

# sequentially apply each byte of the key;
# the first byte of plaintext will be XOR'd against I, the next C, the next E, then I again for the 4th byte, and so on.
ct = ''
for i in range(len(mt)):
    ct += chr(ord(mt[i]) ^ ord(key[i % len(key)]))

print ct.encode('hex')
