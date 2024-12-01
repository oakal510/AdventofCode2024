""" Solution for Advent of Code 2024, Day 1, Part 1 """

def parse_input(input_file):

    list_1 = []
    list_2 = []
    
    with open(input_file) as file:
        for line in file:
            line = line.split("   ")
            list_1.append(int(line[0]))
            list_2.append(int(line[1]))

    return list_1, list_2


def find_distances(lists):
    
    sorted_lists = []

    for my_list in lists:
        sorted_lists.append(sorted(my_list))

    for sorted_list in sorted_lists:
        distance = 0
        for i in range(len(sorted_lists[0])):
            distance += abs(sorted_lists[0][i] - sorted_lists[1][i])

    return distance  


if __name__ == '__main__':

    lists = parse_input('day_01/input.txt')

    result = find_distances(lists)
    print(result)  
