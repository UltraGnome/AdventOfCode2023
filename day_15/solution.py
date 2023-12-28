import re
from functools import reduce
from collections import defaultdict

class Part1:
    @staticmethod
    def solution(instructions) -> int:
        result = 0

        for step in instructions:
            step_score = Part1.score_step(step)
            result += step_score

        return result

    @staticmethod
    def score_step(step):
        step_score = 0
        for letter in list(step):
            step_score += ord(letter)
            step_score = step_score * 17
            step_score = step_score % 256
        return step_score


class Part2:
    @staticmethod
    def solution(instructions) -> int:
        boxes = [dict() for x in range(256)]

        for i, s in enumerate(instructions):
            if "-" in s:
                lens_id = s[:s.index("-")]
                box_id = Part1.score_step(lens_id)

                if lens_id in boxes[box_id]:
                    del boxes[box_id][lens_id]
            elif "=" in s:
                lens_id = s[:s.index("=")]
                box_id = Part1.score_step(lens_id)
                lens_focal = int(s[s.index("=")+1:])
                boxes[box_id][lens_id] = lens_focal

            else:
                print("ERROR", s)

        result = 0
        for box_id, box in enumerate(boxes):
            for slot_id, lens in enumerate(box):
                result += (box_id+1) * (slot_id+1) * box[lens]

        return result



with open("input.txt", "r") as file:
    f = file.read().split(',')

print(f"Part 1: {Part1.solution(f)}")
print(f"Part 2: {Part2.solution(f)}")



