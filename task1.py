with open("./input.txt") as f:
    content = f.readlines()

content = [int(x.strip()) for x in content]

fuel = 0
for i in content:
    fuel += int(i / 3) - 2
       
print(fuel)

