print("Password Checker App")
passw=input("Please, Enter your password: ")

has_upper=False
has_lower=False
has_number=False
has_special=False
special_characters = "@#$%&!*"
#check char one by one
for char in passw:
    if char.isupper():
        has_upper=True
    elif char.islower():
        has_lower=True
    elif char.isdigit():
        has_number=True
    elif char in special_characters:
        has_special=True

if len(passw)<8:
    print("Weak Password")
    print("Reason. Password should have at least 08 characters")
elif has_upper and has_lower and has_special and has_number:
    print("Strong Password")
else:
    print("Medium Password")
    if not has_upper:
        print("Add at least one UpperCase Lettter")
    if not has_lower:
        print("Add at least one LowerCase Letter ")
    if not has_number:
        print("Add at least one Number")
    if not has_special:
        print("Add at least one Special Character")
