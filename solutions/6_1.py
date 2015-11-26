# !/usr/bin/python
#   Written against python 2.7
#   Matasano Problem 6
#
#   Created by 404 on 15/11/26.
#
#   Copyright (c) 2015 404. All rights reserved.

# a function to calculate the hamming distance,test with 'this is a test',output correct.

# def hamming_distance(s1,s2):
# 	c1 = bin(int(s1.encode('hex'),16))[2:]
# 	c2 = bin(int(s2.encode('hex'),16))[2:]
# 	score = 0 
# 	for j in xrange(len(c1)):
# 		if c1[j]!=c2[j]:
# 			score+=1
# 	return score

# s1 = 'this is a test'
# s2 = 'wokka wokka!!!'
# print hamming_distance(s1, s2)

from itertools import combinations
from base64 import b64decode
from operator import itemgetter

character_frequency = {
    'e': 27,
    't': 26,
    'a': 25,
    'o': 24,
    'i': 23,
    'n': 22,
    's': 21,
    'r': 20,
    'h': 19,
    'l': 18,
    'd': 17,
    'c': 16,
    'u': 15,
    'm': 14,
    'f': 13,
    'p': 12,
    'g': 11,
    'w': 10,
    'y': 9,
    'b': 8,
    'v': 7,
    'k': 6,
    'x': 5,
    ' ': 4,
    'j': 3,
    'q': 2,
    'z': 1
}

# use one byte key_value to XOR input_bytes bytes by bytes.Out put the XORed string.
def xor_singlechar(input_bytes, key_value):
    output = b''

    for char in input_bytes:
        output += bytes([char ^ key_value])

    return output


# calculate the sum of the score of every bytes of possible plaintext.
# so that the max one of them may be the correct one.
def xor_find_singlechar_key(ciphertext):
    candidates = list()

    for key_candidate in range(256):
        total_score = 0
        plaintext_candidate = xor_singlechar(ciphertext, key_candidate)

        for byte in plaintext_candidate:
            char_score = character_frequency.get(chr(byte), 0)
            total_score += char_score

        # We might as well include the plaintext in the output since
        # it's used in some of the challenges.
        result = {
            'key': key_candidate,
            'score': total_score,
            'plaintext': plaintext_candidate
        }

        candidates.append(result)

    winner = max(candidates, key=itemgetter('score'))

    return winner


def transpose(list_of_chunks):
    max_chunklength = len(list_of_chunks[0])

    result = []

    for position in range(0, max_chunklength):
        new_chunk = b''

        for chunk in list_of_chunks:
            try:
                char = chunk[position]
                new_chunk += bytes([char])
            except IndexError:
                break

        result.append(new_chunk)

    return result


def divide(input, denominator):
    """Take a string or bytes object and divide it into parts of "denominator"
    length.
    """
    result = []
    for i in range(0, len(input), denominator):
        chunk = input[i:i + denominator]
        result.append(chunk)
    return result


def popcount(x):
    """Return the number of set bits in an integer (a.k.a the Hamming weight).
    """

    return bin(x).count('1')


def hamming_distance(a, b):
    """Take two bytes objects and return the number of differing bits
    (a.k.a. the Hamming distance).
    """

    total_score = 0

    for (byte_a, byte_b) in zip(a, b):
        current_score = popcount(byte_a ^ byte_b)
        total_score += current_score

    return total_score


def xor_find_multichar_key(ciphertext):
    def get_aggregated_sample_score(keysize):
        number_of_samples = 6

        sample_material = ciphertext[:(keysize * number_of_samples)]
        # print(sample_material)

        chunks = divide(sample_material, keysize)
        # print(chunks)

        total_score = 0

        # After advise from Rami__ in the #cryptopals channel on Freenode, I
        # have chosen to take a total of six samples and compare every
        # combination of these samples.

        for (x, y) in combinations(chunks, 2):
            total_score += hamming_distance(x, y)

        normalized_score = total_score / keysize

        return normalized_score

    def determine_keysize():
        keysize_candidates = []

        for i in range(2, 41):
            keysize_candidates.append((i, get_aggregated_sample_score(i)))

        # print(keysize_candidates)

        best_candidate = min(keysize_candidates, key=itemgetter(1))
        # print(best_candidate)
        keysize = best_candidate[0]

        return keysize

    keysize = determine_keysize()
    print(keysize)

    key_material = transpose(divide(ciphertext, keysize))
    print(key_material)
    plaintext = b''

    for char in key_material:
        char_value = xor_find_singlechar_key(char)["key"]
        plaintext += bytes([char_value])

    return plaintext


ciphertext = b64decode(open('6.txt', 'r').read())

key_bytes = xor_find_multichar_key(ciphertext)

print(key_bytes)
