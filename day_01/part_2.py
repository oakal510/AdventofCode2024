""" Solution for Advent of Code 2024, Day 1, Part 2 """

def parse_input(input_file):

    list_1 = []
    list_2 = []
    
    with open(input_file) as file:
        for line in file:
            line = line.split("   ")
            list_1.append(int(line[0]))
            list_2.append(int(line[1]))

    return list_1, list_2


def find_similarity(lists):

    similarity = 0
    
    for number in lists[0]:
        number_count = lists[1].count(number)
        similarity += number * number_count

    return similarity


if __name__ == '__main__':

    lists = parse_input('day_01/input.txt')
    result = find_similarity(lists)
    print(result)