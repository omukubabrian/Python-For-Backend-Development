name=input("Fill name: ").strip()
if name !="":
    with open("guest.txt", "a") as f:
        f.write(name +"\n")
    print("Thanks for signing!")
else:
    print("No name entered,nothing saved.")

count=0
try:
    with open("guest.txt","r") as f:
        for line in f:
            count+=1

except FileNotFoundError:
    pass
print(f"Guests so far:{count}")