import pytest
from part_1 import parse_input, find_distances

def test_parse_input():
    assert parse_input('day_01/test_input.txt') == ([3, 4, 2, 1, 3, 3], [4, 3, 5, 3, 9, 3])

def test_find_distances():
    assert find_distances(([3, 4, 2, 1, 3, 3], [4, 3, 5, 3, 9, 3])) == 11