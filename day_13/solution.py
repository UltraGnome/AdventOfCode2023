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
            line1 = rows[:r][::-1]
            line2 = rows[r:]

            line1 = line1[:len(line2)]
            line2 = line2[:len(line1)]

            if line1 == line2:
                result = r
                return result
        return result


class Part2:
    @staticmethod
    def solution(file_lines: list[str]) -> int:
        """

        Args:
            file_lines: List of lines from input file

        Returns:

        """
        return 0


with open("input.txt", "r") as file:
    f = file.read()

print(f"Part 1: {Part1.solution(f)}")
# print(f"Part 2: {Part2.solution(f)}")
