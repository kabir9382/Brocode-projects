#Email Slicer Program

email = input("Enter your email: ")

find = email.find("@")

username = email[:find]
domain   = email[find:]

print("Your username is: ",username)
print("Your Domain is: ",domain)