primes=[]
for n in range(1,101):
    if n==1:
       print("{n} is not prime number")
    else:
      for d in range(2,(n//2)+1):
        if n%d==0:
        #  print(f"{n} is not prime number it is devisible by{n}")
            break
      else:
        primes.append(n)
print(primes)


         
        