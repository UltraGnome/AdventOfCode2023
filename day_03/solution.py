class Part_Number(object):
    def __init__(self, part_no, row, start_index, end_index):
        self.part_no = part_no
        self.row = row
        self.start_index = start_index
        self.end_index = end_index

class Symbol(object):
    def __init__(self, row, index):
        self.row = row
        self.index = index


class Part1:
    @staticmethod
    def solution(file_lines: list[str]) -> int:
        result = 0
        row = 0
        part_numbers = []
        symbols = []

        for line in file_lines:
            row += 1
            part_no_str = ""
            Part1.parse_line_into_symbols_and_part_numbers(line, part_no_str, part_numbers, row, symbols)

        for part in part_numbers:
            start = part.row - 1
            start2 = part.row
            start3 = part.row + 1
            idx = 0
            if part.start_index > 0:
               idx = part.start_index - 1
            end_idx = part.end_index + 1
            symbol_matches_by_row = [s for s in symbols if s.row in(start,start3,start2)]
            symbol_matches_by_index = [s for s in symbol_matches_by_row if s.index >= idx and s.index <= end_idx]
            if symbol_matches_by_index:
                result += part.part_no

        return result

    @staticmethod
    def parse_line_into_symbols_and_part_numbers(line, part_no_str, part_numbers, row, symbols):
        for i, char in enumerate(line):
            if char != '.' and char.isdigit() is False:
                symbol = Symbol(row, i)
                symbols.append(symbol)
                part_no_str = Part1.add_part_number(i, part_no_str, part_numbers, row)
            elif char.isdigit():
                part_no_str += char
            elif char == '.':
                part_no_str = Part1.add_part_number(i, part_no_str, part_numbers, row)
            else:
                print("hi unexpected char:" + char)

    @staticmethod
    def add_part_number(end_index, part_no_str, part_numbers, row):
        if len(part_no_str) > 0:
            start_index = int(end_index) - int(len(part_no_str))
            end_index = end_index - 1
            part_number = Part_Number(int(part_no_str), row, start_index, end_index)
            part_numbers.append(part_number)
            part_no_str = ""
        return part_no_str


class Part2:
    @staticmethod
    def solution(file_lines: list[str]) -> int:

        return 0


with open("input.txt", "r") as file:
    f = file.read().splitlines()

print(f"Part 1: {Part1.solution(f)}")
# print(f"Part 2: {Part2.solution(f)}")



