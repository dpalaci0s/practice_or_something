f = open('eleven.txt','r')
lines = f.readlines()
lines = lines[:-1]
for l in lines:
	nums = l.split(" ")
	for n in range(1, 1000000):
		if(n%int(nums[0])==int(nums[3]) and n%int(nums[1])==int(nums[4]) and n%int(nums[2])==int(nums[5])):
			print(n)
			break