WON = False

class BingoTable:
    def __init__(self, lines):
        self.table = []
        if len(lines) == 5:
            for line in lines:
                self.table.append([int(x) for x in line.split(" ") if x != ""])
        self.chosen_table = [[0, 0, 0, 0, 0] for _ in range(5)]
        self.already_won = False
        
    def check_chosen(self, chosen_num):
        if not self.already_won:
            for y, row in enumerate(self.table):
                for x, number in enumerate(row):
                    if number == chosen_num:
                        self.chosen_table[y][x] = 1
            if self.check_winning():
                self.already_won = True
                winning_sum = 0
                for y in range(5):
                    for x in range(5):
                        if self.chosen_table[y][x] == 0:
                            winning_sum += self.table[y][x]
                return winning_sum*chosen_num
        return False

    def check_winning(self):
        for y, row in enumerate(self.chosen_table):
            if sum(self.chosen_table[y]) == 5:
                return True
        for x in range(5):
            column = [self.chosen_table[y][x] for y in range(5)]
            if sum(column) == 5:
                return True
        return False


def check_winners(win_numbers, bingo_tables):
    results = []
    for num in win_numbers:
        for table in bingo_tables:
            value = table.check_chosen(num)
            if value != False:
                results.append(result)
    return results

def main():
    with open("data.txt", "r") as f:
        lines = f.read().splitlines()
        win_numbers = []
        bingo_tables = []
        table_lines = []
        for data in lines:
            if len(data) > 15:
                win_numbers = [int(x) for x in data.split(",")]
            elif len(data) == 14:
                table_lines.append(data)
            if len(table_lines) == 5:
                bingo_tables.append(BingoTable(table_lines))
                table_lines.clear()
        winning_tables = check_winners(win_numbers, bingo_tables)
        print("The answer for part 1:", winning_tables[0])
        print("The answer for part 2:", winning_tables[-1])

if __name__ == "__main__":
    main()
