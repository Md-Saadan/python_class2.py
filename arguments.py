# Positional Argument
def student_result(name,roll_number,marks):
    print("Name:",name)
    print("marks:",marks)
    print("percen",sum(marks)/len(marks))
    print("Roll_Number:",roll_number)

student_result("Ahmed",14,[23,45,76,70,78])
student_result("Mohammed",20,[97,64,64,87,98])
student_result("Ahmed",14,[60,50,78,76,58])

# Key Woard Argument
def student_result(name,roll_number,marks):
    print("name:",name)
    print("marks:",marks)
    print("percen",sum(marks)/len(marks))
    print("Roll_Number:",roll_number)

student_result(roll_number=20,name="Aakif",marks=[45,76,98,53,78,64])
student_result(roll_number=50,name="md",marks=[46,72,90,63,98,60])
student_result(roll_number=30,name="ah",marks=[50,78,98,55,77,63])

# Arbitarary Argument
def student_result(name,*marks):
    print("name:",name)
    print("marks:",marks)
    print("percen",sum(marks)/len(marks))
    # print("Roll_Number:",roll_number)

student_result("Aakif",45,76,98,53,78,64)
student_result("md",46,72,90,63,98,60)
student_result("ah",50,78,98,55,77,63)

   # Arbitarary Keywoard Argument
def student_result(**marks):
    #  print("name:",name)
    print("marks:",marks)
    # print("percen",sum(marks)/len(marks))
    # print("Roll_Number:",roll_number)

student_result(English=60,Maths=96,Urdu=50,Science=70)               

