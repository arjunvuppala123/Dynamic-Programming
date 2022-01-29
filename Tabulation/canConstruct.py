def canConstruct(target,wordbank):
    table = [False]*(len(target)+1)
    table[0] = True
    for i in range(len(target)):
        if table[i] == True:
            for word in wordbank:
                if target[i:i+len(word)] == word:
                    table[i+len(word)] = True
    return table[len(target)]
ans = canConstruct('abcdef',['ab','abc','cd','def','abcd'])
print(ans)