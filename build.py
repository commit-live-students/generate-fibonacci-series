n = int(raw_input('Enter n :'))

output = []

a,b = 0,1

output.extend([a,b])

i = 2

while i < n:
    c = a + b
    a,b = b,c
    output.append(c)
    i = i +1

print output
