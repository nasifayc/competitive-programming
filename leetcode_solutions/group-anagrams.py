from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashTable = {}
        for s in strs:
            sorted_characters = sorted(s)
            sorted_string = ''.join(sorted_characters)
            if not  sorted_string in hashTable:
                hashTable[sorted_string] = [s]
            else:
                hashTable[sorted_string].append(s)
        return list(hashTable.values())
