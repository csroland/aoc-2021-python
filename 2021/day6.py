#def part1():
    #with open("test.txt", "r") as f:
        #fishes =[int(x) for x in f.read().rstrip().split(",")]
        #new_fishes = []
        #day = 0
        #while day < 80:
            #for index, fish in enumerate(fishes):
                #if fishes[index] != 0:
                    #fishes[index] -= 1
                #elif fishes[index] == 0:
                    #fishes[index] = 6
                    #new_fishes.append(8)
            #fishes.extend(new_fishes)
            #new_fishes.clear()
            #day += 1
            
def part_1_and_2(length):
    fish_age = {x:0 for x in range(9)}
    day = 0
    with open("data.txt", "r") as f:
        fishes = [int(x) for x in f.read().rstrip().split(",")]
        day = 0
        for fish in fishes:
            fish_age[fish] = fish_age.get(fish, 0) + 1
        while day < length:
            new_fish, old_fish = 0, 0
            for age in range(9):
                if age == 0:
                    new_fish = fish_age[0]
                    old_fish = fish_age[0]
                    fish_age[0] = 0
                else:
                    fish_age[age-1] += fish_age[age]
                    fish_age[age] = 0
            fish_age[8] += new_fish
            fish_age[6] += old_fish
            day += 1
        print("The total number of lanternfish:", sum(fish_age.values()))

def main():
    part_1_and_2(80)
    part_1_and_2(256)


if __name__ == "__main__":
    main()
    
