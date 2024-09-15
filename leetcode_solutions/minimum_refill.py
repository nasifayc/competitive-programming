from typing import List


class Solution:
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        result = 0
        i, j = 0, len(plants) - 1
        a, b = capacityA, capacityB

        while i <= j:
            if i == j:  
                if max(a, b) < plants[i]:
                    result += 1
                break

            if plants[i] > a:  
                result += 1
                a = capacityA  
            a -= plants[i]  
            i += 1

            if plants[j] > b:  
                result += 1
                b = capacityB  
            b -= plants[j]  
            j -= 1

        return result
