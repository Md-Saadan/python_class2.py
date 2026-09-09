#1 Write a program to convert distance from inches to cm,mm,km and miles
inch=float(input("Enter a distance inch:"))
cm=2.5*inch
print(f"Distance in cm={cm}")
mm=cm*10
print(f"Distance in mm={mm}")
meter=cm/100
print(f"Distance in meter={meter}")
km=meter/1000
print(f"Distance in km={km}")
miles=km*0.621371
print(f"Distance in miles={miles}")
