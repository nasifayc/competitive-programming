class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        i,j,s,count = 0,0,0, 0

        while j < len(arr):
            s += arr[j]
            if j - i + 1 == k:
                if s // k >= threshold:
                    count += 1
                s -= arr[i]
                i += 1
            j += 1
        return count


