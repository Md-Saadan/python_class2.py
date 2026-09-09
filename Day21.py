
divisors = []
n=(int(input("Enter a number")))
for i in range(1,n):
        if n%i==0:
            divisors.append(i)
perfect = sum(divisors)        
print(divisors)
print(perfect)
if n==perfect:
    print(f"{n} is perfect number.")
else:
    print(f"{n} is not a perfect number.")


