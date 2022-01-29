def bestSum(target,arr):
    table = [None]*(target+1)
    table[0] = []
    for i in range(target):
        if table[i] != None:
            for num in arr:
                if i+num<=target:
                    combination = table[i]+[num]
                    if (table[i+num]==None or len(combination)<len(table[i+num])):
                        table[i+num] = combination
    return table[target]
ans = bestSum(8,[2,3,5])
print(ans)