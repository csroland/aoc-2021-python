def part1():
    with open("data.txt", "r") as f:
        lines = [int(x) for x in f.read().splitlines()]
        larger_count, prev_line = 0, 0
        is_first = True
        for index, line in enumerate(lines):
            line = int(line)
            if is_first:
                prev_line = line
                is_first = False
            else:
                if line > prev_line:
                    larger_count += 1
                    prev_line = line
                else:
                    prev_line = line
        print("Part1 solution: ", larger_count)
    
def part2():
    with open("data.txt", "r") as f:
        lines = [int(x) for x in f.read().splitlines()]
        larger_count, prev_line = 0, 0
        is_first = True
        for index, line in enumerate(lines):
            line = int(line)
            if index == len(lines)-2:
                break
            if is_first:
                prev_line = line + lines[index+1] + lines[index+2]
                is_first = False
            else:
                if (line + lines[index+1] + lines[index+2]) > prev_line:
                    larger_count += 1
                    prev_line = (line + lines[index+1] + lines[index+2])
                else:
                    prev_line = (line + lines[index+1] + lines[index+2])
        print("Part2 solution: ", larger_count)

def main():
    part1()
    part2()
    
if __name__ == "__main__":
    main()
