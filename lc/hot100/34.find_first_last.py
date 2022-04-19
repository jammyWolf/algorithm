def searchRange(nums, target):
    def search(nums, left, right):
        if not nums or target<nums[left] or target>nums[right]: 
            return [-1, -1]
        
        if nums[left] == target:
            return left

        if nums[right] == target:
            return right


        while left<right:
        
    

    ret = list()

    return ret

li = [[5,7,7,8,8,10],[5,7,7,8,8,10], []]
target = [8, 6, 0]
for num, tar in zip(li, target):
    ret = searchRange(num, tar)
    print(ret)