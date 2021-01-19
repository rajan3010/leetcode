def minMeetingRooms(intervals):

    N=len(intervals)

    start_sorted=sorted([i[0] for i in intervals])
    end_sorted=sorted([i[1] for i in intervals])

    start_ptr=end_ptr=0

    room_count=0

    while start_ptr<N:
        if start_sorted[start_ptr]<end_sorted[end_ptr]:
            room_count+=1
            start_ptr+=1
        else:
            start_ptr+=1
            end_ptr+=1

    return room_count

intervals = [[7,10],[2,4]]
print(minMeetingRooms(intervals))