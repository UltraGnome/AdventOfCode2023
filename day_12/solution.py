class Part1:
    @staticmethod
    def solution(file_lines: list[str]) -> int:

        result = 0

        for line in file_lines:
            spring_conditions, spring_arrangement = line.split()
            spring_arrangement = tuple(map(int, spring_arrangement.split(",")))
            result += Part1.count_possible_arrangements(spring_conditions, spring_arrangement)

        return result

    @staticmethod
    def count_possible_arrangements(spring_conditions, spring_arrangement):
        if spring_conditions == "":
            return 1 if spring_arrangement == () else 0
    
        if spring_arrangement == ():
            return 0 if "#" in spring_conditions else 1
    
        result = 0
    
        if spring_conditions[0] in ".?":
            result += Part1.count_possible_arrangements(spring_conditions[1:], spring_arrangement)
    
        if spring_conditions[0] in "#?":
            if spring_arrangement[0] <= len(spring_conditions) and "." not in spring_conditions[:spring_arrangement[0]] and (spring_arrangement[0] == len(spring_conditions) or spring_conditions[spring_arrangement[0]] != "#"):
                result += Part1.count_possible_arrangements(spring_conditions[spring_arrangement[0] + 1:], spring_arrangement[1:])
    
        return result
class Part2:
    @staticmethod
    def solution(file_lines: list[str]) -> int:
        cache = {}

        def count(cfg, nums):
            if cfg == "":
                return 1 if nums == () else 0

            if nums == ():
                return 0 if "#" in cfg else 1

            key = (cfg, nums)

            if key in cache:
                return cache[key]

            result = 0

            if cfg[0] in ".?":
                result += count(cfg[1:], nums)

            if cfg[0] in "#?":
                if nums[0] <= len(cfg) and "." not in cfg[:nums[0]] and (nums[0] == len(cfg) or cfg[nums[0]] != "#"):
                    result += count(cfg[nums[0] + 1:], nums[1:])

            cache[key] = result
            return result

        total = 0

        for line in file_lines:
            cfg, nums = line.split()
            nums = tuple(map(int, nums.split(",")))

            cfg = "?".join([cfg] * 5)
            nums *= 5

            total += count(cfg, nums)

        return total


with open("input.txt", "r") as file:
    f = file.read().splitlines()

# print(f"Part 1: {Part1.solution(f)}")
print(f"Part 2: {Part2.solution(f)}")



