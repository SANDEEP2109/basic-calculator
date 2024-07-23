def addition():
    a = []
    b = int(input("How many numbers should be added: "))
    for i in range(b):
        c = float(input(f"Enter the value {i + 1} : "))
        a.append(c)
    result = sum(a)
    print(f"addition of all numbers is {result}")

def subraction():
    numbers = []
    entry = int(input("How many numbers: "))
    for i in range(entry):
        inp = float(input(f"Enter the value {i + 1} : "))
        numbers.append(inp)
    diff = numbers[0]
    for i in range(1, len(numbers)):
        diff = diff - numbers[i]
    print(f"Subraction of all numbers is {diff}")

def multiplication():
    mul = []
    number_of = int(input("How many numbers: "))
    for i in range(number_of):
        take = float(input(f"Enter the value {i+1} : "))
        mul.append(take)

    mult = mul[0]
    for i in range(1, len(mul)):
        mult = mult * mul[i]

    print(f"multiplication of all numbers is {mult}")

print("**********CALCULATOR**********")
while True:
    print("1) Addition")
    print("2) Subraction")
    print("3) Multiplication")
    print("4) Exit")
    choice = int(input("Enter the option: "))
    if choice == 1:
        addition()

    elif choice == 2:
        subraction()

    elif choice == 3:
        multiplication()

    elif choice == 4:
        break

    else:
        print("Invalid option")

