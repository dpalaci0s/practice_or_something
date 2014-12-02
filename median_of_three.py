import math
for i in xrange(0,int(raw_input())):
    nums = map(int,raw_input().split())
    print (nums[0]+nums[1]+nums[2])-min(nums[0],nums[1],nums[2])-max(nums[0],nums[1],nums[2])
