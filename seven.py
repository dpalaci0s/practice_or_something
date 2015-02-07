from math import isnan
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
	print(tot)

def toString(n):
	m_count = int(n/10000)
	c_count = int(n%10000/1000)
	h_count = int(n%10000%1000/100)
	d_count = int(n%10000%1000%100/10)
	p_count = int(n%10000%1000%100%10/5)
	i_count = int(n%10000%1000%100%10%5)
	if m_count >= 5:
		print('P' + (m_count-4)*'M')
	else: 
		print('M'*m_count, end="")
	if c_count >= 5:
		print('P' + (c_count-4)*'C',end="")
	else: 
		print('C'*c_count, end="")
	if h_count >= 5:
		print('P' + (h_count-4)*'H',end="")
	else: 
		print('H'*h_count, end="")
	if d_count >= 5:
		print('P' + (d_count-4)*'D',end="")
	else: 
		print('D'*d_count, end="")
	print('P'*p_count,end="")
	print('I'*i_count,end="")

toString(475)


