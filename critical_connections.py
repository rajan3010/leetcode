def criticalConnections(n, connections):

    adj_mat=[[] for nodes in range(n)]
    
    for n1, n2 in connections:
        adj_mat[n1].append(n2)
        adj_mat[n2].append(n1)
    
    disc_time_node=[-1]*n #equivalent to unvisited nodes
    res=[]

    def dfs(node, expected_disc_time, parent):

        if disc_time_node[node]==-1:

            disc_time_node[node]=expected_disc_time

            for i in adj_mat[node]:

                if i!=parent:
                    actual_disc_time=dfs(i, expected_disc_time+1, node)

                    if actual_disc_time>expected_disc_time:
                        res.append([node, i])

                    disc_time_node[node]=min(actual_disc_time,expected_disc_time) # To ensure that in a cyclic case, the lowest discovery time is set for all the prvious nodes

        return disc_time_node[node]

    dfs(n-1, 0, -1)

    return res

n = 4
connections = [[0,1],[1,2],[2,0],[1,3]]

print(criticalConnections(n, connections))