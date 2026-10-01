#A server retries a failed connection up to 3 times
for attempt in range(1,4):
    answer=input(f"Attempt{attempt}:did it connect?(Y/n)").lower()
    if answer=="Y":
        print("Connected!")
        break
    else:
        print("Giving up")
 