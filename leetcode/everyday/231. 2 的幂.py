class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n==0:return False
        base = 2
        n_tmp = n
        while n_tmp%2 == 0:
            if n_tmp%base==0:
                n_tmp = int(n_tmp / base)
                base = base * 2
            else:
                base = int(base / 2)
        return n_tmp == 1



        
s = Solution()
print(s.isPowerOfTwo(3))