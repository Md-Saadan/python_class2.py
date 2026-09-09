import math
numbers=[17,52,6,85,54,85,98,2,3,5,8]
oddeven=[0 if i%2==0 else 1 for i in numbers]
print(oddeven)

digits=["two" if i>=10 and i<=99 else "one" for i in numbers]
print(digits)

numbers=[i*i for i in range(20)]
print(numbers)
sqrts=[round(math.sqrt(i,2)for i in range(0,100,5))]
print(sqrts)
print([i for i in range(1,500) if i%5==0 and i%7==0])

s,e=map(int,input("Enter start and end").split())
n,m=map(int,input("Enter the number to divide:").split())
l=[i for i in range(s,e)if i%n==0 and i%m==0]
print(l)
