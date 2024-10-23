class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        h = set()
        i,j,l = 0,0,0
        while j < len(s):
            if s[j] in h:
                h.remove(s[i])
                i += 1
            else:
                h.add(s[j])
                l = max(l, j - i + 1)
                j += 1 
        return l