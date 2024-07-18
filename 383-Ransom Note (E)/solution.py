class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        char_dict = {}
        mag_dict = {}

        for char in magazine:
            num_chars = char_dict.get(char, None)

            if not num_chars:
                char_dict[char] = 1
            else:
                char_dict[char] = num_chars + 1

        for each in ransomNote:
            num_chars = mag_dict.get(each, None)

            if not num_chars:
                mag_dict[each] = 1
            else:
                mag_dict[each] = num_chars + 1

        for ransom_char, occurences in mag_dict.items():
            
            num_matches = char_dict.get(ransom_char, None)

            if not num_matches:
                return False
            elif num_matches < occurences:
                return False
            else:
                continue

        return True