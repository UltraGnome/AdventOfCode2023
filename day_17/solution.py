from heapq import heappop, heappush
from typing import NamedTuple
from graphs import Direction, GridPoint, Rotation, add_points, parse_grid

class Position(NamedTuple):
    loc: GridPoint
    facing: Direction

    @property
    def next_loc(self) -> GridPoint:
        return add_points(self.loc, Direction.offset(self.facing))

    def step(self) -> "Position":
        return Position(self.next_loc, self.facing)

    def rotate_and_step(self, towards: Rotation):
        return Position(self.loc, Direction.rotate(self.facing, towards)).step()


# cost, position, number of steps in the same direction (max 3)
State = tuple[int, Position, int]
class Part1:

    @staticmethod
    def solution(file_lines: list[str], min_steps:int, max_steps:int) -> int:
        result = -1
        target = len(file_lines) - 1, len(file_lines[-1]) - 1
        grid = {k: int(v) for k, v in parse_grid(file_lines).items()}

        queue: list[State] = [
            (0, Position((0, 0), Direction.DOWN), 0),
            (0, Position((0, 0), Direction.RIGHT), 0),
        ]
        seen: set[tuple[Position, int]] = set()

        while queue:
            cost, pos, num_steps = heappop(queue)

            if pos.loc == target and num_steps >= min_steps:
                result = cost
                return result

            if (pos, num_steps) in seen:
                continue
            seen.add((pos, num_steps))

            if (
                    num_steps >= min_steps
                    and (left := pos.rotate_and_step("CCW")).loc in grid
            ):
                heappush(queue, (cost + grid[left.loc], left, 1))

            if (
                    num_steps >= min_steps
                    and (right := pos.rotate_and_step("CW")).loc in grid
            ):
                heappush(queue, (cost + grid[right.loc], right, 1))

            if num_steps < max_steps and (forward := pos.step()).loc in grid:
                heappush(queue, (cost + grid[forward.loc], forward, num_steps + 1))

        return result

    def dijkstra(file_lines: list[str]) -> int:
        result = -1
        target = len(file_lines) - 1, len(file_lines[-1]) - 1
        grid = {k: int(v) for k, v in parse_grid(file_lines).items()}

        queue: list[State] = [
            (0, Position((0, 0), Direction.DOWN), 0),
            (0, Position((0, 0), Direction.RIGHT), 0),
        ]
        seen: set[tuple[Position, int]] = set()

        while queue:
            cost, pos, num_steps = heappop(queue)

            if pos.loc == target:
                result = cost
                return result

            if (pos, num_steps) in seen:
                continue
            seen.add((pos, num_steps))

            if (
                    left := pos.rotate_and_step("CCW").loc in grid
            ):
                heappush(queue, (cost + grid[left.loc], left, 1))

            if (
                    right := pos.rotate_and_step("CW").loc in grid
            ):
                heappush(queue, (cost + grid[right.loc], right, 1))

            if forward := pos.step().loc in grid:
                heappush(queue, (cost + grid[forward.loc], forward, num_steps + 1))

        return result

class Part2:
    @staticmethod
    def solution(file_lines: list[str]) -> int:
        Part1.solution(file_lines,4,10)


        return 0


with open("input.txt", "r") as file:
    f = file.read().splitlines()
    # just Dijsktra


print(f"just Dijsktra: {Part1.dijkstra(f)}")
print(f"Part 1: {Part1.solution(f,0,3)}")
print(f"Part 2: {Part1.solution(f, 4, 10)}")







#
# class Solution(StrSplitSolution):
#     _year = 2023
#     _day = 17
#
#     def _solve(self, min_steps: int, max_steps: int) -> int:
#
#     @answer(1244)
#     def part_1(self) -> int:
#         return self._solve(0, 3)
#
#     @slow
#     @answer(1367)
#     def part_2(self) -> int:
#         return self._solve(4, 10)
