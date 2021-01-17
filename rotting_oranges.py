#O(n^4) time complexity solution, O(1) space complexity solution
def run_bfs(timestamp, grid):
    rows=len(grid)
    cols=len(grid[0])

    ret=False
    for r in range(rows):
        for c in range(cols):

            if grid[r][c]==timestamp:
                
                for roff,coff in [(-1,0),(0,1),(1,0),(0,-1)]:
                    #print("Enters")
                    if ((r+roff)>=0 and (r+roff)<rows) and ((c+coff)>=0 and (c+coff)<cols) and grid[r+roff][c+coff]==1:
                        grid[r+roff][c+coff]=timestamp+1
                        ret=True

    #print(grid)
    return ret

def rottingOranges(grid):

    rows=len(grid)
    cols=len(grid[0])

    timestamp=2

    while(run_bfs(timestamp,grid)):
        timestamp+=1

    for r in range(rows):
        for c in range(cols):
            if grid[r][c]==1:
                return -1
    
    return timestamp-2

grid =  [[0,2]]

print(rottingOranges(grid))