class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        def maxConsecutiveChar(char: str) -> int:
            l, r, flips, max_length = 0, 0, 0, 0
            n = len(answerKey)

            while r < n:
                if answerKey[r] != char:
                    flips += 1
                while flips > k:
                    if answerKey[l] != char:
                        flips -= 1
                    l += 1

                max_length = max(max_length, r - l + 1)
                r += 1

            return max_length

        return max(maxConsecutiveChar('T'), maxConsecutiveChar('F'))

