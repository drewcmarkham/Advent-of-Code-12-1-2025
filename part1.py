with open("rotations.txt") as rotations:
    items = [line.strip() for line in rotations]

totalValue = 50
password = 0

for x in items:
    direction = x[0]
    value = int(x[1:])
    if direction == "R":
        totalValue += value
    elif direction == "L":
        totalValue -= value
    else:
        print("Error in getting direction")

    totalValue %= 100

    if totalValue == 0:
        password += 1

print (password)