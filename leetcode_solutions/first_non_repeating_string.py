class Solution:
    def first_non_repeating_char(s: str) -> int:
        char_count = {}
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1

        for index, char in enumerate(s):
            if char_count[char] == 1:
                return index

        
        return -1


                

        