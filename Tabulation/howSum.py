def howSum(target,arr):
    table = [None]*(target+1)
    table[0] = []
    for i in range(target):
        if table[i] != None:
            for num in arr:
                if i+num<=target:
                    table[i+num] = table[i]+[num]
    return table[target]
ans = howSum(7,[2,3])
print(ans)