password = input("Enter new password: ")

result = {}

if len(password) >= 8:
   result["length"] = True
    # result.append(True)
else:
   result["length"] = False
    # result.append(False)

digit = False
for i in password:
        if i.isdigit():
            digit = True

result["digits"] = digit
# result.append(digit)

uppercase = False
for i in password:
    if i.isupper():
        uppercase = True

result["upper-case"] = uppercase
# result.append(uppercase)

print((result))
print(result.values())


if all(result.values()):
# before was giving Strong password even tho weak
# had to change if all(result()): to current line above
# if all(result) == True:
    print("Strong password")
else:
    print("Weak password.")


