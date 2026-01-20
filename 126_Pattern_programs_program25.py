n=int(input('Enter No of Rows:'))
for i in range(n):
	print((chr(65+i)+' ')*(i+1))
for i in range(n-1):
	print((chr(63+n-i)+' ')*(n-1-i))