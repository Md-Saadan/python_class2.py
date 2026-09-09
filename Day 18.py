# Method_1
phy=int(input("Enter Marks of Physics"))
bio=int(input("Enter Marks of Biology"))
chem=int(input("Enter Marks of Chemistry"))
total=phy+bio+chem
print("total")
if total>=550:
      print("elligible for MBBS ")
elif total<550 and total>=450:
    print("elligible for BDS")
elif total<450 and total>=350:
    print("elligible for BAMS")
elif total<350 and total>=200:
     print("elligible for BUMS")
else:
      print("not elligible")
# Method_2
phy,chem,bio=map(int,input("Enter Three Numbers").split())
print(f"phy:{phy}\n chem:{chem}\n bio:{bio}")
total=phy+chem+bio
print(total)
if total>=550:
      print("elligible for MBBS ")
elif total<550 and total>=450:
    print("elligible for BDS")
elif total<450 and total>=350:
    print("elligible for BAMS")
elif total<350 and total>=200:
     print("elligible for BUMS")
else:
      print("not elligible")


     
