prices={"apple":60,"banana":50,"mango":30}
total=0
for fruit,price in prices.items():
    total +=price
print(f"Total:{total}")




prices={"apple":50,"banana":20,"mango":80}
for fruit,price in prices.items():
    if price>60:
        print(f"{fruit} is expensive")
    elif price>=50:
        print(f"{fruit}is fair")
    else:
        print(f"{fruit} is cheap")