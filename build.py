fibo_list = [0, 1]
n = 10
i = 1
while i < n - 1:
    fibo_list.append(fibo_list[i - 1] + fibo_list[i])
    i += 1
print fibo_list
