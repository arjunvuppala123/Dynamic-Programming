def bestsum(arr,target,memo={}):
    if target in memo:
        return memo[target]
    if target == 0:
        return []
    if target < 0:
        return None 
    shortest_combination = []
    for i in arr:
        partial = bestsum(arr,target-i,memo)
        if partial != None:
            combination = partial + [i]
        if (len(combination) < len(shortest_combination)) or (shortest_combination == None):
            shortest_combination = combination
    memo[target] = shortest_combination
    return shortest_combination
if __name__ == "__main__":
    print(bestsum([1, 2, 5, 25],100))