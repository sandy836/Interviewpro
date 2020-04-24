def dfs(x, y, matrix, depth, word):
    if depth == len(word):
            return True
    if x<0 or x>=len(matrix) or y<0 or y>=len(matrix[0]) or matrix[x][y] != word[depth]:
        return False
    temp = matrix[x][y]
    matrix[x][y] = '#'
    res = dfs(x-1,y, matrix, depth+1, word) \
        or dfs(x+1,y, matrix, depth+1, word) \
            or dfs(x,y+1, matrix, depth+1, word) \
                or dfs(x,y-1, matrix, depth+1, word)
    matrix[x][y] = temp
    return res

def word_search(matrix, word):
    row, col = len(matrix), len(matrix[0])
    for i in range(row):
        for j in range(col):
            if word[0] == matrix[i][j]:
                if dfs(i, j, matrix, 0, word):
                    return True
    return False
  

matrix = [
  ['F', 'A', 'C', 'I'],
  ['O', 'B', 'Q', 'P'],
  ['A', 'N', 'O', 'B'],
  ['M', 'A', 'S', 'S']
  ]
print(word_search(matrix, 'ABQOSSBPI'))