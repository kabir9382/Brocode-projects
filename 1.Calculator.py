#PYTHON Calculator

#Taking two integers as input
a=int(input("Enter First Number:"))
b=int(input("Enter Second Number:"))


operator = input("Choose Your Operation: ")

#Conditions

if operator=="+":
    print("Addition:",a+b)
elif operator=="-":
    print("Substraction:",a-b)
elif operator=="*":
    print("Multiplication:",a*b)
elif operator=="/":
    print("Division:",a/b)
else:
    print("Invalid")

