def part1():
    with open("data.txt", "r") as f:
        lines = f.read().splitlines()
        covered_positions = {}
        for line in lines:
            data = line.split(" -> ")
            x1 = int(data[0].split(",")[0])
            y1 = int(data[0].split(",")[1])
            x2 = int(data[1].split(",")[0])
            y2 = int(data[1].split(",")[1])
            if x1 == x2:
                if y1 > y2:
                    y1, y2 = y2, y1
                for y in range(y1, y2 + 1):
                    covered_positions[(x1, y)] = covered_positions.get((x1, y), 0) + 1
            elif y1 == y2:
                if x1 > x2:
                    x1, x2 = x2, x1
                for x in range(x1, x2 + 1):
                    covered_positions[(x, y1)] = covered_positions.get((x, y1), 0) + 1
        intersects = 0
        for data in covered_positions.values():
            if data >= 2:
                intersects += 1
        print("Number of intersects: ", intersects)
        
def part2():
    with open("data.txt", "r") as f:
        lines = f.read().splitlines()
        covered_positions = {}
        for line in lines:
            data = line.split(" -> ")
            x1 = int(data[0].split(",")[0])
            y1 = int(data[0].split(",")[1])
            x2 = int(data[1].split(",")[0])
            y2 = int(data[1].split(",")[1])
            if x1 > x2:
                x_coords = range(x1, x2 - 1, -1)
            else:
                x_coords = range(x1, x2 + 1)
            if y1 > y2:
                y_coords = range(y1, y2 - 1, -1)
            else:
                y_coords = range(y1, y2 + 1)
            if len(y_coords) == 1:
                for x in x_coords:
                    covered_positions[(x, y_coords[0])] = covered_positions.get((x, y_coords[0]), 0) + 1
            elif len(x_coords) == 1:
                for y in y_coords:
                    covered_positions[(x_coords[0], y)] = covered_positions.get((x_coords[0], y), 0) + 1
            else:
                for i, x in enumerate(x_coords):
                    covered_positions[(x, y_coords[i])] = covered_positions.get((x, y_coords[i]), 0) + 1
        intersects = sum([1 for data in covered_positions.values() if data >= 2])
        print("Number of intersects: ", intersects)

def main():
    part1()
    part2()

if __name__ == "__main__":
    main()
