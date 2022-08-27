from collections import Counter

all_paths = []

def part_1_and_2():
    global all_paths
    with open("data.txt", "r") as f:
        lines = f.read().splitlines()
        connections = {}
        for line in lines:
            start, end = line.split("-")
            if start in connections.keys():
                connections[start].append(end)
            else:
                connections[start] = [end]
            if end in connections.keys():
                connections[end].append(start)
            else:
                connections[end] = [start]
        paths_from_point("start", [], [], connections, 0)
        part1_ans = len(all_paths)
        all_paths.clear()
        paths_from_point2("start", [], [], connections, 0)
        part2_ans = len(all_paths)
        print(" Part 1: ", part1_ans, "\n", "Part 2: ", part2_ans)
        
def paths_from_point(point, path, visited_points, connections, counter):
    path.append(point)
    global all_paths
    counter += 1
    if point == "end":
        all_paths.append(path)
    else:
        if point.islower():
            visited_points.append(point)
        destinations = connections[point]
        for dest in destinations:
            if not (dest.islower() and dest in path):
                paths_from_point(dest, path, visited_points, connections, counter)
        if point.islower():
            visited_points.remove(point)
    path.pop()
    
def paths_from_point2(point, path, visited_points, connections, counter):
    path.append(point)
    global all_paths
    counter += 1
    if point == "end":
        all_paths.append(path)
    else:
        destinations = connections[point]
        if "start" in destinations:
            destinations.remove("start")
        path_occur = Counter(path)
        for dest in destinations:
            if dest.islower():
                if any([path_occur[x]==2 for x in path_occur.keys() if x.islower()]):
                    if dest not in path:
                        paths_from_point2(dest, path, visited_points, connections, counter)
                else:
                    paths_from_point2(dest, path, visited_points, connections, counter)
            else:
                paths_from_point2(dest, path, visited_points, connections, counter)
    path.pop()

def main():
    part_1_and_2()
    
if __name__ == "__main__":
    main()
