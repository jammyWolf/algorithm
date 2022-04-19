class Solution:
    def reverseString(self, s) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s) - 1
        while left<=right:
            tmp_s = s[left]
            s[left] = s[right]
            s[right] = tmp_s
            left += 1 
            right -= 1
        print(s)

s = Solution()
print(s.reverseString(["h","e","l","l","o"]))