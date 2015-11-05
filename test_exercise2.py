#!/usr/bin/env python

""" Assignment 2, Exercise 2, INF1340, Fall, 2015. DNA Sequencing

Test module for exercise2.py

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"

from exercise2 import find, multi_find


def test_find_basic():
    """
    Test find function.
    """
    assert find("This is an ex-parrot", "parrot", 0, 20) == 14


def test_find_additional():
    """
    Test find function with a variety of arguments.
    """
    # Test with numbers.
    assert find("0123456789", "89", 0, 10) == 8

    # Test with letters.
    assert find("EGG", "G", 0, 3) == 1

    # Test with string having multiple instances of substring.
    assert find("DuckDuckDuckGoose", "Duck", 0, 16) == 0

    # Test with string having no instances of substring.
    assert find("Joe", "Z", 0, 2) == -1

    # Test with string having instances of substring outside of passed index range.
    assert find("012345", "5", 0, 4) == -1

    # Test with index beyond the length of the string.
    assert find("012345", "5", 0, 44) == 5


def test_multi_find_basic():
    """
    Test multi_find function.
    """
    assert multi_find("Ni! Ni! Ni! Ni!", "Ni", 0, 20) == "0,4,8,12"


def test_multi_find_additional():
    """
    Test multi_find function with a variety of arguments.
    """
    # Test with numbers.
    assert multi_find("012345678989", "89", 0, 12) == "8,10"

    # Test with letters.
    assert multi_find("Jennifer", "n", 0, 7) == "2,3"

    # Test with string having multiple instances of substring.
    assert multi_find("DuckDuckDuckGoose", "Duck", 0, 16) == "0,4,8"

    # Test with string having no instances of substring.
    assert multi_find("Joe", "Z", 0, 2) == ""

    # Test with string having instances of substring outside of passed index range.
    assert multi_find("012345555555", "5", 0, 4) == ""

    # Test with index beyond the length of the string.
    assert multi_find("01234555", "5", 0, 44) == "5,6,7"
