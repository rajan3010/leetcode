from collections import deque

def numSquares(n):
    sqr_cache=[]
    count=0

    for i in range(int(n**0.5)+1):
        sqr_cache.append(i*i)

    bfs_queue={n}

    while(bfs_queue):
        count+=1
        
        temp=set()
        for num in bfs_queue:
            for sqr in sqr_cache:
                if sqr==num:
                    return count
                elif sqr<num:
                    temp.add(num-sqr)
        bfs_queue=temp
    return count


print(numSquares(13))