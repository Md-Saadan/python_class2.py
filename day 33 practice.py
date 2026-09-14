# Task 1
for i in range(1,21):
    print(i)

# Task 2
for i in range(1,51):
    if i%2==0:
        print(i)

# Task 3
s=0
for i in range(1,101):
    s=s+i
print(s)

# Task 4
num=int(input("Enter a number: "))
if num>0:
    print("Its a Positive number")
elif num<0:
    print("Its a Negative number")
else:
    print("Its zero")

# Task 5
i=1
num=int(input("Enter a Number: "))
for i in range(1,11):
    print(f"{num} * {i} = {num*i}")

# Task 6
name=input("Enter string: ")
count=0
for i in name:
    if i.lower() in "aeiou":
        count+=1
print("number of vowels in a given string is: ", count)

# Task 7
real=input("Enter string: ")
reverse=""
for i in real:
    reverse=i+reverse
print(reverse)

# Task 8
real=input("Enter string: ")
reverse=""
for i in real:
    reverse=i+reverse
if real==reverse:
    print("Given string is a Palindrome")
else:
    print("is not a palindrome")

# Task 9
list=[10,30,70,40,20,60,50,90]
large=list[0]
for i in list:
    if i>large:
        large=i
    print(large)

# Task 10
list=[10,30,70,40,20,60,50,90]
smallest=list[0]
for i in list:
    if i<smallest:
        smallest=i
print(smallest)

# Task 11
list=[65,96,54,32,98,63,12,37,95,73,76]
even=0
odd=0
for i in list:
    if i%2==0:
        even+=1
    else:
        odd+=1
print("Even:", even)
print("Odd:", odd)

# Task 12
List=[34,65,96,54,32,98,63,12,37,95,73,76]
print(List)
s=int(input("Enter a number to search: "))
for i in List:
    if i==s:
        break
if i==s:
    print("Number found in a list.")
else:
    print("Number not found.")

# Task 13
name=["Aadil","Qasim","Abdullah","Naeem","Aaquib","Khalid","Zahid","Aasim","Shafeeque","Waqqas","Aman","Imran","Ahmad"]
print(name)
for i in name:
    if i.startswith("A"):
        print(i)

# Task 14
sentense=input("Enter snetence.")
count=0
a=sentense.split()
for i in a:
    count+=1
print(count)

# Task 15
String=input("Enter String: ")
Char=input("Enter Charachter to search: ")
count=0
for i in String:
    if i==Char:
        count+=1
print(count)

# Task 16
numbers=[90,70,80,40,50,80,60,10,20,30,70,80,20]
new_list=[]
for i in numbers:
    if i not in new_list:
        new_list.append(i)
print(numbers)
print(new_list)

# Task 17
number=[78,95,86,27,95,34,45]
largest=number[0] 
second=number[0]
for i in number:    
    if i>largest:
        second=largest        
        largest=i   
    elif i>second and i!=largest:    
        second=i
print("Largest =",largest) 
print("Second largest =",second)


# Task 18
for num in range(2, 101):    
    prime = True
    for i in range(2, num):        
        if num % i == 0:            
            prime = False            
            break
    if prime:        
        print(num)

# Task 19
numbers=[20,-70,50,-55,-45,90,30,-25]
pos=[]
neg=[]
for i in numbers:
    if i>=0:
        pos.append(i)
    else:
        neg.append(i)
print(numbers)
print(pos)
print(neg)

# Task 20
marks=[93,87,89,59,86]
total=0
for i in marks:
    total+=i
prcnt=total/len(marks)
print("Marks:", marks)
print("Total: ",total)
print("Percentage: ",round(prcnt,2),"%")
if prcnt>=90:
    print("Grade: O")
elif prcnt>=80:
    print("Grade: A+")
elif prcnt>=70:
    print("Grade: A")
elif prcnt>=60:
    print("Grade: B+")
elif prcnt>=50:
    print("Grade: B")
elif prcnt>=40:
    print("Grade: C")
else:
    print("Fail")
