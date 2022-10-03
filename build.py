count = int(input("Enter limit:"))
lst = []
i = 0
a = 0
b = 1
while i < count:
    lst.append(a)
    a, b = b, a + b
    i += 1
print(lst)
