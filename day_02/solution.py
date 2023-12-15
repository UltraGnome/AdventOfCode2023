class Part1:

    @staticmethod
    def solution(file_lines: list[str]) -> int:
        result = 0

        for line in file_lines:
            result += Part1.evaluate_cube_counts(line)

        return result

    @staticmethod
    def evaluate_cube_counts(line):
        result = 0
        cube_totals_by_color = {"red":12,"green":13,"blue":14}
        blues = []
        reds = []
        greens = []
        line = line.lower()
        game_id = int(line.split(":")[0].split(" ")[1])
        line = line.replace(";", ",")
        line = line.split(":")[1]
        Part1.count_by_color(blues, greens, line, reds)
        return Part1.validate_game(blues, cube_totals_by_color, game_id, greens, reds, result)

    @staticmethod
    def validate_game(blues, cube_totals_by_color, game_id, greens, reds, result):
        if max(reds) > cube_totals_by_color["red"]:
            return result
        elif max(greens) > cube_totals_by_color["green"]:
            return result
        elif max(blues) > cube_totals_by_color["blue"]:
            return result
        else:
            result = game_id
            return result

    @staticmethod
    def count_by_color(blues, greens, line, reds):
        cube_counts = line.split(",")
        for count in cube_counts:
            count = count.strip()
            color_pair = count.split(" ")
            if color_pair[1].startswith("r"):
                reds.append(int(color_pair[0]))
            elif color_pair[1].startswith("g"):
                greens.append(int(color_pair[0]))
            else:
                blues.append(int(color_pair[0]))

class Part2:
    @staticmethod
    def solution(file_lines: list[str]) -> int:
        result = 0

        for line in file_lines:
            blues = []
            reds = []
            greens = []
            line = line.lower()
            line = line.replace(";", ",")
            line = line.split(":")[1]
            Part1.count_by_color(blues, greens, line, reds)
            game_power = max(blues) * max(greens) * max(reds)
            result += game_power

        return result



with open("input.txt", "r") as file:
    f = file.read().splitlines()

#print(f"Part 1: {Part1.solution(f)}")
print(f"Part 2: {Part2.solution(f)}")



