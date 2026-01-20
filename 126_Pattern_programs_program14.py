n=int(input('Enter Number of rows:'))
for i in range(n):
	print(' '*(n-i-1) + (chr(i+65)+' ')*(i+1))