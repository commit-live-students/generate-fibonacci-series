n = int(raw_input('Enter n :'))

a,b = 0,1

print a
print b

i = 2

while i < n:
	c = a+b
	print c

	a,b = b,c
