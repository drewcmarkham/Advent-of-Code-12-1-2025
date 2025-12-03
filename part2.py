with open("rotations.txt") as rotations:
    items = [line.strip() for line in rotations]
#  items = ["R10", "L20", "R30", "L40", "R50", "L60", "L30", 'R70', 'L40', 'L20', 'R80', 'R200', 'L180', 'R0', 'L8']
# # #         60,    40,    70,    30,    80,    20,     90,   60,     20,    0,     80   80      0    0     92
# # #          0      0      0      0      0      0       1     2      2      3      3     5      7     8     8
totalValue = 50
password = 0

for x in items:

    direction = x[0]
    value = int(x[1:])
    temp = totalValue

    loops = value // 100 
    remainder = value % 100

    if direction == "R":
        totalValue += value
    elif direction == "L":
        totalValue -= value
    else:
        print("Error in getting direction")
    

    if direction == "R":
        if (temp + remainder) >= 100:
            password += 1
    elif direction == "L":
        if (temp - remainder) <= 0:
            password += 1

    totalValue %= 100
    # if (totalValue == 0):
    #     password += 1  #<-- double counts?
    password += loops

print (password)