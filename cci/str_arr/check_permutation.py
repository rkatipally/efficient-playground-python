class CheckPermutation:
    @staticmethod
    def check_permutation_by_sort(str1, str2):
        if len(str1) != len(str2):
            return False
        str1 = sorted(str1)
        str2 = sorted(str2)
        return str1 == str2

    @staticmethod
    def check_permutation_by_hash(str1, str2):
        if len(str1) != len(str2):
            return False
        char_map = {}
        for c in str1:
            if char_map.get(c):
                char_map[c] = char_map[c] + 1
            else:
                char_map[c] = 1
        for c in str2:
            char_map[c] = char_map[c] - 1
            if char_map[c] < 0:
                return False
        return True

