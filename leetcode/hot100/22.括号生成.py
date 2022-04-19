from tabnanny import check
from turtle import right


def generateParenthesis(n: int):
    ret = list()
    def search(combine, left_cnt, right_cnt):
        if left_cnt==0 and right_cnt==0 and combine not in ret:
            ret.append(combine)
            return 
        if right_cnt<left_cnt:
            return
        if left_cnt>0:
            search(combine+'(', left_cnt-1, right_cnt)
        if right_cnt>0:
            search(combine+')', left_cnt, right_cnt-1)


    search("", n, n)
    return ret


for each in range(1, 6):
    print(generateParenthesis(each))