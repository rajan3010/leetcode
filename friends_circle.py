def findCircleNum(M):

    if not M:
        return 0
    
    visited=[False]*len(M)

    def dfs(first):
        for j in range(first, len(M)):
            if visited[j]==False and M[first][j]==1:
                visited[j]=True
                dfs(j)

    count=0
    for i in range(len(M)):
        if visited[i]==False:
            visited[i]=True
            count+=1
            dfs(i)

    return count

input=[[1,1,0],[1,1,0],[0,0,1]]
print(findCircleNum(input))