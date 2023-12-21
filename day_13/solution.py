class Part1:
    @staticmethod
    def solution(file_contents) -> int:
        """
            get rows
            get cols
            traverse, comparing n to n+1


        """
        valley_of_mirrors_patterns = file_contents.split('\n\n')

        result = 0
        for pattern in valley_of_mirrors_patterns:
            valley_of_mirrors_map: object = pattern.splitlines()
            rows = []
            cols = []
            for row in valley_of_mirrors_map:
                rows.append(row)

            result += (Part1.find_reflection_padding(rows) * 100)

            for column in list(zip(*valley_of_mirrors_map)):
                cols.append(''.join(column))

            result += (Part1.find_reflection_padding(cols))

        return result

    @staticmethod
    def find_reflection_padding(rows):
        result = 0
        for r in range(1, len(rows)):
            line1 = rows[:r][::-1]  #::-1 means start at the end
            line2 = rows[r:]

            line1 = line1[:len(line2)]
            line2 = line2[:len(line1)]

            if line1 == line2:
                result = r
                return result
        return result


class Part2:

    def find_smudge_padding(grid):
        for i in range(1, len(grid)):
            line1 = grid[:i][::-1]
            line2 = grid[i:]
    
            total_mismatches = 0
            for top_row, bottom_row in zip(line1, line2):
                for (top_char, bottom_char) in zip(top_row, bottom_row):
                    if top_char != bottom_char:
                        total_mismatches += 1
            # we only want the pairs with one mismatch
            if total_mismatches == 1:
                return i
    
        return 0
    
    
    @staticmethod
    def solution(file_contents) -> int:
        valley_of_mirrors_patterns = file_contents.split('\n\n')

        result = 0
        for pattern in valley_of_mirrors_patterns:
            grid = pattern.splitlines()

            row_index = Part2.find_smudge_padding(grid)
            result += row_index * 100

            transposed_grid = list(zip(*grid))
            column_index = Part2.find_smudge_padding(transposed_grid)
            result += column_index

        return result


with open("input.txt", "r") as file:
    f = file.read()

# print(f"Part 1: {Part1.solution(f)}")
print(f"Part 2: {Part2.solution(f)}")
