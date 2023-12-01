from itertools import compress
class Part1:

    def solution(file_lines: list[str]) -> int:
      result = 0

      for line in file_lines:
        if(len(line)>1):
          result += Part1.process_line(line)

      return result

    def process_line(line: str):
        found_digits = ""
        result = 0
        calibration_string = ""
        for index, letter in enumerate(line):
            if letter.isdigit():
                found_digits += letter
        if (len(found_digits) < 2):
            calibration_string += found_digits + found_digits
        else:
            calibration_string += found_digits[0] + found_digits[len(found_digits) - 1]
        result += int(calibration_string)
        return result


class Part2:

    def solution(file_lines: list[str]) -> int:
        result = 0

        for line in file_lines:
            clean_line = Part2.extract_numbers(line)
            if(clean_line != line):
              print (line + "  >  " + clean_line)
            result += Part1.process_line(clean_line)

        return result

    def extract_numbers(inputline):
        junk_numbers_to_correct = {"eightwo":"eighttwo","twone":"twoone","eighthree":"eightthree","nineight":"nineeight","oneight":"oneeight"}
        numbers_by_index = {"one":0,"two":0,"three":0,"four":0,"five":0,"six":0,"seven":0,"eight":0,"nine":0}
        numbers_with_numeral = {"one":"1","two":"2","three":"3","four":"4","five":"5","six":"6","seven":"7","eight":"8","nine":"9"}
        line = inputline.lower()
        numbers_by_index["eight"]=(line.find("eight"))
        numbers_by_index["nine"]=(line.find("nine"))
        numbers_by_index["two"]=(line.find("two"))
        numbers_by_index["one"]=(line.find("one"))
        numbers_by_index["two"]=(line.find("two"))
        numbers_by_index["three"]=(line.find("three"))
        numbers_by_index["four"]=(line.find("four"))
        numbers_by_index["five"]=(line.find("five"))
        numbers_by_index["six"]=(line.find("six"))
        numbers_by_index["seven"]=(line.find("seven"))
        numbers_by_index["eight"]=(line.find("eight"))
        numbers_by_index["nine"]=(line.find("nine"))

        # #find last occurence
        numbers_by_index["one"]=(line.rfind("one"))
        numbers_by_index["two"]=(line.rfind("two"))
        numbers_by_index["eight"]=(line.rfind("eight"))
        numbers_by_index["three"]=(line.rfind("three"))
        numbers_by_index["four"]=(line.rfind("four"))
        numbers_by_index["five"]=(line.rfind("five"))
        numbers_by_index["six"]=(line.rfind("six"))
        numbers_by_index["seven"]=(line.rfind("seven"))
        numbers_by_index["eight"]=(line.rfind("eight"))
        numbers_by_index["nine"]=(line.rfind("nine"))

        for key, value in junk_numbers_to_correct.items():
            line = line.replace(key, junk_numbers_to_correct[key])

        for key, value in numbers_by_index.items():
            if value > -1:
                line = line.replace(key, numbers_with_numeral[key])

        return line

# with open("test_input_2.txt", "r") as file:
with open("input.txt", "r") as file:
    f = file.read().splitlines()

#print(f"Test input: {Part1.solution(f)}")
#print(f"Part 1: {Part1.solution(f)}")
print(f"Part 2: {Part2.solution(f)}")
