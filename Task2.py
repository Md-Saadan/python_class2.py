def electricity_bill(consumers_data):
    bill_list=[]
    for units in consumers_data.values():
        if units<=200:
            amount=100+units*3
        elif units>200 and units<=300:
            amount=700+(units-200)*4
        elif units>300 and units<=400:
            amount=1100+(units-300)*5
        elif units>400 and units<=500:
            amount=1600+(units-400)*6
        else:
            amount=2200+(units-500)*7
        bill_list.append(amount)
    return bill_list

list_of_consumers={"abdullah":120,"Ali":250,"Mazz":300,"Aakif":450}
bill_amount=electricity_bill(list_of_consumers)
print("Calculated bill list",bill_amount)

