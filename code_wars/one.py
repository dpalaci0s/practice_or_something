from math import sqrt,ceil
n = int(input())
while(n!=0):
    print(int(ceil(100*sqrt(n)+201/(n+1)+1)))
    n = int(input())