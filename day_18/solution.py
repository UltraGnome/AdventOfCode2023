class Part1:
    @staticmethod
    def solution(file_lines: list[str]) -> int:
        # https://en.wikipedia.org/wiki/Pick%27s_theorem
        """
        Using Picks theorem to get the exterior points of the polygon
        """
        result = 0
        points = [(0, 0)]
        dirs = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}

        total_number_of_squares = 0

        for line in file_lines:
            direction, number_of_squares_in_segment, _ = line.split()  # Don't need the color for the first day
            dr, dc = dirs[direction]
            number_of_squares_in_segment = int(number_of_squares_in_segment)
            total_number_of_squares += number_of_squares_in_segment
            r, c = points[-1]
            points.append((r + dr * number_of_squares_in_segment, c + dc * number_of_squares_in_segment))

        A = abs(sum(points[i][0] * (points[i - 1][1] - points[(i + 1) % len(points)][1]) for i in range(len(points)))) // 2
        i = A - total_number_of_squares // 2 + 1

        result = i + total_number_of_squares
        return result


class Part2:
    @staticmethod
    def solution(file_lines: list[str]) -> int:
        result = 0
        points = [(0, 0)]
        dirs = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}

        b = 0

        for line in file_lines:
            _, _, x = line.split()
            x = x[2:-1]
            dr, dc = dirs["RDLU"[int(x[-1])]]
            n = int(x[:-1], 16)
            b += n
            r, c = points[-1]
            points.append((r + dr * n, c + dc * n))

        A = abs(sum(points[i][0] * (points[i - 1][1] - points[(i + 1) % len(points)][1]) for i in range(len(points)))) // 2
        i = A - b // 2 + 1

        result = i + b
        return result


with open("input.txt", "r") as file:
    f = file.read().splitlines()

print(f"Part 1: {Part1.solution(f)}")
print(f"Part 2: {Part2.solution(f)}")



