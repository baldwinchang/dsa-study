def permutations(items):
    def backtrack(items):
        if len(items) == 0:
            result.append([item for item in buffer])
        else:
            for i in range(len(items)):
                buffer.append(items[i])
                backtrack(items[:i] + items[i+1:])
                buffer.pop()
    result = []
    buffer = []
    backtrack(items)
    return result


print(permutations([1,1,2,3,4]))