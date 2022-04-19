def sortColors(nums) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    left, right = 0, len(nums) - 1
    i = 0
    while(i<len(nums)):
        while nums[i] == 2 and i<right:
            nums[i], nums[right] = nums[right], nums[i]
            right -= 1

        if nums[i]==0:
            nums[i], nums[left] = nums[left], nums[i]
            left += 1
        i += 1
        
    print(nums)

a = [2,0,2,1,1,0]
# a = [2,0,1]
# a = [1,0,2]
a = [0,0,1,0,1,1]
# a = [1,2,1]

sortColors(a)
    