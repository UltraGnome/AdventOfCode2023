import itertools
import math
import re


class Part1:
    @staticmethod
    def solution(file_contents) -> int:
        result = 0
        directions, nodes = file_contents.split('\n\n')
        directions = itertools.cycle(0 if step.upper() == 'L' else 1 for step in directions)

        node_dict = {}
        regex = r'(\w{3}) = \((\w{3}), (\w{3})\)'
        # read all the nodes into a dictionary.
        for node, foo, bar in re.findall(regex, nodes):
            node_dict[node] = [foo, bar]

        #  go to the AAA node, not starting from idx 0
        node = 'AAA'
        for result, d in enumerate(directions, start=1):
            node = node_dict[node][d]
            if node == 'ZZZ':
                break

        """
        counter for steps
        Read directions into a list.
        Read nodes into a dictionary, k, []
        for loop directions
        at end, recursively continue
        """

        return result


class Part2:
    @staticmethod
    def solution(file_contents) -> int:
        result = 0
        directions, nodes = file_contents.split('\n\n')
        directions = itertools.cycle(0 if step.upper() == 'L' else 1 for step in directions)

        node_dict = {}
        regex = r'(\w{3}) = \((\w{3}), (\w{3})\)'
        # read all the nodes into a dictionary.
        for node, foo, bar in re.findall(regex, nodes):
            node_dict[node] = [foo, bar]

        starting_nodes = [node for node in node_dict if node[2] == 'A']
        step_counts = []
        for node in starting_nodes:
            for steps, d in enumerate(directions, start=1):
                node = node_dict[node][d]
                if node[2] == 'Z':
                    step_counts.append(steps)
                    break

        result = math.lcm(*step_counts)
        return result

with open("input.txt", "r") as file:
    f = file.read()

# print(f"Part 1: {Part1.solution(f)}")
print(f"Part 2: {Part2.solution(f)}")



