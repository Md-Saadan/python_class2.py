def restaruent_bill(recipes):
    total=0

    print("............RESTURENT_BIll...........")

    for i,(item,price)in enumerate(recipes.items(),start=1):
        print(f"{i}:{item}   {price}")
        total+=price

    gst_rate=0.06
    gst =total *gst_rate
    final_amount=total + gst

    print("..........................")
    print(f"Total Bill Amount {total}")
    print(f"GST {gst_rate}      {gst:.2f}")
    print(f"Bill Amount With GST {final_amount:.2f}")

recipes = {"Briyani":500,"Chiken":400}
restaruent_bill(recipes)