def canSum(target,arr):
    table = [False]*(target+1)
    table[0] = True
    for i in range(len(table)):
        if table[i]==True:
            for num in arr:
                if i+num<=target:
                    table[i+num] = True
    return table[target]
ans = canSum(7,[3,10])
print(ans)
