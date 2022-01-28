memo = {}
def canConstruct(target,wordbank):
    if target in memo:
        return memo[target]
    if len(target) == 0:
        return True
    for word in wordbank:
        if target.rfind(word) == 0:
            k = len(word)
            suffix = target[k:]
            if (canConstruct(suffix,wordbank)==True):
                memo[target] = True
                return True
    memo[target] = False
    return False
ans = canConstruct('abcdef',['ab','abc','cd','def','abcd'])
print(ans)