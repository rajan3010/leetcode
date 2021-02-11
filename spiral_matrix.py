def spiralOrder(matrix):

    R=len(matrix)
    C=len(matrix[0])
    seen=[[False]*C for _ in matrix]

    dx=[0,1,0,-1]
    dy=[1,0,-1,0]

    r=0
    c=0

    i=0

    res=[]
    for _ in range(R*C):

        res.append(matrix[r][c])
        seen[r][c]=True
        ix=r+dx[i]
        jy=c+dy[i]    

        if 0<=ix<R and 0<=jy<C and seen[ix][jy]!=True:
            r=ix
            c=jy
        else:
            i=(i+1)%4
            r, c=r+dx[i], c+dy[i]

    return res

matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print(spiralOrder(matrix))