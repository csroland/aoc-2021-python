def is_low_point(x, y, width, height, data_table):
    all_adjacents = [(x, y-1), (x-1, y), (x+1, y), (x, y+1)]
    adjacents = []
    is_lower = []
    for coord in all_adjacents:
        if (coord[0] >= 0 and coord[0] <= width-1 and coord[1] >= 0 and coord[1] <= height-1):
            adjacents.append(coord)
    for coord in adjacents:
        if data_table[coord[1]][coord[0]] <= data_table[y][x]:
            return False
    return True

def flood_fill(x, y, width, height, data_table, visited_points, basin_size):
    visited_points.append((x, y))
    all_adjacents = [(x, y-1), (x+1, y), (x, y+1), (x-1, y)]
    adjacents = []
    diff = 0
    for coord in all_adjacents:
        if (coord[0] >= 0 and coord[0] <= width-1 and coord[1] >= 0 and coord[1] <= height-1):
            adjacents.append(coord)
    for coord in adjacents:
        if data_table[coord[1]][coord[0]] != 9 and coord not in visited_points:
            diff += flood_fill(coord[0], coord[1], width, height, data_table, visited_points, basin_size)
    return diff + 1

def part_1_and_2():
    with open("data.txt", "r") as f:
        lines = f.read().splitlines()
        data = [] #data[y][x]
        for line in lines:
            data.append([int(char) for char in line])
        height = len(data)
        width = len(data[0])
        risk_levels = {}
        for y, line in enumerate(data):
            for x, lava_tube_height in enumerate(line):
                if is_low_point(x, y, width, height, data):
                    risk_levels[(x, y)] = lava_tube_height + 1
        print("The answer for part 1", sum(risk_levels.values()))
        basins = []
        for coord in risk_levels:
            basins.append(flood_fill(coord[0], coord[1], width, height, data, [], 1))
        basins.sort(reverse = True)
        print("The answer for part 2:", basins[0]*basins[1]*basins[2])

def main():
    part_1_and_2()
    
if __name__ == "__main__":
    main()
