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


def find(input_string, substring, start, end):
    """
    Find the first instance of a substring within a string in a specific range; return the index of the substring.

    :param input_string: a longer string in which you wish to find a substring
    :param substring: the string you wish to find
    :param start: an integer - the first index at which to seek the substring in the input_string
    :param end: an integer - the last index a which to seek the substring in the input_string
    :return: index at which the substring is found in the larger string
    """

    # Set index to start to give initial index point.
    index = start
    # Define found marker's base state.
    found = 0
    # Loop through a series of slices of the input_string, checking each against the substring for a match.
    for input_slice in input_string[start:end]:
        input_slice = input_string[index:index + len(substring)]
        index += 1
        # If substring found, change found marker to 1 and return the index
        if input_slice == substring:
            found = 1
            print (index - 1)
            return (index - 1)


    # If function completes loop with found marker in base state, means no match; return -1.
    if found == 0:
        print -1
        return -1
# Will not work if index is above length of
find("012345678989", "8a", 0, 11)


def multi_find(input_string, substring, start, end):
    """
    Find the all instances of a substring within a string in a specific range; return the index of the substring.

    :param input_string: a longer string in which you wish to find a substring
    :param substring: the string you wish to find
    :param start: an integer - the first index at which to seek the substring in the input_string
    :param end: an integer - the last index a which to seek the substring in the input_string
    :return: index at which the substring is found in the larger string
    """