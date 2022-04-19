def letterCombinations(digits: str):
    if not digits: return []
    ret = []
    ALP = {'2':"abc", '3':"def", '4':"ghi", \
        '5':"jkl", '6':"mno", '7':"pqrs", '8':"tuv", '9':"wxyz"}
    total_num = len(digits)

    def search(digits, combine, idx):
        if len(combine)==total_num:
            ret.append(combine)
            return

        else:
            for x in ALP[digits[idx]]:
                search(digits, combine+x, idx+1)
    
    search(digits, "", 0) 
    return ret

a = "23"
a = ""
a = "2"
print(letterCombinations(a))

    
            
        