class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m==0:
            for i in range(len(nums1)):
                nums1[i] = nums2[i]
        elif n==0:
            nums1 = nums1
        else:
            i, j, pvt = nums1.index(max(nums1[:m])), nums2.index(max(nums2)), len(nums1)-1
            while i<m-1 and nums1[i]==nums1[i+1]:
                i+=1
            while j<n-1 and nums2[j]==nums2[j+1]:
                j+=1
            while i>=0 and j>=0:
                if nums1[i]>nums2[j]:
                    nums1[pvt] = nums1[i]
                    i -= 1
                else:
                    nums1[pvt] = nums2[j]
                    j -= 1
                pvt -= 1
            while j>=0 and pvt>=0:
                nums1[pvt] = nums2[j]
                j -= 1
                pvt -= 1
        print(nums1)

def main():
    s = Solution()
    nums1=[-12,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    nums2=[-49,-45,-42,-41,-40,-39,-39,-39,-38,-36,-34,-34,-33,-33,-32,-31,-29,-28,-26,-26,-24,-21,-20,-20,-18,-16,-16,-14,-11,-7,-6,-5,-4,-4,-3,-3,-2,-2,-1,0,0,0,2,2,6,7,7,8,10,10,13,13,15,15,16,17,17,19,19,20,20,20,21,21,22,22,24,24,25,26,27,29,30,30,30,35,36,36,36,37,39,40,41,42,45,46,46,46,47,48]
    s.merge(nums1, 1, nums2, 90)

if __name__=="__main__":
    main()