class Bearowcount:
    start_point = ()
    current_direction = {}

class Part1:
    @staticmethod
    def solution(file_lines: list[str]) :

        row_index = 0
        col_index = 0

        grid = [list(row) for row in file_lines]
        rowcount, n = len(grid), len(grid[0])
        visited_points = set()
        energized_points = set()
        queue = set([(0, 0, 'right')])
        while queue:
            row_index, col_index, direction = queue.pop()
            energized_points.add((row_index, col_index))
            tile = grid[row_index][col_index]

            if col_index < n-1 and (row_index, col_index+1, 'right') not in visited_points and (
                    (direction == 'right' and tile in '.-') or
                    (direction == 'up' and tile in '/-') or
                    (direction == 'down' and tile in '\\-')):
                queue.add((row_index, col_index+1, 'right'))
                visited_points.add((row_index, col_index+1, 'right'))

            if row_index > 0 and (row_index-1, col_index, 'up') not in visited_points and (
                    (direction == 'up' and tile in '.|') or
                    (direction == 'right' and tile in '/|') or
                    (direction == 'left' and tile in '\\|')):
                queue.add((row_index-1, col_index, 'up'))
                visited_points.add((row_index-1, col_index, 'up'))

            if col_index > 0 and (row_index, col_index-1, 'left') not in visited_points and (
                    (direction == 'left' and tile in '.-') or
                    (direction == 'up' and tile in '\\-') or
                    (direction == 'down' and tile in '/-')):
                queue.add((row_index, col_index-1, 'left'))
                visited_points.add((row_index, col_index-1, 'left'))

            if row_index < rowcount-1 and (row_index+1, col_index, 'down') not in visited_points and (
                    (direction == 'down' and tile in '.|') or
                    (direction == 'right' and tile in '\\|') or
                    (direction == 'left' and tile in '/|')):
                queue.add((row_index+1, col_index, 'down'))
                visited_points.add((row_index+1, col_index, 'down'))
    
        return len(energized_points)


class Part2:
    @staticmethod
    def solution(file_lines: list[str]) -> int:
        row_index = 0
        col_index = 0
        grid = [list(row) for row in file_lines]
        rowcount, rowsize = len(grid), len(grid[0])
        edge_start_points = ({(row_index, 0, 'right') for row_index in range(rowcount)} |
                   {(row_index, rowsize-1, 'left') for row_index in range(rowcount)} |
                   {(rowcount-1, col_index, 'up') for col_index in range(rowsize)} |
                   {(0, col_index, 'down') for col_index in range(rowsize)})

        best = 0
        for i in edge_start_points:
            visited = set()
            energized = set()
            queue = set([i])
            while queue:
                row_index, col_index, direction = queue.pop()
                energized.add((row_index, col_index))
                tile = grid[row_index][col_index]
    
                if col_index < rowsize-1 and (row_index, col_index+1, 'right') not in visited and (
                        (direction == 'right' and tile in '.-') or
                        (direction == 'up' and tile in '/-') or
                        (direction == 'down' and tile in '\\-')):
                    queue.add((row_index, col_index+1, 'right'))
                    visited.add((row_index, col_index+1, 'right'))
    
                if row_index > 0 and (row_index-1, col_index, 'up') not in visited and (
                        (direction == 'up' and tile in '.|') or
                        (direction == 'right' and tile in '/|') or
                        (direction == 'left' and tile in '\\|')):
                    queue.add((row_index-1, col_index, 'up'))
                    visited.add((row_index-1, col_index, 'up'))
    
                if col_index > 0 and (row_index, col_index-1, 'left') not in visited and (
                        (direction == 'left' and tile in '.-') or
                        (direction == 'up' and tile in '\\-') or
                        (direction == 'down' and tile in '/-')):
                    queue.add((row_index, col_index-1, 'left'))
                    visited.add((row_index, col_index-1, 'left'))
    
                if row_index < rowcount-1 and (row_index+1, col_index, 'down') not in visited and (
                        (direction == 'down' and tile in '.|') or
                        (direction == 'right' and tile in '\\|') or
                        (direction == 'left' and tile in '/|')):
                    queue.add((row_index+1, col_index, 'down'))
                    visited.add((row_index+1, col_index, 'down'))
    
            best = max(best, len(energized))

        return best


with open("input.txt", "r") as file:
    f = file.read().splitlines()

print(f"Part 1: {Part1.solution(f)}")
print(f"Part 2: {Part2.solution(f)}")



