def gcd(x,n):
    gcdV=0
    for i in xrange(1,max(x,n)):
        if x%i==0 and n%i==0:
            gcdV=i
    return gcdV

def lcm(x,n):
    return (x/gcd(x,n))*n

for x in xrange(0, int(raw_input())):
    nums = map(int, raw_input().split())
    print "(" + str(gcd(nums[0],nums[1])) + " " + str(lcm(nums[0],nums[1])) + ")",
