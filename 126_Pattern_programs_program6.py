n=int(input('Enter Number of rows:'))
#for i in range(n):
#	print('* '*(n-i))

#for i in range(n):
#	for j in range(n-i):
#		print('*',end=' ')
#	print()

#for i in range(n):
#	print((chr(i+65)+' ') * (i+1) )

for i in range(n):
	for j in range(i+1):
		print(chr(i+65),end=' ')
	print()

