__author__ = "dpalaci0s"
import time
start = time.time()
pows = []
for a in xrange(2,101):
    for b in xrange(2,101):
        pows.append(a**b)
pows.sort()
sum = 0
for n in xrange(len(pows)-2):
    if pows[n] == pows[n+1]:
        sum+=1
print len(pows) - sum, time.time()-start
