def fib():
    num0 = 0
    num1 = 1
    fib = 0
    length = 0;
    n = 1
    nums = []*1000
    for x in xrange(0,1000):
        fib = num0+num1
        num0 = num1
        num1 = fib
        n+=1
        nums.append(fib)
    return nums
nums = fib()
for x in xrange(0,int(raw_input())):
    num = int(raw_input())
    for i in xrange(0,len(nums)):
        if nums[i] == num:
            print i+2,
