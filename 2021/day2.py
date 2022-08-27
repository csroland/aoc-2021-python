def part1():
    depth, aim, horizontal = 0, 0, 0
    with open("data.txt", "r") as f:
        dataset = f.read().splitlines()
        for data in dataset:
            command, value = data.split()
            if command == "forward":
                horizontal += int(value)
            elif command == "down":
                depth += int(value)
            elif command == "up":
                depth -= int(value)
    print("Part 1 answer is: ", depth*horizontal)
        
def part2():
    depth, aim, horizontal = 0, 0, 0
    with open("data.txt", "r") as f:
        dataset = f.read().splitlines()
        for data in dataset:
            command = data.split()[0]
            value = int(data.split()[1])
            if command == "forward":
                horizontal += value
                depth += aim*value
            elif command == "down":
                aim += value
            elif command == "up":
                aim -= value
    print("Part 2 answer is: ", depth*horizontal)
    
def main():
    part1()
    part2()
    
if __name__ == "__main__":
    main()
