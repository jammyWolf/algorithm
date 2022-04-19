def combinationSum(candidates, target: int):
    ret = []
    def miniSearch(cans, combine, tar):
        if tar==0:
            if combine not in ret:
                ret.append(combine)
            return
        elif tar<0:
            return 
        else:
            for i, c in enumerate(cans):
                miniSearch(cans[i:], combine+[c], tar - c)
       
    miniSearch(candidates, [], target) 
    return ret

for c, t in zip([[2,3,6,7],[2,3,5],[2]],[7,8,1]):
    a = combinationSum(c, t)
    print(a)

