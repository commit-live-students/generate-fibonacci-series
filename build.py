"""Program to generate Fibonacci sequence"""

n1,n2,n3 = 1,0,0
fib=[]

n=int(input("Enter number of terms : "))

while(n>0):
    fib.append(n3)
    n3 = n1+n2
    n1, n2 = n2, n3
    n-=1

print(fib)
