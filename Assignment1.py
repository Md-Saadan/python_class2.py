all_product=[]
for i in range(3):
    e_commerce=()
    order_id=int(input("Enter id"))
    product_name=(input("Enter product name"))
    price=float(input("Enter price"))
    qty=int(input("Enter the qty"))
    city=(input("Enter the City Name"))
    payment_method=(input("Enter the Payment method COD,UPI,Net Banking"))
    if payment_method not in ("COD","UPI","Net Banking"):
        print("The payment method is invalid")
        break
    amount=price*qty
    
        