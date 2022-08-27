
def part1():
    with open("data.txt", "r") as f:
        lines = f.read().splitlines()
        renders = []
        outputs = []
        for line in lines:
            line_split = line.split("|")
            renders.append(line_split[0])
            outputs.append(line_split[1])
        unique_digits = 0
        for data in outputs:
            digits = data.split()
            for digit in digits:
                if len(digit) in [2, 3, 4, 7]:
                    unique_digits += 1
        print("The answer for part 1:", unique_digits)
        
def part2():
    with open("data.txt", "r") as f:
        lines = f.read().splitlines()
        sum_output = 0
        for line in lines:
            line_split = line.split("|")
            known_numbers = {}
            display_segments = {}
            digits = line_split[0].split()
            digits.sort(key = len)
            for digit in digits:
                digit_chars = [char for char in digit]
                if len(digit) == 2:
                    display_segments[1] = digit_chars
                    display_segments[4] = digit_chars
                if len(digit) == 3:
                    display_segments[0] = [char for char in digit_chars if char not in display_segments[1]]
                if len(digit) == 4:
                    display_segments[2] = [char for char in digit_chars if char not in display_segments[1]]
                    display_segments[3] = [char for char in digit_chars if char not in display_segments[1]]
                if len(digit) == 7:
                    display_segments[5] = []
                    display_segments[6] = []
                    for char in digit_chars:
                        if char not in display_segments[0] and char not in display_segments[1] and char not in display_segments[2] and char not in display_segments[3] and char not in display_segments[4]:
                            display_segments[5].append(char)
                            display_segments[6].append(char)
            for digit in digits:
                digit_chars = [char for char in digit]
                if len(digit) == 5:
                    if all(char in digit_chars for char in display_segments[1]):
                        for char in digit_chars:
                            if char in display_segments[3]:
                                display_segments[3] = [char]
                                display_segments[2].remove(char)
                            if char in display_segments[6]:
                                display_segments[6] = [char]
                                display_segments[5].remove(char)
            for digit in digits:
                digit_chars = [char for char in digit]
                if len(digit) == 6:
                    if not all(char in digit_chars for char in display_segments[4]):
                        for char in digit_chars:
                            if char in display_segments[4]:
                                display_segments[4] = [char]
                                display_segments[1].remove(char)
            for digit in digits:
                digit_chars = [char for char in digit]
                if len(digit_chars) == 2:
                    known_numbers[1] = sorted(digit_chars)
                elif len(digit_chars) == 3:
                    known_numbers[7] = sorted(digit_chars)
                elif len(digit_chars) == 4:
                    known_numbers[4] = sorted(digit_chars)
                elif len(digit_chars) == 7:
                    known_numbers[8] = sorted(digit_chars)
                elif len(digit_chars) == 5:
                    number_5 = display_segments[0] + display_segments[2] + display_segments[3] + display_segments[4] + display_segments[6]
                    number_2 = display_segments[0] + display_segments[1] + display_segments[3] + display_segments[5] + display_segments[6]
                    number_3 = display_segments[0] + display_segments[1] + display_segments[3] + display_segments[4] + display_segments[6]
                    if all(char in number_5 for char in digit_chars):
                        known_numbers[5] = sorted(digit_chars)
                    if all(char in number_2 for char in digit_chars):
                        known_numbers[2] = sorted(digit_chars)
                    if all(char in number_3 for char in digit_chars):
                        known_numbers[3] = sorted(digit_chars)
                elif len(digit_chars) == 6:
                    number_0 = display_segments[0] + display_segments[1] + display_segments[2] + display_segments[4] + display_segments[5] + display_segments[6]
                    number_6 = display_segments[0] + display_segments[2] + display_segments[3] + display_segments[4] + display_segments[5] + display_segments[6]
                    number_9 = display_segments[0] + display_segments[1] + display_segments[2] + display_segments[3] + display_segments[4] + display_segments[6]
                    if all(char in number_0 for char in digit_chars):
                        known_numbers[0] = sorted(digit_chars)
                    if all(char in number_6 for char in digit_chars):
                        known_numbers[6] = sorted(digit_chars)
                    if all(char in number_9 for char in digit_chars):
                        known_numbers[9] = sorted(digit_chars)
            output = line_split[1].split()
            solution_string = ""
            for number in output:
                number_chars = sorted([char for char in number])
                for key in known_numbers:
                    if number_chars == known_numbers[key]:
                        solution_string += str(key)
            sum_output += int(solution_string)
        print("The answer for part 2:", sum_output)

def main():
    part1()
    part2()

if __name__ == "__main__":
    main()
