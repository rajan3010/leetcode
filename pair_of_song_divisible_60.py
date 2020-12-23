from collections import defaultdict
def pairOfSongs(time):

    modulo=defaultdict(int)
    res=0

    for i in time:
        if i%60==0:
            res+=modulo[0]
        else:
            res+=modulo[60-(i%60)]
        
        modulo[i%60]+=1

    return res

time=[60,60,60]
print(pairOfSongs(time))