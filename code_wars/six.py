from string import punctuation
s = input()
negs = ['DONT', 'CANT', 'ISNT', 'HAVENT', 'CANNOT', 'WOULDNT', 'COULDNT',
'WONT', 'NO', 'NOT', 'NEVER', 'NOBODY', 'NOWHERE', 'NEITHER', 'AINT']
while s is not ".":
    negCount = 0
    orig = s
    for c in punctuation:
       s = s.replace(c, "")
    words = list(s.split(" "))
    for n in range(0,len(words)):
        if words[n] in negs:
            negCount+=1
    print(str(negCount) + ": " + orig)
    s = input()