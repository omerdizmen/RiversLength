def rivers(array):
    memo = {}    
    rivers = []
    for x in range(len(array)):
        for  y in range(len(array[0])):
            if array[x][y] == 1:
                river = getFoundRiverLength(array, x, y, memo)
                rivers.append(river)
    
    return rivers


def getFoundRiverLength(array, x, y, memo):    
    if x > len(array) - 1 or y < 0 or y > len(array[0]) - 1:
        return 0
    
    if f"{x}{y}" in memo:
        return 0

    if (array[x][y] == 0):
        return 0

    length = 1
    
    memo[f"{x}{y}"] = 1

    length += getFoundRiverLength(array, x+1, y, memo)
    length += getFoundRiverLength(array, x, y+1, memo)
    length += getFoundRiverLength(array, x, y-1, memo)

    
    
    return length

array = [
    [1, 0, 0, 1, 0],
    [1, 0, 1, 0, 0],
    [0, 0, 1, 0, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 1, 1, 0]
]
memo = {}  


print(rivers(array))
