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
    Translate an English word into Pig Latin.

    :param word: a word
    :return: the resulting word in Pig Latin
    :raises: MismatchedAttributesException:
    """

    vowels = ["A", "E", "I", "O", "U"]

    # If a word begins with a vowel, append "yay" to the end of the word.
    if word[0].upper() in vowels:
        new_word = word + "yay"
        print new_word.lower()
        return new_word.lower()

    # If the word begins with a consonant, remove all the consonants from beginning up to the first vowel
    # Then append them to the end of the word, followed by "ay"
    else:
        # Create prefix variable to capture consonants and store for later use
        prefix = ""
        # Loop through every character in the word until encounter vowel, then stop looping
        while word[0].upper() not in vowels:
            prefix += word[0]
            word = word[1:len(word)]

    new_word = word + prefix + "ay"
    return new_word.lower()

# Have user enter word to translate.
pig_latinify("Shiny")