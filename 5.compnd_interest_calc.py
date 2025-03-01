# Compound Interest Calculator

principle = float(input("Enter Principle Amount: "))

while principle <= 0:
    print("Principle amount cant be less than 0")
    principle = float(input("Enter Principle Amount: "))

rate_of_interest = float(input("Enter rate of interest: "))

while rate_of_interest < 0:
    print("Interest rate cant be less or equal to 0")
    rate_of_interest = float(input("Enter rate of interest: "))

time = int(input("Total Years: "))
while time <= 0:
    print("Time cant be less or equal to 0")
    time = int(input("Total Years: "))

final = principle * pow((1 + rate_of_interest/100),time)

print(f"The Final Amount after {time} years is {final:.2f}")






