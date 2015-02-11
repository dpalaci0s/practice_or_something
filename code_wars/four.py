from math import fabs
from collections import OrderedDict
correct = int(input())
s = ""
for n in range(0, int(input())):
    s+=input() + '\n'
    d = OrderedDict(map(lambda l: l.split(), s.splitlines()))
print(d)
winners = []
nearest = 1000
for guess in d.keys():
    if (fabs(correct-int(guess))) < nearest:
        nearest = fabs(correct-int(guess))
for sec in d.keys():
    if (fabs(correct-int(sec)))==nearest:
        winners.append(d[sec])
for i in range(0,len(winners)):
    print(winners[i], end=" ")