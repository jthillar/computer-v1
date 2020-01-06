#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest

from computer import computer

class MyTestCase(unittest.TestCase):

    def testComputerPol2(self):
        equation = "6 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0"
        result = computer(equation)
        self.assertEqual(result['degree'], 2)
        self.assertEqual(result['discriminant'] > 0, True)
        self.assertEqual(result['solution'], True)

    def testComputerPol2_2(self):
        equation = "7 * X^0 + 13 * X^1 + 3 * X^2 = 1 * X^0 + 1 * X^1"
        result = computer(equation)
        self.assertEqual(result['degree'], 2)
        self.assertEqual(result['discriminant'] > 0, True)
        self.assertEqual(result['solution'], True)

    def testComputerPol2DiscriminantNull(self):
        equation = "6 * X^0 + 11 * X^1 + 5 * X^2 = 1 * X^0 + X"
        result = computer(equation)
        self.assertEqual(result['degree'], 2)
        self.assertEqual(result['discriminant'] == 0, True)
        self.assertEqual(result['solution'], True)
        self.assertEqual(result['solution2'], None)

    def testComputerPol2DiscriminantNegative(self):
        equation = "5 * X^0 + 3 * X^1 + 3 * X^2 = 1 * X^0 + 0 * X^1"
        result = computer(equation)
        self.assertEqual(result['degree'], 2)
        self.assertEqual(result['discriminant'] < 0, True)
        self.assertEqual(result['solution'], True)

    def testComputerPol2DiscriminantNegative2(self):
        equation = "4 * X^0 + 3 * X^1 + X^2 = 0"
        result = computer(equation)
        self.assertEqual(result['degree'], 2)
        self.assertEqual(result['discriminant'] < 0, True)
        self.assertEqual(result['solution'], True)

    def testComputerPol1(self):

        equation = "5 * X^0 + 4 * X^1 - 0 * X^2 = 1 * X^0"
        result = computer(equation)
        self.assertEqual(result['degree'], 1)
        self.assertEqual(result['solution'], True)

    def testComputerPol1_2(self):

        equation = "5 * X^0 + 4 + 7 * X^1 + 8 * X = 0"
        result = computer(equation)
        self.assertEqual(result['degree'], 1)
        self.assertEqual(result['solution'], True)

    def testComputerPol0(self):

        equation = "5 * X^2 = 5 * X^2"
        result = computer(equation)
        self.assertEqual(result['solution'], None)

    def testComputerPolNoSolution(self):

        equation = "5 * X^0 = 8 * X^0"
        result = computer(equation)
        self.assertEqual(result['solution'], False)

    def testComputerPolToHigh(self):

        equation = "6 * X^0 + 4 * X^18 - 9.3 * X^3 = 1 * X^0"
        result = computer(equation)
        self.assertEqual(result['solution'], False)

    def testComputerErrorNegative(self):
        equation = "6 * X^0 + -4 * X^2 = 1 * X^0"
        with self.assertRaises(SystemExit) as cm:
            computer(equation)
        self.assertEqual(cm.exception.code, 1)

    def testComputerErrorConstruction(self):
        equation = "5X^0 + 4X^1 - 0 * X^2 = 1 * X^0"
        with self.assertRaises(SystemExit) as cm:
            computer(equation)
        self.assertEqual(cm.exception.code, 1)

    def testComputerErrorCaracters(self):
        equation = "5glezjjngv = 1 * X^0"
        with self.assertRaises(SystemExit) as cm:
            computer(equation)
        self.assertEqual(cm.exception.code, 1)

    def testComputerErrorEquality(self):
        equation = "5 * X = 1 * X^0 = 3 * X"
        with self.assertRaises(SystemExit) as cm:
            computer(equation)
        self.assertEqual(cm.exception.code, 1)

        equation = "5 * X + 3 * X"
        with self.assertRaises(SystemExit) as cm:
            computer(equation)
        self.assertEqual(cm.exception.code, 1)

    def testComputerErrorNotEntire(self):

        equation = "6 * X^0 + 4.2 * X^2 = 1 * X^0"
        result = computer(equation)

    def testComputerNullCoeff(self):

        equation = "6 * X^0 + 0 * X^2 = 1 * X^0"
        result = computer(equation)
        self.assertEqual(result['solution'], False)

if __name__ == '__main__':
    unittest.main()
