from string import punctuation
def isPangram(s):
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    sentence = set(s.lower())
    return sentence.issuperset(alphabet)
s = input()
rem = s
for q in punctuation:
    rem = rem.replace(q, "")
rem = rem.replace(" ", "")
sum = 0
for n in range(0,len(rem)):
    sum+=ord(rem[n])
if sum==2015:
    print("PERFECT: " + s)
elif isPangram(rem):
    print("PANGRAM: " + s)
else:
    print("NEITHER: " + s)