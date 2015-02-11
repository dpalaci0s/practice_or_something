def sieve(n):
    primes, sieve = [], [1] * (n + 1)
    for p in range(2, n + 1):
        if sieve[p]:
           primes.append(p)
           for i in range(2 * p, n + 1, p):
               sieve[i] = False
    return primes

f = open("nine.txt","r")
primes = sieve(1000)
lines = f.readlines()
lines = lines[:-1]
for line in lines:
	int1 = (int(line)/2)
	int2 = (int(line)/2)
	while(True):
		if(int1 + int2 == int(line)):
			if(int1 in primes):
				if(int2 in primes):
					break
				else:
					int1-=1
					int2+=1
					continuej
			else:
				int1-=1
				int2+=1
				continue
		else:
			int1-=1
			int2+=1
	print(str(int1) + " + " + str(int2) + " = " + str(line))
