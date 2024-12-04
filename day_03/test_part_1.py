from part_1 import find_mul_pairs, parse_pairs, pair_multiplier, find_sum_of_products

test_input = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"


def test_find_mul_pairs():
    assert find_mul_pairs(test_input) == [["2", "4"], ["5", "5",], ["11", "8"], ["8", "5"]]
    assert find_mul_pairs("maroeumul(353,343)area") == [["353", "343"]]


def test_parse_pairs():
    assert parse_pairs(["mul(2,4)", "mul(5,5)", "mul(11,8)", "mul(8,5)"]) == [["2", "4"], ["5", "5",], ["11", "8"], ["8", "5"]]


def test_pair_multiplier():
    assert pair_multiplier(["2", "4"]) == 8
    assert pair_multiplier(["5", "5"]) == 25
    assert pair_multiplier(["11", "8"]) == 88
    assert pair_multiplier(["8", "5"]) == 40


def test_find_sum_of_products():
    assert find_sum_of_products([["2", "4"], ["5", "5",], ["11", "8"], ["8", "5"]]) == 161