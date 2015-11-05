#!/usr/bin/env python

""" Assignment 2, Exercise 3, INF1340, Fall, 2015. DBMS
This module performs table operations on database tables
implemented as lists of lists.
"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"

#REMOVE THESE BEFORE SUBMITTING, ALONG WITH THE COMMENTED OUT FUNCTION CALLS
GRADUATES = [["Number", "Surname", "Age"], [7274, "Robinson", 37], [7432, "O'Malley", 39], [9824, "Darkes", 38]]

MANAGERS = [["Number", "Surname", "Age"], [9297, "O'Malley", 56], [7432, "O'Malley", 39], [9824, "Darkes", 38], [3, "ekj", 5]]


#####################
# HELPER FUNCTIONS ##
#####################
def remove_duplicates(l):
    """
    Removes duplicates from l, where l is a List of Lists.
    :param l: a List
    """

    d = {}
    result = []
    for row in l:
        if tuple(row) not in d:
            result.append(row)
            d[tuple(row)] = True

    return result


class MismatchedAttributesException(Exception):
    """
    Raised when attempting set operations with tables that
    don't have the same attributes.
    """
    pass


def union(table1, table2):
    """
    Perform the union set operation on tables, table1 and table2.

    :param table1: a table (a List of Lists)
    :param table2: a table (a List of Lists)
    :return: the resulting table
    :raises: MismatchedAttributesException:
        if tables t1 and t2 don't have the same attributes
    """

    # If the schema match, combine the tables and remove duplicates using helper function.
    if table1[0] == table2[0]:
        table3 = (table1 + table2)
        table3 = remove_duplicates(table3)
        return table3

    # If the schema don't match, raise error.
    else:
        raise MismatchedAttributesException
#union(GRADUATES, MANAGERS)


def intersection(table1, table2):
    """
    Perform the intersection set operation on tables, table1 and table2.

    :param table1: a table (a List of Lists)
    :param table2: a table (a List of Lists)
    :return: the resulting table
    :raises: MismatchedAttributesException:
        if tables t1 and t2 don't have the same attributes
    """

    # Check if tables' schema match.
    if table1[0] == table2[0]:
        # Create empty table3, then add entries one at a time to select only duplicates (including the schema itself).
        table3 = []
        for index in range(len(table1)):
            if table1[index] in table2:
                table3.append(table1[index])
        return table3
    # For schema that don't match, raise error.
    else:
        raise MismatchedAttributesException

#intersection(GRADUATES, MANAGERS)


def difference(table1, table2):
    """
    Perform the difference set operation on tables, table1 and table2.

    :param table1: a table (a List of Lists)
    :param table2: a table (a List of Lists)
    :return: the resulting table
    :raises: MismatchedAttributesException:
        if tables t1 and t2 don't have the same attributes
    """

    # Check if tables' schema match.
    if table1[0] == table2[0]:

        # Create empty table3, then add schema headers to it, then add entries occurring in only table1.
        table3 = []
        table3.append(table1[0])
        for index in range(len(table1)):
            if table1[index] not in table2:
                table3.append(table1[index])
        print table3
        return table3

    # For schema that don't match, raise error.
    else:
        raise MismatchedAttributesException

#difference(GRADUATES, MANAGERS)





