class Part1():
    def __init__(self):
        self.charge_up = []
        self.record = []

    def read_data(self):
        with open("input.txt", "r") as f:
            document = f.read()
        return document

    def evaluate(self, race_time: int, record: int):
        count = 0
        for charge_time in range(race_time):
            dist = charge_time * race_time - charge_time ** 2
            if dist > record:
                count += 1
        return count

def main():
    solver = Part1()
    data = solver.read_data().split("\n")
    solver.charge_up.extend(data[0].split()[1:])
    solver.record.extend(data[1].split()[1:])
    total = 1
    for (duration, record) in zip(solver.charge_up, solver.record):
        duration, record = list(map(int, (duration, record)))
        print(f"Race duration: {duration}")
        print(f"Current record: {record}")
        res = solver.evaluate(duration, record)
        total *= res
        print(f"Possible ways to beat record: {res}")
    return total