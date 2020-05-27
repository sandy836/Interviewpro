def dfs(matrix, i, j):
    if i<0 or i>=len(matrix) or j<0 or j>=len(matrix[0]) or matrix[i][j] != '1':
        return
    matrix[i][j] = '#'
    dfs(matrix, i-1, j)
    dfs(matrix, i+1, j)
    dfs(matrix, i, j-1)
    dfs(matrix, i, j+1)


def countIsland(matrix):
    count = 0
    if not matrix:
        return count
        
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[0])):
            if matrix[i][j] == '1':
                count += 1
                dfs(matrix, i, j)
    return count

print(countIsland([["1","1","1","0","0"],["1","1","0","1","0"],
["1","1","0","0","0"],["0","0","0","0","0"]]))
