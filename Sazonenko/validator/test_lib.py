from unittest import TestCase
from Sazonenko.validator.lib import *

class Test(TestCase):
    def test_spc_latin_validator(self):
        self.assertTrue(spc_latin_validator("PLATANUS ACERIFOLIA"))
        self.assertFalse(spc_latin_validator("10"))

    def test_wire_htap_validator(self):
        self.assertTrue(wire_htap_validator("yes"))
        self.assertTrue(wire_htap_validator("no"))
        self.assertTrue('fff')

    def test_status_validator(self):
        self.assertFalse(status_validator("aaa"))
        self.assertFalse(status_validator('1'))
        self.assertTrue(status_validator("dead"))
        self.assertTrue(status_validator("good"))

    def test_borocode_validator(self):
        self.assertTrue(borocode_validator('1'))
        self.assertTrue(borocode_validator('8'))
        self.assertFalse(borocode_validator('100'))
        self.assertFalse(borocode_validator('Hello'))


    def test_sort_sentence_alphabetically(self) :  # 15
        self.assertEqual(True, borocode_validator('1'))
        self.assertEqual(False, borocode_validator('London is the capital'))
