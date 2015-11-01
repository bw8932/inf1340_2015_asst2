#!/usr/bin/env python

""" Assignment 2, Exercise 2, INF1340, Fall, 2015. DNA Sequencing

This module converts performs substring matching for DNA sequencing

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"


#DNA Sequencing

#Determine or of nucleotide bases in a molecule of DNA
#Nucleotide bases: adenine, thymine, cytosine, guanine
#Nucleotide bases: A, T, C, G

#Substring Matching: determine whether a shorter string
    #is contained within a longer string.

#find(substring, start, end) returns lowest
    #index(integer) where substring is found in the
    #index range start <_ index < end.
    #If substring not found -1 is returned.

#functions to add.
    #Write loop to do letter by letter comparison.
    #String to search must be an argument.

    #Write function that returns a string with zero or more indices separated by commas.
    #String will contain digits representing the integer indices.
    #If substring not found an empty string returned.

input_string = raw_input("Enter DNA sequence: ")
substring = raw_input("Enter substring: ")

def find_string():
    index = 0
    if substring.upper() in input_string.upper():
        print substring, "found within", input_string
    else:
        print substring, "not found within", input_string
find_string()

def find_string_2():
   index = 0
   while index < len(input_string):
        index = input_string.find(substring, index)
        if index == -1:
            break
        index += 1
        print substring, "found at", index
find_string_2()

#For some reason the index is off by +1, if the actual position is 0 it shows 1, if 6 then 7. Need to fix..