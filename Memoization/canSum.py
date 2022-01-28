memo = {}
def canSum(arr,target):
    if target in memo:
        return True
    if target == 0:
        return True
    if target < 0:
        return False
    for i in arr:
        target = target - i
        if canSum(arr,target):
            memo[target] = True
            return memo[target]
    memo[target] = False
    return memo[target]
arr = [2,3]
target = 7
res = canSum(arr,target)
print(res)