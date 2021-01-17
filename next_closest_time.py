def nextClosestTime(time):

    digit_set={int(x) for x in time if x!=':'} #This is a set, Initializing curly braces with values is set.Withou

    curr_time_mins=int(time[:2])*60+int(time[3:])

    while True:

        curr_time_mins=(curr_time_mins+1)%(24*60)

        if all(digit in digit_set for unit in divmod(curr_time_mins,60) for digit in divmod(unit,10)):
            return "{:02d}:{:02d}".format(*divmod(curr_time_mins, 60))

print(nextClosestTime("23:59"))