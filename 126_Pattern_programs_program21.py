n=int(input('Enter Number of Rows:'))
for i in range(n):
	print(' '*i + (str(i+1)+' ') * (n-i))