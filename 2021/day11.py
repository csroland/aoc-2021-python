def get_adjacent(x,y, width, height):
    all_adjacents = [(x-1, y-1), (x, y-1), (x+1, y-1), (x-1, y), (x+1, y), (x-1, y+1), (x, y+1), (x+1, y+1)]
    adjacents = []
    for coord in all_adjacents:
        if (coord[0] >= 0 and coord[0] <= width-1 and coord[1] >= 0 and coord[1] <= height-1):
            adjacents.append(coord)
    return adjacents

def part1():
    with open("data.txt", "r") as f:
        lines = f.read().splitlines()
        data = []
        for line in lines:
            data.append([int(char) for char in line])
        height, width = len(data), len(data[0])
        flashed = []
        [flashed.append([0] * width) for _ in range(height)]
        turns = 0
        octopus_flashes = 0
        all_flashed = False
        while not all_flashed:
            data_sum = 0
            for x, line in enumerate(data):
                for y, flash_level in enumerate(line):
                    data_sum += flash_level
            if data_sum == 0:
                print("all flashed after: ", turns)
                all_flashed = True
                break
            for x, line in enumerate(data):
                for y, flash_level in enumerate(line):
                    data[y][x] += 1
            new_flash = True
            for x, line in enumerate(flashed):
                for y, flash in enumerate(line):
                    flashed[y][x] = 0
            while new_flash:
                new_flash = False
                for y, line in enumerate(data):
                    for x, flash_level in enumerate(line):
                        if flash_level > 9 and flashed[y][x] == 0:
                            new_flash = True
                            flashed[y][x] = 1
                            octopus_flashes += 1
                            adjacents = get_adjacent(x, y, width, height)
                            for coords in adjacents:
                                data[coords[1]][coords[0]] += 1
            for x, line in enumerate(flashed):
                for y, flash in enumerate(line):
                    if flash == 1:
                        data[x][y] = 0
            turns += 1
            if turns == 100:
                print(octopus_flashes)

def main():
    part1()

if __name__ == "__main__":
    part1()
