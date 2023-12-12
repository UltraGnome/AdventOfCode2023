from collections import Counter
import functools
from enum import Enum

class Hand(object):
    def __init__(self, hand, bid):
        self.hand = hand
        self.bid = bid

    def get_card_ranks(self):
        ranks = []
        for letter in list(self.hand):
            if letter == 'A':
                ranks.append(14)
            elif letter == 'K':
                ranks.append(13)
            elif letter == 'Q':
                ranks.append(12)
            elif letter == 'J':
                ranks.append(0)
            elif letter == 'T':
                ranks.append(10)
            else:
                ranks.append(int(letter))
        return ranks

class Part1:

    @staticmethod
    def solution(file_lines: list[str]) -> int:
        result = 0
        fv_oak = []
        fr_oak = []
        fh = []
        th_oak = []
        two_pr = []
        one_pr = []
        high_cd = []
        for line in file_lines:
            hand = Hand(line.split(' ')[0], line.split(' ')[1])
            Part1.determine_hand_type(hand, fh, fr_oak, fv_oak, high_cd, one_pr, th_oak, two_pr)

        sorted_hands = Part1.rank_all_hand_types(fh, fr_oak, fv_oak, high_cd, one_pr, th_oak, two_pr)

        index = 1
        for hand in sorted_hands:
            result += index * int(hand.bid)
            index += 1

        return result

    @staticmethod
    def rank_all_hand_types(fh, fr_oak, fv_oak, high_cd, one_pr, th_oak, two_pr):
        sorted_hands = sorted(high_cd, key=functools.cmp_to_key(Part1.compare_hands))
        sorted_hands.extend(sorted(one_pr, key=functools.cmp_to_key(Part1.compare_hands)))
        sorted_hands.extend(sorted(two_pr, key=functools.cmp_to_key(Part1.compare_hands)))
        sorted_hands.extend(sorted(th_oak, key=functools.cmp_to_key(Part1.compare_hands)))
        sorted_hands.extend(sorted(fh, key=functools.cmp_to_key(Part1.compare_hands)))
        sorted_hands.extend(sorted(fr_oak, key=functools.cmp_to_key(Part1.compare_hands)))
        sorted_hands.extend(sorted(fv_oak, key=functools.cmp_to_key(Part1.compare_hands)))

        return sorted_hands

    @staticmethod
    def determine_hand_type(hand, fh, fr_oak, fv_oak, high_cd, one_pr, th_oak, two_pr):

        hand_profile = Counter(hand.hand)
        if len(hand_profile.keys()) == 5:
            high_cd.append(hand)
        elif len(hand_profile.keys()) == 4:
            one_pr.append(hand)
        elif len(hand_profile.keys()) == 3 and 3 in hand_profile.values():
            th_oak.append(hand)
        elif len(hand_profile.keys()) == 3 and max(hand_profile.values()) == 2:
            two_pr.append(hand)
        elif len(hand_profile.keys()) == 2 and 4 in hand_profile.values():
            fr_oak.append(hand)
        elif len(hand_profile.keys()) == 2 and 3 in hand_profile.values():
            fh.append(hand)
        elif len(hand_profile.keys()) == 1:
            fv_oak.append(hand)

    @staticmethod
    def compare_hands(hand1,hand2):
        hands_are_equal = 0
        card_comparison_result = hands_are_equal
        index = 0
        while index < 5:
            card_comparison_result = Part1.compare_cards(hand1.get_card_ranks()[index], hand2.get_card_ranks()[index])
            if card_comparison_result == 0:
                index += 1
            else:
                return card_comparison_result
        else:
           return card_comparison_result

    @staticmethod
    def compare_cards(card1,card2):
        first_card_is_lower = -1
        second_card_is_lower = 1
        cards_are_equal = 0
        if card1 == card2:
            return cards_are_equal
        elif card1 < card2:
            return first_card_is_lower
        else:
            return second_card_is_lower

# 1 hand type
# 2 hand rank by type
#  sort each hand type list
# 3 calculate hand winnings
# 4 sum winnings
# collection = Counter(a_string)



class Part2:
    @staticmethod
    def solution(file_lines: list[str]) -> int:
        result = 0
        fv_oak = []
        fr_oak = []
        fh = []
        th_oak = []
        two_pr = []
        one_pr = []
        high_cd = []
        for line in file_lines:
            hand = Hand(line.split(' ')[0], line.split(' ')[1])
            Part2.determine_hand_type(hand, fh, fr_oak, fv_oak, high_cd, one_pr, th_oak, two_pr)

        sorted_hands = Part1.rank_all_hand_types(fh, fr_oak, fv_oak, high_cd, one_pr, th_oak, two_pr)

        index = 1
        for hand in sorted_hands:
            result += index * int(hand.bid)
            index += 1

        return result


    @staticmethod
    def determine_hand_type(hand, fh, fr_oak, fv_oak, high_cd, one_pr, th_oak, two_pr):

        hand_profile = Counter(hand.hand)
        joker_count = hand_profile.get('J')
        if joker_count is None:
            joker_count = 0
        if joker_count == 0:
            Part1.determine_hand_type(hand, fh, fr_oak, fv_oak, high_cd, one_pr, th_oak, two_pr)
        elif len(hand_profile.keys()) == 5:
            one_pr.append(hand)
        elif len(hand_profile.keys()) == 4:
            th_oak.append(hand)
        elif len(hand_profile.keys()) == 3:
            if joker_count > 1:
                fr_oak.append(hand)
            elif joker_count==1 and max(hand_profile.values())==3:
                fr_oak.append(hand)
            else:
                fh.append(hand)
        elif len(hand_profile.keys()) == 2 and 4 in hand_profile.values():
            fv_oak.append(hand)
        elif len(hand_profile.keys()) == 2 and 3 in hand_profile.values():
            fv_oak.append(hand)
        elif len(hand_profile.keys()) == 1:
            fv_oak.append(hand)



with open("input.txt", "r") as file:
    f = file.read().splitlines()

# print(f"Part 1: {Part1.solution(f)}")
print(f"Part 2: {Part2.solution(f)}")



