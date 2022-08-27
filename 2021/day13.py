def part1():
    with open("data.txt", "r") as f:
        lines = f.read().splitlines()
        points, folds = [], []
        for line in lines:
            if len(line) == 0:
                continue
            if "fold along" not in line:
                coords = line.split(",")
                points.append([int(coords[0]), int(coords[1])])
            else:
                i = line.split()
                folds.append(i[2])
        for i, fold in enumerate(folds):
            fold_direction, fold_place = fold.split("=")
            fold_place = int(fold_place)
            for point in points:
                if fold_direction == "x":
                    if point[0] > fold_place:
                        point[0] -= 2*(point[0]-fold_place)
                elif fold_direction == "y":
                    if point[1] > fold_place:
                        point[1] -= 2*(point[1]-fold_place)
            if i == 0:
                print("Part 1: ", len(set([(coord[0], coord[1]) for coord in points])))
    return points
      
def part2(points_list):
    width = max([x[0] for x in points_list]) + 1
    height = max([x[1] for x in points_list]) + 1
    array = []
    for y in range(height):
        array.append([" " for _ in range(width)])
    for point in points_list:
        array[point[1]][point[0]] = "█"
    for y in array:
        line = ""
        for char in y:
            line += str(char)
        print(line)
      
def main():
    points = part1()
    part2(points)

if __name__ == "__main__":
    main()
