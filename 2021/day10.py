def part_1_and_2():
    with open("data.txt", "r") as f:
        lines = f.read().splitlines()
        data = []
        for line in lines:
            data.append([char for char in line])
        chunk_start_char = ("<", "(", "[", "{")
        chunk_end_char = (">", ")", "]", "}")
        pairs = [("<", ">"),("(", ")"),("[", "]"),("{", "}")]
        syntax_error_points = 0
        uncorrupted_lines = []
        for line in data:
            start_char = ["0"] * len(line)
            end_char = ["0"] * len(line)
            for char in line:
                if char in chunk_start_char:
                    start_char[start_char.index("0")] = char
                elif char in chunk_end_char:
                    index = start_char.index("0") - 1
                    while end_char[index] != "0":
                        index -= 1
                    end_char[index] = char
            corrupted = False
            for i, char in enumerate(start_char):
                if (char, end_char[i]) not in pairs and end_char[i] != "0":
                    if end_char[i] == ")":
                        syntax_error_points += 3
                    elif end_char[i] == "]":
                        syntax_error_points += 57
                    elif end_char[i] == "}":
                        syntax_error_points += 1197
                    elif end_char[i] == ">":
                        syntax_error_points += 25137
                    corrupted = True
            if not corrupted:
                uncorrupted_lines.append(line)
        print("Part 1:", syntax_error_points)
        completion = []
        for line in uncorrupted_lines:
            start_char = ["0"] * len(line)
            end_char = ["0"] * len(line)
            completion_chars = ""
            for char in line:
                if char in chunk_start_char:
                    start_char[start_char.index("0")] = char
                elif char in chunk_end_char:
                    index = start_char.index("0") - 1
                    while end_char[index] != "0":
                        index -= 1
                    end_char[index] = char
            for index, char in enumerate(reversed(start_char)):
                if char in chunk_start_char and end_char[-index-1] == "0":
                    completion_chars += char
            completion.append(completion_chars)
        auto_complete_points = []
        for string in completion:
            points = 0
            chars = [char for char in string]
            for char in chars:
                points = points * 5
                if char == "(":
                    points += 1
                elif char == "[":
                    points += 2
                elif char == "{":
                    points += 3
                elif char == "<":
                    points += 4
            auto_complete_points.append(points)
        auto_complete_points.sort()
        print("Part 2:", auto_complete_points[len(auto_complete_points)//2])

def main():
    part_1_and_2()
    
if __name__ == "__main__":
    main()
