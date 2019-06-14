class UniqueStr():
    @staticmethod
    def is_unique(str):
        if len(str) > 128:
            return False

        char_flags = [False]*128
        for c in str:
            val = ord(c)
            if char_flags[val]:
                return False
            char_flags[val] = True
        return True
