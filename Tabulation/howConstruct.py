def howConstruct(target,wordbank):
    table = [0]*(len(target)+1)
    table[0] = 1
    for i in range(len(target)):
        if table[i] != None:
            for word in wordbank:
                if target[i:i+len(word)] == word:
                    table[i+len(word)] += 1
    return table[len(target)]
ans = howConstruct('abcdef',['ab','abc','cd','def','abcd'])
print(ans)