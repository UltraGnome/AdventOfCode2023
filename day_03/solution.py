from collections import Counter
class Part_Number(object):
    def __init__(self, part_no, row, start_index, end_index):
        self.part_no = part_no
        self.row = row
        self.start_index = start_index
        self.end_index = end_index
        self.gear_matches = ""

    def get_gear_matches(self):
        return self.gear_matches

    def set_gear_matches(self, gear_id):
        self.gear_matches = gear_id

class Symbol(object):
    def __init__(self, row, index, char):
        self.row = row
        self.index = index
        self.char = char




class Part1:
    @staticmethod
    def solution(file_lines: list[str]) -> int:
        result = 0
        row = 0
        part_numbers = []
        symbols = []


        for line in file_lines:
            line = line.strip()
            line = line.rstrip('\n')
            line = line.rstrip('\r')
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
            if part.end_index < 140:
                end_idx = part.end_index + 1
            else:
                end_idx = part.end_index
            symbol_matches_by_row = [s for s in symbols if s.row in(start,start3,start2)]
            symbol_matches_by_index = [s for s in symbol_matches_by_row if s.index >= idx and s.index <= end_idx]
            if symbol_matches_by_index:
                # print("found: " + str(part.part_no))
                result += part.part_no
                gear_symbol_matches = [s for s in symbol_matches_by_index if s.char.strip() == '*' ]
                for gear in gear_symbol_matches:
                    part.set_gear_matches(str(gear.row) + str(gear.index))



        parts_with_one_gear = [s for s in part_numbers if len(s.gear_matches) > 0 ]
        howdy = {}

        stupid_gear_answer = 0

        for x in parts_with_one_gear:
            if(x.gear_matches) in howdy:
                howdy[x.gear_matches].append(x.part_no)
                foo = howdy[x.gear_matches][0] * howdy[x.gear_matches][1]
                stupid_gear_answer += foo
            else:
                howdy[x.gear_matches]=[x.part_no]




        return result

    @staticmethod
    def parse_line_into_symbols_and_part_numbers(line, part_no_str, part_numbers, row, symbols):
        line = line.rstrip('\n')
        for i, char in enumerate(line):
            if char.strip() != '.' and char.strip().isdigit() is False:
                symbol = Symbol(row, i, char)
                symbols.append(symbol)
                # print(str(i) + " - " + symbol.char + " " + str(symbol.row) + " " + str(symbol.index))
                part_no_str = Part1.add_part_number(i, part_no_str, part_numbers, row)
            elif char.strip().isdigit():
                part_no_str += char
            elif char.strip() == '.':
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
        result = 0
        row = 0
        part_numbers = []
        symbols = []
        for line in file_lines:
            line = line.strip()
            line = line.rstrip('\n')
            line = line.rstrip('\r')
            row += 1
            part_no_str = ""
            Part1.parse_line_into_symbols_and_part_numbers(line, part_no_str, part_numbers, row, symbols)



        return 0


with open('input.txt') as filey:
    f = [line.rstrip() for line in filey]



print(f"Part 1: {Part1.solution(f)}")
# print(f"Part 2: {Part2.solution(f)}")



