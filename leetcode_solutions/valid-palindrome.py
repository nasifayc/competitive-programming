import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_phrase = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        i,j = 0, len(cleaned_phrase)-1

        while i < j:
            if cleaned_phrase[i] != cleaned_phrase[j]:
                return False
            i += 1
            j -= 1
        return True
