#!/usr/bin/env python

import unittest
import add

class SampleClassTest(unittest.TestCase):

    CLS_VAL = 'none'

    def setUp(self):
        self.smpl = add.SampleClass()

    def test_default(self):
        expected = 0
        actual = self.smpl.get()
        self.assertEqual(expected, actual)

    def test_add(self):
        expected = 1
        self.smpl.add()
        actual = self.smpl.get()
        self.assertEqual(expected, actual)

