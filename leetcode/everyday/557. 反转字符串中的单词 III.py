class Solution:
    def reverseWords(self, s: str) -> str:
        new_s = " ".join([t[::-1] for t in s.split(" ")])
        return new_s


        
s = Solution()
print(s.reverseWords("Let's take LeetCode contest"))