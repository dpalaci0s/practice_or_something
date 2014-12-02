for i in xrange(0,int(raw_input())):
    temp = raw_input()
    haw = map(float,temp.split())
    bmi = haw[0]/(haw[1] ** 2)
    if bmi < 18.5:
        print 'under',
    elif bmi>=18.5 and bmi < 25.0:
        print 'normal',
    elif bmi>=25.0 and bmi < 30.0:
        print 'over',
    else:
        print 'obese',
