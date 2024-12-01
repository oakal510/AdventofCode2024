from part_2 import parse_input, find_similarity

def test_parse_input():
    # test input is a file with the test input data from the AoC problem
    assert parse_input('day_01/test_input.txt') == ([3, 4, 2, 1, 3, 3], [4, 3, 5, 3, 9, 3])

def test_find_similarity():
    assert find_similarity(([3, 4, 2, 1, 3, 3], [4, 3, 5, 3, 9, 3])) == 31