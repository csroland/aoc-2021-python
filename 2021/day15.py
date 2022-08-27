from queue import PriorityQueue

def get_adjacent(x, y, width, height):
    all_adjacents = [(x, y-1), (x-1, y), (x+1, y), (x, y+1)]
    adjacents = []
    for coord in all_adjacents:
        if (coord[0] >= 0 and coord[0] <= width-1 and coord[1] >= 0 and coord[1] <= height-1):
            adjacents.append(coord)
    return adjacents

def part1():
    with open("data.txt", "r") as f:
        lines = f.read().splitlines()
        risk_map = []
        for line in lines:
            risk_map.append([int(x) for x in line])
        width = len(risk_map[0])
        height = len(risk_map)
        costs = []
        for y in range(height):
            costs.append([float("inf")]*width)
        costs[0][0] = 0
        priority_queue = PriorityQueue()
        priority_queue.put((0, (0, 0)))
        visited_coords = []
        while not priority_queue.empty():
            (cost, current_coords) = priority_queue.get()
            visited_coords.append(current_coords)
            all_neighbours = get_adjacent(current_coords[0], current_coords[1], width, height)
            neighbours = [neighbour for neighbour in all_neighbours if neighbour not in visited_coords]
            for neighbour in neighbours:
                old_cost = costs[neighbour[1]][neighbour[0]]
                new_cost = costs[current_coords[1]][current_coords[0]] + risk_map[neighbour[1]][neighbour[0]]
                if new_cost < old_cost:
                    priority_queue.put((new_cost, neighbour))
                    costs[neighbour[1]][neighbour[0]] = new_cost
        return costs[-1][-1]
        
def part2():
    with open("data.txt", "r") as f:
        lines = f.read().splitlines()
        part_risk_map = []
        for line in lines:
            part_risk_map.append([int(x) for x in line])
        part_width = len(part_risk_map[0])
        part_height = len(part_risk_map)
        width = part_width * 5
        height = part_height * 5
        risk_map = []
        for y in range(height):
            risk_map.append([0]*width)
        for y, line in enumerate(risk_map):
            for x, cost in enumerate(risk_map):
                new_raw_value = (part_risk_map[y%part_height][x%part_width] + y//part_height + x//part_width)
                risk_map[y][x] = new_raw_value%10 + new_raw_value//10
        costs = []
        for y in range(height):
            costs.append([float("inf")]*width)
        costs[0][0] = 0
        priority_queue = PriorityQueue()
        priority_queue.put((0, (0, 0)))
        visited_coords = []
        while not priority_queue.empty():
            (cost, current_coords) = priority_queue.get()
            all_neighbours = get_adjacent(current_coords[0], current_coords[1], width, height)
            neighbours = [neighbour for neighbour in all_neighbours if neighbour not in visited_coords]
            for neighbour in neighbours:
                old_cost = costs[neighbour[1]][neighbour[0]]
                new_cost = cost + risk_map[neighbour[1]][neighbour[0]]
                if new_cost < old_cost:
                    priority_queue.put((new_cost, neighbour))
                    costs[neighbour[1]][neighbour[0]] = new_cost
        return costs[-1][-1]

def main():
    print(part1(), part2())
    
if __name__ == "__main__":
    main()
