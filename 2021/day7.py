def part1():
    with open("data.txt", "r") as f:
        lines = [int(x) for x in f.read().split(",")]
        max_horizontal = max(lines)
        used_fuel_at_coord = []
        for x in range(max_horizontal+1):
            used_fuel = 0
            for data in lines:
                used_fuel += abs(x-data)
            used_fuel_at_coord.append(used_fuel)
        print("The answer for part 1:", min(used_fuel_at_coord))
    
def part2():
    with open("data.txt", "r") as f:
        lines = [int(x) for x in f.read().split(",")]
        max_horizontal = max(lines)
        used_fuel_at_coord = []
        for x in range(max_horizontal + 1):
            used_fuel = 0
            for data in lines:
                used_fuel += ((1 + abs(data-x))**2)//2
            used_fuel_at_coord.append(used_fuel)
        print("The answer for part 2:", min(used_fuel_at_coord))

def main():
    part1()
    part2()

if __name__ == "__main__":
    main()
