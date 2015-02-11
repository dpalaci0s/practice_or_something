def decode(length, code):
	decoded = ['@']*length
	lettersUsed = [0]*length
	c = 0
	cplaced = 0
	while cplaced < length:
		char = code[c]
		decoded[cplaced] = char
		lettersUsed[c] = 1
		cplaced+=1
		if cplaced < length:
			if char.isalpha(): 
				toMove = ord(char.upper())-ord('A')+1
			else:
				toMove = 1
			while toMove > 0:
				c = (c+1)%length
				if lettersUsed[c] == 0:
					toMove-=1
	return ''.join(decoded)

f = open('ten.txt','r')
lines = f.readlines()
lines = lines[:-1]
for l in lines:
	length, code = l.split(None, 1)
	out = decode(int(length), code)
	print(out)
