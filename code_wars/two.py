import sys
count = int(sys.stdin.readline())
while (count > 0):
    count -= 1
    line = sys.stdin.readline().rstrip('\n')
    currentDigit=1
    checkDigit=0
    for c in line:
        if (c.isdigit()):
            value = int(c)
            checkDigit += value
            if (currentDigit % 2 == 1):
                checkDigit += value+value # Add odd positions a total of 3 times.
            currentDigit += 1
    checkDigit = checkDigit % 10
    print (line, (10-checkDigit)%10)