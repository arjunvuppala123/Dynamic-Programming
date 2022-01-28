memo = {}

def canConstruct(target,wordbank):
    if target in memo:
        return memo[target]
    if target == '':
        return 1
    totalCount = 0
    for word in wordbank:
        if target.rfind(word) == 0:
            numWays = canConstruct(target[len(word):],wordbank)
            totalCount += numWays
    memo[target] = totalCount
    return totalCount

ans = canConstruct('abcdef',['ab','abc','cd','def','abcd'])
print(ans)