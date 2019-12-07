
def calculate_fuel(input) -> int:
    tmp = (input // 3) - 2
    if tmp <= 0:
        return 0
    else:
        return tmp + calculate_fuel(tmp)


with open("./input.txt") as f:
    masses = f.readlines()

masses = [int(x.strip()) for x in masses]

fuel = 0
for mass in masses:
    fuel += calculate_fuel(mass)
       
print(fuel)