import itertools
f = open('thirteen.txt','r')
lines = f.readlines()
lines = lines[:-1]
words = []
lets = lines[1].split(" ")
lets[len(lets)-1] = lets[len(lets)-1][0]
lets.sort()
perms = list(itertools.permutations(lets,5))
nuPerms = []
for n in range(0, len(perms)):
	if perms[n] not in nuPerms:
		nuPerms.append(perms[n])

answer = ""
for i in range(2, len(lines)):
	for x in range(0, len(nuPerms[int(lines[i])-1])):
		answer+=str(nuPerms[int(lines[i])-1][x])
	print(answer)
	answer=""