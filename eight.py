f = open('eight.txt','r')
lines = f.readlines()
lines = lines[:-1]
for line in lines:
	spl = line.split(" ")
	num = int(spl[0])
	print(spl[-num-1])
