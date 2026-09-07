def create_disctionary(pnames,prices):
    my_products=dict()
    if len(pnames)!=len(prices):
        print("pnames and prices are does not match")
    else:
        for i in range(len(pnames)):
            my_products[pnames[i]]=prices[i]  
        return my_products

a=create_disctionary(["Keyboard","Mouse","Monitor","Printer"],[500,350,4000,8000]) 
print(a)
