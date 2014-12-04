def neumann(n):
    num=n
    num2 = 0
    prev = [0]*1000
    count = 0
    while num2 != n:
        sq = (num**2)
        num2 = (sq/100)%10000
        if num2 in prev:
            count+=1
            break
        else:
            prev.append(num2)
            count+=1
        num=num2
    print count

throw_away = raw_input()
nums = map(int, raw_input().split())
for i in xrange(0,len(nums)):
    neumann(nums[i])


