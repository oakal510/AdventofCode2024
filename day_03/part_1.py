""" Solution for Advent of Code 2024, Day 3, Part 1 """

import re


def find_mul_pairs(input):
    matches = re.findall(r'mul\(\d\d?\d?,\d\d?\d?\)', input)
    print(matches)
    return parse_pairs(matches)


def parse_pairs(pair_matches):
    mul_pairs = []
    for pair_match in pair_matches:
        matches = re.findall(r'\d\d?\d?', pair_match)
        mul_pairs.append(matches)
    
    return mul_pairs


def find_sum_of_products(multiplication_pairs):

    sum_of_products = 0

    for pair in multiplication_pairs:
        sum_of_products += pair_multiplier(pair)
    return sum_of_products


def pair_multiplier(pair_list):
    return int(pair_list[0])*int(pair_list[1])


if __name__ == "__main__":

    with open('day_03/input.txt') as file:
        input = file.read()
    
    print(find_sum_of_products(find_mul_pairs(input)))
