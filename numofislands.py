def dfs(grid, row, col):
    r=len(grid)
    c=len(grid[0])

    grid[row][col]='0'
    if (row+1<r and grid[row+1][col]=='1'): dfs(grid, row+1, col)
    if (row-1>=0 and grid[row-1][col]=='1'): dfs(grid, row-1, col)
    if (col+1<c and grid[row][col+1]=='1'): dfs(grid, row, col+1)
    if (col-1>=0 and grid[row][col-1]=='1'): dfs(grid, row, col-1)

    return

def numislands(grid):
    rows=len(grid)
    island_count=0

    if rows==0:
        return 0
    col=len(grid[0])

    for i in range(0,rows):
        for j in range(0,col):
            if grid[i][j]=='1':
                island_count+=1
                dfs(grid, i ,j)
    return island_count
