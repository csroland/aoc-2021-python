from collections import Counter

def insertion(polymer, polymer_rules):
    new_polymer = [char for char in polymer]
    insertions = 0
    for i in range(len(polymer)-1):
        if polymer[i]+polymer[i+1] in polymer_rules.keys():
            new_polymer.insert(i+insertions+1, polymer_rules[polymer[i]+polymer[i+1]])
            insertions += 1
    new_polymer_string = ""
    for char in new_polymer:
        new_polymer_string += char
    return new_polymer_string

def part1():
    with open("data.txt", "r") as f:
        lines = f.read().splitlines()
        polymer = ""
        poly_rules = {}
        for line in lines:
            if line != "":
                if "->" in line:
                    start, end = line.split(" -> ")
                    poly_rules[start] = end
                else:
                    polymer = line
        for cycle in range(10):
            polymer = insertion(polymer, poly_rules)
        poly_values = Counter(polymer).values()
        print(max(poly_values)-min(poly_values))

def part2():
    with open("data.txt", "r") as f:
        lines = f.read().splitlines()
        polymer = ""
        polymer_dict = {}
        element_count = {}
        poly_rules = {}
        for line in lines:
            if line != "":
                if "->" in line:
                    start, end = line.split(" -> ")
                    poly_rules[start] = end
                else:
                    polymer = line
        for i in range(len(polymer)-1):
            element_count[polymer[i]] = element_count.get(polymer[i],0) + 1
            polymer_dict[polymer[i]+polymer[i+1]] = polymer_dict.get(polymer[i]+polymer[i+1], 0) + 1
        element_count[polymer[-1]] = element_count.get(polymer[-1],0) + 1
        for cycle in range(40):
            polymer_dict_copy = polymer_dict.copy()
            for pair in polymer_dict_copy.keys():
                if pair in poly_rules.keys():
                    count = polymer_dict_copy[pair]
                    polymer_dict[pair] -= count
                    new_poly = insertion(pair, poly_rules)
                    polymer_dict[new_poly[0:2]] = polymer_dict.get(new_poly[0:2], 0) + count
                    polymer_dict[new_poly[1:3]] = polymer_dict.get(new_poly[1:3], 0) + count
                    element_count[new_poly[1]] = element_count.get(new_poly[1], 0) + count
        print(max(element_count.values())-min(element_count.values()))

def main():
    part1()
    part2()

if __name__ == "__main__":
    main()
