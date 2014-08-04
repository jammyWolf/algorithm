
class Solution:
    # @param height, a list of integer
    # @return an integer
    def largestRectangleArea(self, height):
        stack_high = height
        if height != []:
            level = []
            ins_index =  []
            area = 0
            for i, each in enumerate(height):
                if len(level) == 0 or each >= level[-1]:
                    level.append(each)
                    ins_index.append(i)
                elif each < level[-1]:
                    last_index = 0
                    while level and level[-1] > each:
                        last_index = ins_index.pop()
                        tmp_area = level.pop()*(i-last_index)
                        if area < tmp_area: area = tmp_area
                    level.append(each)
                    ins_index.append(last_index)
            while level:
                tmp_area = level.pop()*(len(height)-ins_index.pop())
                if tmp_area > area:
                    area = tmp_area
            return area
        else:
            return 0

def main():
    s = Solution()
    print s.largestRectangleArea([2,1,2])
    # print s.largestRectangleArea([1, 1])

if __name__ == "__main__":
    main()
    

