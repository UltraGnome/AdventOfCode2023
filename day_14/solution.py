from functools import cache
class Part1:
    @staticmethod
    def solution(file) -> int:
        stone_map: object = file.splitlines()
        result = 0

        cols = []

        for column in list(zip(*stone_map)):
            cols.append(''.join(column))

        i = 0
        for col in cols:
            i += 1
            print(str(i) + " " + col + '\n')
            col=Part1.bubble_sort(list(col))
            print("sorted:  " + str(i) + " " + "".join(col) + '\n')
            result += Part1.score_column(col)

        return result
    @staticmethod
    def bubble_sort(sequence):
        n = len(sequence)
        for i in range(n-1):
            for j in range(n-i-1):
                if(sequence[j]=='.' and sequence[j+1]=='O'):
                    sequence[j+1], sequence[j] = sequence[j], sequence[j+1]
        return sequence

    @staticmethod
    def score_column(sequence):
        row_score = len(sequence)
        score = 0
        for i in range(row_score):
            if sequence[i] == 'O':
                score += row_score - i

        return score


class Part2:
    @staticmethod
    def solution(file_contents) -> int:
        rock_map = tuple(file_contents.splitlines())
        for i in range(1_000_000_000 // 1000):
            rock_map = Part2.thousand_cycles(rock_map)

        return Part2.calculate_load(rock_map)

    @cache
    def move_north(rock_map: tuple[str]) -> tuple[str]:
        rock_map = list(rock_map)
        for y, row in enumerate(rock_map):
            for x, char in enumerate(row):
                if char != 'O':  # skip non-moving rocks
                    continue
                obstacles_y = [y for y in range(y) if rock_map[y][x] in '#O']
                new_y = max(obstacles_y, default=-1) + 1
                if new_y != y:
                    rock_map[y] = rock_map[y][:x] + '.' + rock_map[y][x+1:]
                    rock_map[new_y] = rock_map[new_y][:x]+'O'+rock_map[new_y][x+1:]
        return tuple(rock_map)


    @cache
    def turn_clockwise(rock_map: tuple[str]) -> tuple[str]:
        return tuple(''.join(row) for row in zip(*rock_map[::-1]))


    @cache
    def thousand_cycles(rock_map: tuple[str]) -> tuple[str]:
        for _ in range(4 * 1000):
            rock_map = Part2.move_north(rock_map)
            rock_map = Part2.turn_clockwise(rock_map)
        return rock_map


    def calculate_load(rock_map: tuple[str]) -> int:
        height = len(rock_map)
        return sum(row.count('O') * (height - y) for y, row in enumerate(rock_map))



with open("input.txt", "r") as file:
    f = file.read()



# print(f"Part 1: {Part1.solution(f)}")
print(f"Part 2: {Part2.solution(f)}")



