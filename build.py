val = 10
fibo = []
a = 0
b = 1
count = 2
fibo.extend([a,b])
while count < val:
	c = a + b
	a,b = b,c
	fibo.append(c)
	count += 1
print fibo
