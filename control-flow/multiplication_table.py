n = int(input("Enter a number to see its multiplication table:"))


for i in range(1, 11):
    prod = n * i
    print(f"{n} * {i} = {prod}")
