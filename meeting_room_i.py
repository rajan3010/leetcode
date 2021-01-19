def canAttendMeetings(intervals):
    
    sorted_intervals=sorted(intervals)

    for i in range(0,len(sorted_intervals)-1):
        if sorted_intervals[i+1][0]<sorted_intervals[i][1]:
            return False
        
    return True

intervals = [[13,15],[1,13]]
print(canAttendMeetings(intervals))

