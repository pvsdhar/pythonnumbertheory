a = int(input("Enter a natural number:"))
b = input("Type E for even numbers and O for odd numbers.")
if b == "E" or b == "e":
    for a in range(1,(a+1)):
        if a%2 == 0:
            print(a)
elif b == "O" or b == "o":
    for a in range(1,(a+1)):
        if a%2 == 1:
            print(a)


