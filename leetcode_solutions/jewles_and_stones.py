class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0
        for i in range(len(jewels)):
            for j in range(len(stones)):
                if(ord(jewels[i]) == ord(stones[j])):
                    count += 1
        return count
