from unittest import TestCase
from cci.str_arr.unique_str import UniqueStr


class TestUniqueStr(TestCase):
    def test_is_unique(self):
        self.assertTrue(UniqueStr.is_unique('abc'))
        self.assertTrue(UniqueStr.is_unique('abc'))
        self.assertFalse(UniqueStr.is_unique('abca'))
