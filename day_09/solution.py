class Part1:
    @staticmethod
    def solution(file_lines: list[str]) -> int:
        result = 0
        next_numbers_for_all_sequences = []

        for line in file_lines:
            line_array = line.split(' ')
            sequence = [int(x) for x in line_array]
            next_numbers_for_all_sequences.append(Part1.predict_next_number(sequence))

        result = sum(next_numbers_for_all_sequences)


        return result

    @staticmethod
    def predict_next_number(seq, prev=0):
        if seq:
            if len(seq) == 1:
                return prev + seq[-1] # Predict next in sequence as last value + difference

            return Part1.predict_next_number([b - a for a, b in zip(seq[:-1], seq[1:])], prev + seq[-1]) # Find prediction for next difference
        else:
            return 0


class Part2:
    @staticmethod
    def solution(file_lines: list[str]) -> int:
        result = 0
        previous_numbers_for_all_sequences = []

        for line in file_lines:

            line_array = line.split(' ')
            sequence = [int(x) for x in line_array]
            sequence.reverse()
            previous_numbers_for_all_sequences.append(Part1.predict_next_number(sequence))

        result = sum(previous_numbers_for_all_sequences)


        return result


with open("input.txt", "r") as file:
    f = file.read().splitlines()

print(f"Part 1: {Part1.solution(f)}")
print(f"Part 2: {Part2.solution(f)}")



