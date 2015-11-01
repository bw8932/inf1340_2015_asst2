#!/usr/bin/env python

""" Assignment 2, Exercise 1, INF1340, Fall, 2015. Pig Latin

This module converts English words to Pig Latin words

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"

#Create a function..
def pig_latinify(word):
    #If a word begins with a vowel, append "yay" to the end of the word.
    if word[0].upper() in ["A", "E", "I", "O", "U"]:
        print word[0:] + "yay"
        return
    #If the word begins with a consonant, remove all the consonants from beginning up to the first vowel and append them to the end of the word. Then append "ay" to end.
    #create index with a starting position of 0.
    index = 0
    #create store variable with no content; used to capture consonants and store for later use
    store = ""
    #loop through every character in the word.
    for character in word:
      if character.upper() not in ["A", "E", "I", "O", "U"]:
        store = store + character
      else:
        break #if character is not a vowel, else means if it is a vowel then the break stops it

    index += 1
    #the new word is created by finding the position up to the the first vowel, adding the stored characters to the end, then adding "ay".
    new_word = word[index:] + store + "ay"
    print new_word

#Have user enter word to translate.
pig_latinify(raw_input("Enter a word to translate into Pig Latin: "))


