for i in xrange(0,int(raw_input())):
    nums = map(int,raw_input().split())
    list.sort(nums)
    print nums[1],
