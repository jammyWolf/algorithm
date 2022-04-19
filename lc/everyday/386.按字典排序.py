def lexicalOrder(n: int):
    ret = list()
    num = 1
    for i in range(n):
        ans.append(num)
        if num * 10 <= n:
            num *= 10
        else:
            while num % 10 == 9 or num + 1 > n:
                num //= 10
            num += 1
    return ans

a = lexicalOrder(13)
print(a)