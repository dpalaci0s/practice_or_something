def josephus(group, step):
    step -= 1
    index = step
    while len(group) > 1:
        group.pop(index)
        index = (index+step) % len(group)
    return group[0]
inp = map(int, raw_input().split())
nums = [0]*inp[0]
for x in xrange(0, len(nums)):
    nums[x] = x+1
print josephus(nums,inp[1])
