""" Solution for Advent of Code 2024, Day 4, Part 1 """

import re


def find_magic_word(input):

    count = find_fwd_bwd_matches(input)
    count += find_vertical_diag_matches(input)
    
    return count


def find_fwd_bwd_matches(input):
    fwd_matches = re.findall("XMAS", input)
    bwd_matches = re.findall("SAMX", input)
    return (len(fwd_matches) + len(bwd_matches))


def find_vertical_diag_matches(input):

    count = 0

    input_list = input.split("\n")
    input_grid = [list(line) for line in input_list]

    print(input_grid)

    for i, line in enumerate(input_grid):
        for j, letter in enumerate(line):
            if i == len(input_grid) - 3:
                return count
            else:
                if letter == 'X':
                    # find forward vertical matches
                    if input_grid[i+1][j] == "M":
                        if input_grid[i+2][j] == "A":
                            if input_grid[i+3][j] == "S":
                                print("fwd_vertical")
                                count += 1   
                    # find forward right diagonal matches
                    if j <= len(line) - 4:
                        if input_grid[i+1][j+1] == "M":
                            if input_grid[i+2][j+2] == "A":
                                if input_grid[i+3][j+3] == "S":
                                    print("fwd_right_diagonal")
                                    count += 1
                    # find forward left diagonal matches
                    if j >= len("MAS"):
                        if input_grid[i+1][j-1] == "M":
                            if input_grid[i+2][j-2] == "A":
                                if input_grid[i+3][j-3] == "S":
                                    print("fwd_left_diagonal")
                                    count += 1

                elif letter == "S":
                    # find backward vertical matches
                    if input_grid[i+1][j] == "A":
                        if input_grid[i+2][j] == "M":
                            if input_grid[i+3][j] == "X":
                                print("bwd_vertical")
                                count += 1
                    # find backward right diagonal matches
                    if j <= len(line) - 4:
                        if input_grid[i+1][j+1] == "A":
                            print(i+3, j+3, len(input_grid))
                            if input_grid[i+2][j+2] == "M":
                                if input_grid[i+3][j+3] == "X":
                                    print("bwd_right_diagonal")
                                    count += 1
                    # find backward left diagonal matches
                    if j >= len("MAS"):
                        if input_grid[i+1][j-1] == "A":
                            if input_grid[i+2][j-2] == "M":
                                if input_grid[i+3][j-3] == "X":
                                    count += 1


    return count


if __name__ == "__main__":

    with open('day_04/input.txt') as file:
        input = file.read()
    
    print(find_magic_word(input))