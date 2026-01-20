n=int(input('Enter no of zrows:'))
for i in range(n):
	print(' '*i,end='')
	for j in range(n-i):
		print(j+1,end=' ')
	print()		