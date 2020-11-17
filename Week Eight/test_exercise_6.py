'''
Tests for SOF1 Practical 7 Ex 6

@author: djs574@york.ac.uk
'''

import unittest
from recursion import iselfish, something_ish

class Testiselfish(unittest.TestCase):

    def test_empty(self):
        self.assertEqual(False, iselfish(''))

    def test_valid(self):
        self.assertEqual(True, iselfish('elf'))
        self.assertEqual(True, iselfish('whiteleaf'))
        self.assertEqual(True, iselfish('tasteful'))
        self.assertEqual(True, iselfish('unfriendly'))
        self.assertEqual(True, iselfish('wafFles'))

    def test_invalid(self):
        self.assertEqual(False, iselfish('piano'))
        self.assertEqual(False, iselfish('ravioli'))
        self.assertEqual(False, iselfish('elephant'))

class Testsomething_ish(unittest.TestCase):
    
    def test_empty(self):
        self.assertEqual(True, something_ish('',''))
        self.assertEqual(False, something_ish('elf',''))
        self.assertEqual(True, something_ish('','elf'))
    
    def test_valid(self):
        self.assertEqual(True, something_ish('elf', 'elf'))
        self.assertEqual(True, something_ish('elf', 'whiteleaf'))
        self.assertEqual(True, something_ish('elf', 'tasteful'))
        self.assertEqual(True, something_ish('elf', 'unfriendly'))
        self.assertEqual(True, something_ish('elf', 'waffles'))
    
    def test_invalid(self):
        self.assertEqual(False, something_ish('elf', 'piano'))
        self.assertEqual(False, something_ish('elf', 'ravioli'))
        self.assertEqual(False, something_ish('elf', 'elephant'))
    
    def test_duplicated(self):
        # duplicated letters must be present at least that many times
        self.assertEqual(False, something_ish('elff', 'elf'))
        self.assertEqual(True, something_ish('elff', 'elff'))

        self.assertEqual(True, something_ish('elff', 'waffles'))

