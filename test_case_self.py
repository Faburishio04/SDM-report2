#!/usr/bin/python3

import unittest
from calc_mul import calc

# Run with testrunner so needs to be in file test_

class TestCalc (unittest.TestCase):

        def test_boundary_valid_min(self):
            self.assertEqual(1, calc(1, 1))

        def test_zero_a(self):
            self.assertEqual(-1, calc(0, 5))

        def test_zero_b(self):
            self.assertEqual(-1, calc(5, 0))

        def test_negative_values(self):
            self.assertEqual(-1, calc(-3, 5))

        def test_float_values(self):
            self.assertEqual(-1, calc(1.5, 2))

        def test_lower_boundary_over1(self):
            self.assertEqual(-1, calc(1, -1))

        def test_lower_boundary_over2(self):
            self.assertEqual(-1, calc(1, 0))

        def test_lower_boundary(self):
            self.assertEqual(1, calc(1, 1))
        
        def test_upper_boundary_just_before(self):
            self.assertEqual(998, calc(1, 998))

        def test_upper_boundary(self):
            self.assertEqual(-1, calc(1, 999))

        def test_upper_boundary_over(self):
            self.assertEqual(-1, calc(1, 1000))

