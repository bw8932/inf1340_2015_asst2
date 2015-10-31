#!/usr/bin/env python

""" Assignment 2, Exercise 3, INF1340, Fall, 2015. DBMS
This module performs table operations on database tables
implemented as lists of lists.
"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"


GRADUATES = [["Number", "Surname", "Age"], [7274, "Robinson", 37], [7432, "O'Malley", 39], [9824, "Darkes", 38]]

MANAGERS = [["Number", "Surname", "Age"], [9297, "O'Malley", 56], [7432, "O'Malley", 39], [9824, "Darkes", 38], [3, "ekj", 5]]


def union(table1, table2):
    """
    Perform the union set operation on tables, table1 and table2.

    :param table1: a table (a List of Lists)
    :param table2: a table (a List of Lists)
    :return: the resulting table
    :raises: MismatchedAttributesException:
        if tables t1 and t2 don't have the same attributes
    """

# for matching schema
    if table1[0] == table2[0]:
        print "tables match"

# create deep copy of table1
        table3 = []
        table3 += table1
# add entries from table2 one at a time to avoid duplicates
        for index in range(len(table2)):
            if table2[index] not in table3:
                table3.append(table2[index])
            else:
                print index, "is duplicate"
        print table3
# for schema that don't match
    else:
        print "mismatch"
    return [table3]

union(GRADUATES, MANAGERS)





def intersection(table1, table2):
    return [table3]



def difference(table1, table2):
    return [table3]



def trash_attempt(table1, table2):
    trytable = []
    trytable += (table1 + table2)
    clean_table = remove_duplicates(trytable)
    print " "
    print clean_table
    return clean_table


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