def merge(intervals):

    intervals.sort(key=lambda x:x[0])

    res=[]
    curr_start=0
    curr_end=0
    #print("always")

    for start,end in intervals:
        if not res:
            #print("always")
            res.append([start, end])
        else:
            curr_start, curr_end=res.pop()
            #print(curr_start)
            #print(curr_end)
            if start>=curr_start and start<=curr_end:
                res.append([min(curr_start,start), max(curr_end,end)])
                #print(res)
            else:
                res.append([curr_start, curr_end])
                res.append([start, end])
                #print(res)

    return res

intervals = [[1,4],[4,5]]
print(merge(intervals))