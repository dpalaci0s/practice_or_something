for x in xrange(0, int(raw_input())):
    inp = map(int, raw_input().split())
    r = 1
    for n in xrange(0, inp[1]):
        d = float(inp[0])/r
        r = float(r+d)/2
    print r,
