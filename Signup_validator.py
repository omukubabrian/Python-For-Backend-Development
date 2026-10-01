username=input("Username:").strip()
password=input("Password:")

if not username:
    print("Error:username is required!")
elif len(password)<8:
    print("Error must be at least 8 characters")
elif password==username:
    print("Error:Password must differ from username")
else:
    print("Signup OK")