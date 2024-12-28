value = float(input("Enter Temparature:"))
unit = input("Celsius or Ferheinheit 'C' or 'F': ")

if unit=="C":
    print("Converting to Ferheinheit")
    conv = ((9*value)/5) + 32
    print(value,"Celsius=",round(conv,2),"Ferheinheit")
elif unit=="F":
    print("Converting to Celsius")
    conv = ((5*value)-160)/9
    print(value,"Ferheinheit=",round(conv,2),"Celsius")
else:
    print("Invalid Input")