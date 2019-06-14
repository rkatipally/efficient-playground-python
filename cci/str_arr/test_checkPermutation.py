from unittest import TestCase
from cci.str_arr.check_permutation import CheckPermutation


class TestCheckPermutation(TestCase):
    def test_check_permutation_success(self):
        self.assertTrue(CheckPermutation.check_permutation_by_sort('abcd', 'acbd'))
        self.assertTrue(CheckPermutation.check_permutation_by_sort('abacd', 'aacbd'))
        self.assertTrue(CheckPermutation.check_permutation_by_sort('abcddac', 'aacdbcd'))

    def test_check_permutation_failure(self):
        self.assertFalse(CheckPermutation.check_permutation_by_sort('abcd', 'acbda'))
        self.assertFalse(CheckPermutation.check_permutation_by_sort('abacd', 'aaccd'))
        self.assertFalse(CheckPermutation.check_permutation_by_sort('abcddac', 'aac'))

    def test_check_permutation_by_hash(self):
        self.assertTrue(CheckPermutation.check_permutation_by_hash('abcd', 'acbd'))
        self.assertTrue(CheckPermutation.check_permutation_by_hash('abacd', 'aacbd'))
        self.assertTrue(CheckPermutation.check_permutation_by_hash('abcddac', 'aacdbcd'))

    def test_check_permutation_by_hash_failure(self):
        self.assertFalse(CheckPermutation.check_permutation_by_hash('abcd', 'acbda'))
        self.assertFalse(CheckPermutation.check_permutation_by_hash('abacd', 'aaccd'))
        self.assertFalse(CheckPermutation.check_permutation_by_hash('abcddac', 'aac'))
