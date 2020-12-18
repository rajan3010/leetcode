from collections import defaultdict
def gridIllumination(N, lamps, queries):

    on=set()    #Store the lights which are on
    rows_lit=defaultdict(int)   # each for row col and diagnols lit testing
    cols_lit=defaultdict(int)
    diag_left_lit=defaultdict(int)
    diag_right_lit=defaultdict(int)

    adj_bulbs=[[0,0],[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1],[-1,0],[-1,1]]
    res=[]
    for r,c in lamps: # illuminate the rows and diagnols based on the light lit
        on.add((r,c))
        rows_lit[r]+=1
        cols_lit[c]+=1
        diag_left_lit[r-c]+=1
        diag_right_lit[r+c]+=1

    for r,c in queries: #Check the queried bulb locations and see if they are lit
        turned_on= rows_lit[r] or cols_lit[c] or diag_left_lit[r-c] or diag_right_lit[r+c]
        res.append(+bool(turned_on))

        if turned_on: #If the grid is illuminated, switch off any ajacent bulbs which might be on
            for i,j in adj_bulbs:
                if (r+i,c+j) in on:
                    on.remove((r+i, c+j))
                    rows_lit[r+i]-=1
                    cols_lit[c+j]-=1
                    diag_left_lit[(r+i)-(c+j)]-=1
                    diag_right_lit[(r+i)+(c+j)]-=1

    return res

N = 5
lamps = [[0,0],[0,4]]
queries = [[0,4],[0,1],[1,4]]

print(gridIllumination(N, lamps, queries))