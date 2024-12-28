#Python weight converter

weight = int(input("enter weight: "))
unit = input("KG or LBS: ")

if unit=="KG":
    conv = 2.2 * weight
    print(conv,"Pound")
elif unit == "LBS":
    conv = .45 * weight
    print(conv,"KG")
