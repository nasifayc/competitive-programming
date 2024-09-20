

from typing import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""
        
        
        target_map = Counter(t)
        required = len(target_map)  
        
        
        left, right = 0, 0
        formed = 0  
        window_counts = {}  
        min_length = float("inf")  
        min_window = (0, 0)  
        
        while right < len(s):
            
            char = s[right]
            window_counts[char] = window_counts.get(char, 0) + 1
            
            
            if char in target_map and window_counts[char] == target_map[char]:
                formed += 1
            
            
            while left <= right and formed == required:
                char = s[left]
                
                
                if right - left + 1 < min_length:
                    min_length = right - left + 1
                    min_window = (left, right)
                
                
                window_counts[char] -= 1
                if char in target_map and window_counts[char] < target_map[char]:
                    formed -= 1
                left += 1
            
            
            right += 1
        
        
        start, end = min_window
        return s[start:end+1] if min_length != float("inf") else ""
