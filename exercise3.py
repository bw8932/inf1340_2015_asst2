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
    class MismatchedAttributesException(AttributeError):
        """Raise when schema of tables t1 and t2 don't have the same attributes"""

# for matching schema
    if table1[0] == table2[0]:
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
        return [table3]
# for schema that don't match
    else:
        raise AttributeError

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
    class MismatchedAttributesException(AttributeError):
        """Raise when schema of tables t1 and t2 don't have the same attributes"""

# for matching schema
    if table1[0] == table2[0]:
# create deep copy of table1
        table3 = []
# add entries from table1 one at a time to select only duplicates
        for index in range(len(table1)):
            if table1[index] in table2:
                table3.append(table1[index])
            else:
                print index, "is not duplicate"
        print table3
        return [table3]
# for schema that don't match
    else:
        raise AttributeError
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
    class MismatchedAttributesException(AttributeError):
        """Raise when schema of tables t1 and t2 don't have the same attributes"""

# for matching schema
    if table1[0] == table2[0]:
# create deep copy of table1
#add schema to new table
        table3 = []
        table3.append(table1[0])
# add entries from table1 one at a time to select only duplicates
        for index in range(len(table1)):
            if table1[index] not in table2:
                table3.append(table1[index])
            else:
                print index, "is in both"
        print table3
        return [table3]
# for schema that don't match
    else:
        raise AttributeError
#difference(GRADUATES, MANAGERS)




#Here is a second version of union, using the helper function she included
#but I can't figure out how to get the others to use it, so there doesn't seem to be any point in using here
def union_with_helper(table1, table2):
    table3 = []
    table3 += (table1 + table2)
    table3 = remove_duplicates(table3)
    print " "
    print table3
    return table3
#union_with_helper(GRADUATES, MANAGERS)

