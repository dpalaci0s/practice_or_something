x = raw_input()
for i in xrange(0,int(x)):
    nums = map(int,raw_input().split())
    list.sort(nums)
    print nums[1],
