class Part1():
    def solution(file_lines: list[str]) -> int:
        race_durations  = []
        record_distances = []
        race_durations.extend(file_lines[0].split()[1:])
        record_distances.extend(file_lines[1].split()[1:])
        result = 1
        for (duration, distance) in zip(race_durations , record_distances):
            duration, distance = list(map(int, (duration, distance)))
            res = Part1.evaluate(duration, distance)
            result *= res
        return result

    def evaluate(duration: int, distance: int):
        result = 0
        for button_push_time in range(duration):
            dist = button_push_time * duration - button_push_time ** 2
            if dist > distance:
                result += 1
        return result


class Part2:
    def solution(file_lines: list[str]) -> int:
        race_durations  = []
        record_distances = []
        race_durations.extend(file_lines[0].split()[1:])
        record_distances.extend(file_lines[1].split()[1:])
        result = 1
        # Converting integer list to string list
        # and joining the list using join()
        duration = int("".join(map(str, race_durations)))
        distance = int("".join(map(str, record_distances)))
        res = Part1.evaluate(duration, distance)
        result *= res

        return result



with open("input.txt", "r") as file:
    f = file.read().splitlines()

# print(f"Part 1: {Part1.solution(f)}")
# print(f"Part 2: {Part2.solution(f)}")
print("2 squared is :" + str(2 ** 2) )

