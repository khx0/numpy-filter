#!/usr/bin/python
# -*- coding: utf-8 -*-
##########################################################################################
# author: Nikolas Schnellbaecher
# contact: khx0@posteo.net
# date: 2021-01-23
# file: test_slicer.py
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

from slicer import isMonotonicallyIncreasing
from slicer import isStrictlyMonotonicallyIncreasing
from slicer import isMonotonicallyDecreasing
from slicer import isStrictlyMonotonicallyDecreasing
from slicer import getMonotonicSubIntervals

class SlicerTest(unittest.TestCase):

    """
    Test cases for the getMonotonicSubIntervals function.
    GT = ground truth
    """
    '''
    def test_01(self):

        X = [1.0, 2.0, 3.0, 4.0, 3.0, 2.0, 1.0]
        intervalsGT = [[1.0, 2.0, 3.0, 4.0], [4.0, 3.0, 2.0, 1.0]]
        indexListGT = [(0, 3), (3, 6)]

        intervals, indexList = getMonotonicSubIntervals(X)

        self.assertTrue(np.array_equal(intervals, intervalsGT))
        self.assertTrue(np.array_equal(indexList, indexListGT))

    def test_02(self):

        X = [1.1, 1.1]
        intervalsGT = [[1.1, 1.1]]
        indexListGT = [(0, 1)]

        intervals, indexList = getMonotonicSubIntervals(X)

        self.assertTrue(np.array_equal(intervals, intervalsGT))
        self.assertTrue(np.array_equal(indexList, indexListGT))

    def test_03(self):

        X = [1.1, 1.0]
        intervalsGT = [[1.1, 1.0]]
        indexListGT = [(0, 1)]

        intervals, indexList = getMonotonicSubIntervals(X)

        self.assertTrue(np.array_equal(intervals, intervalsGT))
        self.assertTrue(np.array_equal(indexList, indexListGT))

    def test_04(self):

        X = [1.0, 1.1]
        intervalsGT = [[1.0, 1.1]]
        indexListGT = [(0, 1)]

        intervals, indexList = getMonotonicSubIntervals(X)

        self.assertTrue(np.array_equal(intervals, intervalsGT))
        self.assertTrue(np.array_equal(indexList, indexListGT))

    def test_05(self):

        X = [1.0, 2.0, 3.0, 4.0, 5.0]
        intervalsGT = [[1.0, 2.0, 3.0, 4.0, 5.0]]
        indexListGT = [(0, 4)]

        intervals, indexList = getMonotonicSubIntervals(X)

        self.assertTrue(np.array_equal(intervals, intervalsGT))
        self.assertTrue(np.array_equal(indexList, indexListGT))

    def test_06(self):

        X = [5.0, 4.0, 3.0, 2.0, 1.0]
        intervalsGT = [[5.0, 4.0, 3.0, 2.0, 1.0]]
        indexListGT = [(0, 4)]

        intervals, indexList = getMonotonicSubIntervals(X)

        self.assertTrue(np.array_equal(intervals, intervalsGT))
        self.assertTrue(np.array_equal(indexList, indexListGT))

    def test_07(self):

        X = [5.0, 4.0, 3.0, 3.0, 1.0]
        intervalsGT = [[5.0, 4.0, 3.0, 3.0, 1.0]]
        indexListGT = [(0, 4)]

        intervals, indexList = getMonotonicSubIntervals(X)

        self.assertTrue(np.array_equal(intervals, intervalsGT))
        self.assertTrue(np.array_equal(indexList, indexListGT))

    def test_08(self):

        X = [1.0, 2.0, 2.0, 3.0, 4.0]
        intervalsGT = [[1.0, 2.0, 2.0, 3.0, 4.0]]
        indexListGT = [(0, 4)]

        intervals, indexList = getMonotonicSubIntervals(X)

        self.assertTrue(np.array_equal(intervals, intervalsGT))
        self.assertTrue(np.array_equal(indexList, indexListGT))

    def test_09(self):

        X = [1.0, 1.0, 1.0, 1.0, 1.0]
        intervalsGT = [[1.0, 1.0, 1.0, 1.0, 1.0]]
        indexListGT = [(0, 4)]

        intervals, indexList = getMonotonicSubIntervals(X)

        self.assertTrue(np.array_equal(intervals, intervalsGT))
        self.assertTrue(np.array_equal(indexList, indexListGT))

    def test_10(self):

        X = [1.0, 1.0, 1.0, 1.0, 5.0]
        intervalsGT = [[1.0, 1.0, 1.0, 1.0, 5.0]]
        indexListGT = [(0, 4)]

        intervals, indexList = getMonotonicSubIntervals(X)

        self.assertTrue(np.array_equal(intervals, intervalsGT))
        self.assertTrue(np.array_equal(indexList, indexListGT))

    def test_11(self):

        X = [1.0, 1.0, 1.0, 1.0, 0.0]
        intervalsGT = [[1.0, 1.0, 1.0, 1.0, 0.0]]
        indexListGT = [(0, 4)]

        intervals, indexList = getMonotonicSubIntervals(X)

        self.assertTrue(np.array_equal(intervals, intervalsGT))
        self.assertTrue(np.array_equal(indexList, indexListGT))
    '''
    def test_12(self):

        X = [1.0, 1.0, 0.0, 1.0]
        intervalsGT = [[1.0, 1.0,  0.0], [0.0, 1.0]]
        indexListGT = [(0, 2), (2, 3)]

        intervals, indexList = getMonotonicSubIntervals(X)

        self.assertTrue(intervals == intervalsGT)
        self.assertTrue(indexList == indexListGT)

    def test_13(self):

        X = [1.0, 1.0, 1.0, 1.0, 2.0, 2.0, 0.0]
        intervalsGT = [[1.0, 1.0, 1.0, 1.0, 2.0, 2.0,], [2.0, 0.0]]
        indexListGT = [(0, 5), (5, 6)]

        intervals, indexList = getMonotonicSubIntervals(X)

        self.assertTrue(intervals == intervalsGT)
        self.assertTrue(indexList == indexListGT)

    def test_14(self):

        X = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        intervalsGT = [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]]
        indexListGT = [(0, 6)]

        intervals, indexList = getMonotonicSubIntervals(X)

        self.assertTrue(intervals == intervalsGT)
        self.assertTrue(indexList == indexListGT)

    def test_15(self):

        X = [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        intervalsGT = [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]]
        indexListGT = [(0, 6)]

        intervals, indexList = getMonotonicSubIntervals(X)

        self.assertTrue(intervals == intervalsGT)
        self.assertTrue(indexList == indexListGT)

    def test_16(self):

        X = [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]
        intervalsGT = [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0]]
        indexListGT = [(0, 5), (5, 6)]

        intervals, indexList = getMonotonicSubIntervals(X)

        self.assertTrue(intervals == intervalsGT)
        self.assertTrue(indexList == indexListGT)


    def test_isMonotonicallyIncreasing(self):

        X = np.array([0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])
        self.assertTrue(isMonotonicallyIncreasing(X))

        X = np.linspace(0.0, 100.0, 100)
        self.assertTrue(isMonotonicallyIncreasing(X))

        X = np.zeros((100))
        self.assertTrue(isMonotonicallyIncreasing(X))

        X = np.ones((100))
        self.assertTrue(isMonotonicallyIncreasing(X))

        X = np.array([0.0, -1.0, -2.0, -3.0])
        self.assertFalse(isMonotonicallyIncreasing(X))

    def test_isStrictlyMonotonicallyIncreasing(self):

        X = np.array([0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])
        self.assertTrue(isStrictlyMonotonicallyIncreasing(X))

        X = np.linspace(0.0, 100.0, 100)
        self.assertTrue(isStrictlyMonotonicallyIncreasing(X))

        X = np.zeros((100))
        self.assertFalse(isStrictlyMonotonicallyIncreasing(X))

        X = np.ones((100))
        self.assertFalse(isStrictlyMonotonicallyIncreasing(X))

        X = np.array([0.0, -1.0, -2.0, -3.0])
        self.assertFalse(isStrictlyMonotonicallyIncreasing(X))

    def test_isMonotonicallyDecreasing(self):

        X = np.array([0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])
        self.assertFalse(isMonotonicallyDecreasing(X))

        X = np.flip(X, axis = 0)
        self.assertTrue(isMonotonicallyDecreasing(X))

        X = np.linspace(0.0, 100.0, 100)
        self.assertFalse(isMonotonicallyDecreasing(X))

        X = np.flip(X, axis = 0)
        self.assertTrue(isMonotonicallyDecreasing(X))

        X = np.zeros((100))
        self.assertTrue(isMonotonicallyDecreasing(X))

        X = np.ones((100))
        self.assertTrue(isMonotonicallyDecreasing(X))

        X = np.array([0.0, -1.0, -2.0, -3.0])
        self.assertTrue(isMonotonicallyDecreasing(X))

    def test_isStrictlyMonotonicallyDecreasing(self):

        X = np.array([0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])
        self.assertFalse(isStrictlyMonotonicallyDecreasing(X))

        X = np.flip(X, axis = 0)
        self.assertTrue(isStrictlyMonotonicallyDecreasing(X))

        X = np.linspace(0.0, 100.0, 100)
        self.assertFalse(isStrictlyMonotonicallyDecreasing(X))

        X = np.flip(X, axis = 0)
        self.assertTrue(isStrictlyMonotonicallyDecreasing(X))

        X = np.zeros((100))
        self.assertFalse(isStrictlyMonotonicallyDecreasing(X))

        X = np.ones((100))
        self.assertFalse(isStrictlyMonotonicallyDecreasing(X))

        X = np.array([0.0, -1.0, -2.0, -3.0])
        self.assertTrue(isStrictlyMonotonicallyDecreasing(X))

if __name__ == '__main__':

    print("/////////////////////////////////////////////////////////////////////////////")
    print("Running", __file__)
    print("/////////////////////////////////////////////////////////////////////////////")
    print("Python Interpreter Version =", platform.python_version())
    print("/////////////////////////////////////////////////////////////////////////////")
    print("Start testing ...")
    print("/////////////////////////////////////////////////////////////////////////////")

    unittest.main()
