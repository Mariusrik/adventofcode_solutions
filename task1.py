
def calculate_fuel(input, total) -> int:
    tmp = (input // 3) - 2
    if tmp <= 0:
        return total
    else:
        return calculate_fuel(tmp, total + tmp)


with open("./input.txt") as f:
    masses = f.readlines()

masses = [int(x.strip()) for x in masses]

fuel = 0
for mass in masses:
    fuel += calculate_fuel(mass, 0)
       
print(fuel)