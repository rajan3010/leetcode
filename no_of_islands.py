def dfs(r, c, grid):

    rows=len(grid)
    cols=len(grid[0])

    if (r<0 or r>=rows) or (c<0 or c>=cols) or grid[r][c]!="1": # whilie doing dfs if the cell is out of bounds or is not land then no need to further proceed
        return
    
    grid[r][c]="0"  #equivalent to visited

    for roff,coff in [(-1,0),(0,1),(1,0),(0,-1)]:
        dfs(r+roff, c+coff, grid)

    return 

def numIslands(grid):

    rows=len(grid)
    cols=len(grid[0])

    isl_count=0

    for r in range(rows):
        for c in range(cols):

            if grid[r][c]=="1":
                dfs(r,c,grid)
                isl_count+=1
    
    return isl_count

grid = [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]

print(numIslands(grid))