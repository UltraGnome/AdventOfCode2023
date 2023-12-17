class Part1:
    @staticmethod
    def solution(file_lines: list[str]) -> int:
        result = 0
        galaxy_map = [list(line) for line in file_lines]

        empty_rows = [i for i, row in enumerate(
            galaxy_map) if all(char == '.' for char in row)]

        empty_cols = [i for i, col in enumerate(zip(*galaxy_map)) if all(
            char == '.' for char in col)]

        galaxies = [(row, col) for row, line in enumerate(galaxy_map)
                    for col, char in enumerate(line) if char == '#']

        for i, (galaxy_row, galaxy_col) in enumerate(galaxies):
            for (other_galaxy_row, other_galaxy_col) in galaxies[:i]:
                for row in range(min(other_galaxy_row, galaxy_row), max(other_galaxy_row, galaxy_row)):
                    result += 2 if row in empty_rows else 1

                for col in range(min(other_galaxy_col, galaxy_col), max(other_galaxy_col, galaxy_col)):
                    result += 2 if col in empty_cols else 1
        return result

class Part2:
    @staticmethod
    def solution(file_lines: list[str]) -> int:
        result = 0
        empty_rows = [r for r, row in enumerate(file_lines) if all(ch == "." for ch in row)]
        empty_cols = [c for c, col in enumerate(zip(*file_lines)) if all(ch == "." for ch in col)]

        points = [(r, c) for r, row in enumerate(file_lines) for c, ch in enumerate(row) if ch == "#"]


        scale = 1000000

        for i, (r1, c1) in enumerate(points):
            for (r2, c2) in points[:i]:
                for r in range(min(r1, r2), max(r1, r2)):
                    result += scale if r in empty_rows else 1
                for c in range(min(c1, c2), max(c1, c2)):
                    result += scale if c in empty_cols else 1
        return result


with open("input.txt", "r") as file:
    f = file.read().splitlines()

# print(f"Part 1: {Part1.solution(f)}")
print(f"Part 2: {Part2.solution(f)}")



