for x in xrange(0,int(raw_input())):
    data = map(int,raw_input().split())
    day1 = (data[0]*(3600*24))+(data[1]*3600)+(data[2]*60)+data[3]
    day2 = (data[4]*(3600*24))+(data[5]*3600)+(data[6]*60)+data[7]
    diff = day2-day1
    days = diff/(3600*24)
    hours = diff%(3600*24)/3600
    minutes = diff%(3600*24)%3600/60
    seconds = diff%(3600*24)%(3600)%60
    print "("+ str(days), str(hours), str(minutes), str(seconds) + ")"
