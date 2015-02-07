def toInt(n):
	d = {'I':1,'P':5,'D':10,'H':100,'C':1000,'M':10000}
	tot = 0
	x = 0
	while(x < len(n)):
		if n[x] == 'P' and x < len(n)-1:
			if n[x+1] == 'I':
				tot+=5*d[n[x+1]]
				x+=1
			else:
				tot+=5*d[n[x+1]]
				x+=2
		else:
			tot+=d[n[x]]
			x+=1
	return tot

def toString(n):
	m_count = int(n/10000)
	c_count = int(n%10000/1000)
	h_count = int(n%10000%1000/100)
	d_count = int(n%10000%1000%100/10)
	p_count = int(n%10000%1000%100%10/5)
	i_count = int(n%10000%1000%100%10%5)

	return m_count, c_count, h_count, d_count, p_count, i_count

print(toString(12))



