def minimumPathSum(grid):

    if not grid:
        return 0


    rows=len(grid)
    cols=len(grid[0])

    for r in range(rows):
        for c in range(cols):
            if r==0 and c==0:
                pass
            elif r==0:
                grid[r][c]=grid[r][c]+grid[r][c-1]
            elif c==0:
                grid[r][c]=grid[r][c]+grid[r-1][c]
            else:
                grid[r][c]=grid[r][c]+min(grid[r-1][c], grid[r][c-1])

    return grid[rows-1][cols-1]

grid = [[1,2,3],[4,5,6]]
print(minimumPathSum(grid))