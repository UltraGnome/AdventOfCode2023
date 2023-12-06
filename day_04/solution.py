class Part1:
    @staticmethod
    def solution(file_lines: list[str]) -> int:
        result = 0

        for line in file_lines:
            score = 0
            found_one_winner = False
            numbers, winners = Part1.parse_line(line)
            for w in winners:
                if len(w.strip()) > 0:
                    if w in numbers:
                        if found_one_winner:
                            score = score * 2
                        else:
                            score = 1
                            found_one_winner = True
            result += score



        return result

    @staticmethod
    def parse_line(line):
        line = line.strip()
        line = line.rstrip('\n')
        line = line.rstrip('\r')
        card = line.split(':')
        card2 = str(card[1].strip()).split('|')
        winners = str(card2[0].strip()).split(' ')
        numbers = str(card2[1].strip()).split(' ')
        return numbers, winners


class Part2:

    @staticmethod
    def solution(file_lines: list[str]) -> int:
        result = 0
        cards = {}
        max_value = 0
        for line in file_lines:
            for line in file_lines:
                card_id, winners = Part2.parse_line_d2(line)
                if winners > max_value:
                    max_value = winners
                cards[card_id] = [winners, 1]
            for i in range(len(cards)+1, max_value + len(cards)):
                cards[i] = [0,0,0]

            for id in cards.keys():
                for e in range(cards[id][1]):
                    for i in range(cards[id][0]):
                        cards[id+i+1][1] += 1

            for val in cards.values():
                if len(val) == 2:
                    result += val[1]
            return result
    @staticmethod
    def parse_line_d2(line: str):
        card_id = int(line[:line.index(':')].split()[-1])
        winners = line[line.index(':')+1:line.index('|')-1].split()
        numbers = line[line.index('|')+1:].strip().split()
        count = 0
        for e in numbers:
            if e in winners:
                count += 1
        return card_id, count

with open("input.txt", "r") as file:
    f = file.read().splitlines()

# print(f"Part 1: {Part1.solution(f)}")
print(f"Part 2: {Part2.solution(f)}")



