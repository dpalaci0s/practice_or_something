def bubble_sort(n):
    size = len(n)
    nums = n
    pass_count = 0
    test_count = 0
    swap_count = 0
    temp = 0
    is_sorted = False
    while not is_sorted:
        test_count=0
        for x in xrange(0, size-1):
            if nums[x] > nums[x+1]:
                temp = nums[x]
                nums[x] = nums[x+1]
                nums[x+1] = temp
                swap_count+=1
            pass_count+=1
        for x in xrange(0,size-1):
            if nums[x] > nums[x+1]:
                test_count+=1
        is_sorted = True
    return swap_count
def checksum(nums):
    result = 0
    for x in xrange(0, len(nums)):
        result = (result+nums[x])*113
        result%=10000007
    print result

nums = map(int, raw_input().split())
nums.remove(-1)
print bubble_sort(nums), checksum(nums)
