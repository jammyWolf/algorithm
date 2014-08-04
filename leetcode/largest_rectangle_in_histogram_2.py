class Solution:
    # @param height, a list of integer
    # @return an integer
   def largestRectangleArea(self, height):
        maxArea = 0
        stackHeight = []
        stackIndex = []
        for i in range(len(height)):
            if stackHeight == [] or height[i] > stackHeight[-1]:
                stackHeight.append(height[i]); stackIndex.append(i)
            elif height[i] < stackHeight[-1]:
                lastIndex = 0
                while stackHeight and height[i] < stackHeight[-1]:
                    lastIndex = stackIndex.pop()
                    tempArea = stackHeight.pop() * (i-lastIndex)
                    if maxArea < tempArea: maxArea = tempArea
                    print maxArea
                stackHeight.append(height[i]); stackIndex.append(lastIndex)
        while stackHeight:
            print height, stackIndex
            tempArea = stackHeight.pop() * (len(height) - stackIndex.pop())
            if tempArea > maxArea:
                maxArea = tempArea
        return maxArea

def main():
    s = Solution()
    print s.largestRectangleArea([2,1,2])
    # print s.largestRectangleArea([1, 1])

if __name__ == "__main__":
    main()