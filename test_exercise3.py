#!/usr/bin/env python

""" Assignment 2, Exercise 3, INF1340, Fall, 2015. DBMS

Test module for exercise3.py

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"

from exercise3 import union, intersection, difference


###########
# TABLES ##
###########
GRADUATES = [["Number", "Surname", "Age"],
             [7274, "Robinson", 37],
             [7432, "O'Malley", 39],
             [9824, "Darkes", 38]]

MANAGERS = [["Number", "Surname", "Age"],
            [9297, "O'Malley", 56],
            [7432, "O'Malley", 39],
            [9824, "Darkes", 38]]

STAFF = [["Number", "Surname", "Age"],
            [4444, "Johnson", 44],
            [7432, "O'Malley", 39]]

PETS = [["Name", "Age, Type"],
        ["Mr. Woofs", 4, "Dog"],
        ["Socks", 12, "Cat"]]

LIVESTOCK = [["Name", "Age, Type"],
             ["Wilbur", 5, "Pig"],
             ["Bess", 11, "Cow"],
             ["Socks", 12, "Cat"]]

#####################
# HELPER FUNCTIONS ##
#####################
def is_equal(t1, t2):
    return set(map(tuple, t1)) == set(map(tuple, t2))


###################
# TEST FUNCTIONS ##
###################
def test_union():
    """
    Test union operation.
    """

    result = [["Number", "Surname", "Age"],
              [7274, "Robinson", 37],
              [9297, "O'Malley", 56],
              [7432, "O'Malley", 39],
              [9824, "Darkes", 38]]

    result2 = [["Number", "Surname", "Age"],
               [9297, "O'Malley", 56],
               [7432, "O'Malley", 39],
               [9824, "Darkes", 38],
               [4444, "Johnson", 44]]

    result3 = [["Number", "Surname", "Age"],
               [9297, "O'Malley", 56],
               [7432, "O'Malley", 39],
               [9824, "Darkes", 38]]

    result4 = [["Name", "Age, Type"],
                ["Mr. Woofs", 4, "Dog"],
                ["Socks", 12, "Cat"],
                ["Wilbur", 5, "Pig"],
                ["Bess", 11, "Cow"]]

# Test a regular union with matching schema.
    assert is_equal(result, union(GRADUATES, MANAGERS))

# Test a second regular union with matching schema, in case the first worked by coincidence.
    assert is_equal(result2, union(MANAGERS, STAFF))

# Test a union of a table with itself.
    assert is_equal(result3, union(MANAGERS, MANAGERS))

# Test a union of two completely other tables with matching schema.
    assert is_equal(result4, union(PETS, LIVESTOCK))

# Test a union of non-matching schema
    #try:
       # union(MANAGERS, PETS)
   # except MismatchedAttributesException:
     #   assert True


def test_intersection():
    """
    Test intersection operation.
    """
    result = [["Number", "Surname", "Age"],
              [7432, "O'Malley", 39],
              [9824, "Darkes", 38]]

    assert is_equal(result, intersection(GRADUATES, MANAGERS))

def test_difference():
    """
    Test difference operation.
    """

    result = [["Number", "Surname", "Age"],
              [7274, "Robinson", 37]]

    assert is_equal(result, difference(GRADUATES, MANAGERS))