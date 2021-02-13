#!/usr/bin/python
# -*- coding: utf-8 -*-
##########################################################################################
# author: Nikolas Schnellbaecher
# contact: khx0@posteo.net
# date: 2021-01-23
# file: test_filter_sequential_duplicates.py
# tested with python 3.7.6 and numpy 1.20.1
##########################################################################################

'''
--- Example invocations ---
Cd to the directory containing this script and there invoke
$python -m pytest (-v)
where python is your chosen python interpreter or alternatively only call
$pytest
or
$pytest -v
using the default python interpreter on your system.
The -v flag (equal to --verbose) sets the pytest mode to 'verbose'.
-------------------------------------------------------------------------------
To only run the tests in this test file use
$python -m pytest (-v) test_*.py
where test_*.py is the considered unit test script.
-------------------------------------------------------------------------------
plain unittest invocation
$python test_*.py
-------------------------------------------------------------------------------
Tested with pytest version 6.2.2.
'''

import platform
import unittest
import numpy as np

from filter_sequential_duplicates import get_multiplicity

class FilterSequentialDuplicatesTest(unittest.TestCase):

    def test_01(self):
        """
        test the get_multiplicity function
        """

        X = np.array([1, 1, 2, 3, 4, 5])
        reference = [(0, 2)]
        multiplicity = get_multiplicity(X)
        # print(multiplicity)
        self.assertTrue(multiplicity == reference)

        X = np.array([1, 2, 2, 3, 4, 5])
        reference = [(1, 2)]
        multiplicity = get_multiplicity(X)
        # print(multiplicity)
        self.assertTrue(multiplicity == reference)

        X = np.array([1, 2, 3, 4, 5, 5])
        reference = [(4, 2)]
        multiplicity = get_multiplicity(X)
        # print(multiplicity)
        self.assertTrue(multiplicity == reference)

        X = np.array([1, 1, 2, 2, 3, 4, 5])
        reference = [(0, 2), (2, 2)]
        multiplicity = get_multiplicity(X)
        # print(multiplicity)
        self.assertTrue(multiplicity == reference)

        X = np.array([])
        reference = []
        multiplicity = get_multiplicity(X)
        # print(multiplicity)
        self.assertTrue(multiplicity == reference)

        X = np.array([3])
        reference = []
        multiplicity = get_multiplicity(X)
        # print(multiplicity)
        self.assertTrue(multiplicity == reference)

        X = np.array([1, 1, 1, 2, 2, 2, 3, 1, 4, 5, 5, 1, 2, 2, 2])
        reference = [(0, 3), (3, 3), (9, 2), (12, 3)]
        multiplicity = get_multiplicity(X)
        # print(multiplicity)
        self.assertTrue(multiplicity == reference)

        X = np.array([2, 2, 4, 4, 4, 4, 4])
        reference = [(0, 2), (2, 5)]
        multiplicity = get_multiplicity(X)
        # print(multiplicity)
        self.assertTrue(multiplicity == reference)

        X = np.array([90, 100, 4, 4, 4, 1])
        reference = [(2, 3)]
        multiplicity = get_multiplicity(X)
        # print(multiplicity)
        self.assertTrue(multiplicity == reference)

        return None

if __name__ == '__main__':

    print("/////////////////////////////////////////////////////////////////////////////")
    print("Running", __file__)
    print("/////////////////////////////////////////////////////////////////////////////")
    print("Python Interpreter Version =", platform.python_version())
    print("/////////////////////////////////////////////////////////////////////////////")
    print("Start testing ...")
    print("/////////////////////////////////////////////////////////////////////////////")

    unittest.main()
