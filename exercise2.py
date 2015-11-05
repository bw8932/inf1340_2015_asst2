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

        # If substring found, change found marker to 1 and return the index
        if input_slice == substring:
            found = 1
            return index
        index += 1

    # If function completes loop with found marker in base state, means no match; return -1.
    if found == 0:
        return -1


def multi_find(input_string, substring, start, end):
    """
    Find the all instances of a substring within a string in a specific range; return the indices of the substring.

    :param input_string: a longer string in which to search for a substring
    :param substring: the string to be found
    :param start: an integer - the first index at which to seek the substring in the input_string
    :param end: an integer - the last index a which to seek the substring in the input_string
    :return: all_results: string with all the indices at which the substring is found
    """

    # Create a find_output variable that will stop function from looping when it receives -1 from find function.
    find_output = 0

    # Create an empty result string which will serve as the product of the function.
    result = ""

    # Call find function in a loop, storing the results, until it returns -1 (meaning no more instances to be found.)
    while find_output != -1:
        find_output = find(input_string, substring, start, end)
        result += "," + str(find_output)
        start = find_output + 1

    # Remove the -1 and superfluous commas from result string.
    result = result[1:-3]
    return result