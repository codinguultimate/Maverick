secretpassword = "Tinker" 
while True:
    password = input("Enter the password: ")
    if password.lower() == secretpassword.lower():
        print("Access granted.")
        break
    else:
        print("Access denied. Try again.")