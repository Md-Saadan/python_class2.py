def display_result(students):
    total_percentage=0
    for s in students:
        total=sum(s["marks"])
        percentage=round(total/len(s["marks"]),2)
        s["total"]=total
        s["percentage"]=percentage
        print(s)
        total_percentage+=s["percentage"]
    return round(total_percentage/len(students),2)

list_of_students=[{"name":"Abdullah","marks":[45,74,85,85,65,65]},
                 {"name":"Abdurrahman","marks":[65,84,80,81,65,55]},
                 {"name":"Sarim","marks":[65,85,75,70,66,50]},
                 {"name":"Adeem","marks":[70,90,80,90,88,47]}]
avg=display_result(list_of_students)
print("average percentage of all student are:",avg)

