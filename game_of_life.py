def gameOfLife(board):
    rows=len(board)
    cols=len(board[0])

    neighbors=[(-1,0),(-1,-1),(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1)]

    for r in range(0,rows):
        for c in range(0,cols):

            liveCount=0

            for n in neighbors:

                if(((r+n[0])>-1 and (r+n[0])<rows) and ((c+n[1])>-1 and (c+n[1])<cols) and abs(board[r+n[0]][c+n[1]])):
                    liveCount=liveCount+1

            #Apply the rules    #Set -1 for dying flag and 2 for spawning flag
            if board[r][c]==1 and (liveCount<2 or liveCount>3):
                board[r][c]=-1
            elif board[r][c]==0 and liveCount==3:
                board[r][c]=2

    for r in range(0,rows):
        for c in range(0,cols):
            if board[r][c]>0:
                board[r][c]=1
            else:
                board[r][c]=0

    return board

input=[
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]

print(gameOfLife(input))