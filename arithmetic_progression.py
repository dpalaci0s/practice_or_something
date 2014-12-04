for x in xrange(0,int(raw_input())):
    nums = map(int,raw_input().split())
    sum = 0
    for i in xrange(0,nums[2]):
        sum+=(nums[0] + i*nums[1])
    print sum,
