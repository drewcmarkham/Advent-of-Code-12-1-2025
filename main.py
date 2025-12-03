with open("rotations.txt") as rotations:
    items = [line.strip() for line in rotations]

for x in items:
    direction = x[0]
    value = x[1:]
    print(value)