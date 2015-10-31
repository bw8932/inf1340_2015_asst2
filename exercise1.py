#!/usr/bin/env python

""" Assignment 2, Exercise 1, INF1340, Fall, 2015. Pig Latin

This module converts English words to Pig Latin words

"""



__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"


def pig_latinify(word):
    """
    Translate an english word into piglatin.

    :param word:  a word
    :return:  the resulting word in piglatin
    :raises:

    """
    word = str(word)
    vowels = "aeiou"
    prefix = ""
    if word[0] in vowels:
        result = word + "yay"

    else:
        while word[0] not in vowels:
            prefix += word[0]
            word = word[1:len(word)]
        result = word + prefix + "ay"

    print result
    return result

pig_latinify("stew")