a=0
b=1

print a
print b
n=10
i=2
while i < n:
	c = a + b
	print c

	a, b = b, c
	i = i + 1
