from part_1 import find_magic_word, find_fwd_bwd_matches, find_vertical_diag_matches

test_input = """MMMSXXMASM\nMSAMXMSMSA\nAMXSXMAAMM\nMSAMASMSMX\nXMASAMXAMM\nXXAMMXXAMA\nSMSMSASXSS\nSAXAMASAAA\nMAMMMXMMMM\nMXMXAXMASX"""


def test_find_magic_word():
    assert find_magic_word(test_input) == 18


def test_find_fwd_bwd_matches():
    assert find_fwd_bwd_matches(test_input) == 5
    assert find_fwd_bwd_matches("..X...\n.SAMX.\n.A..A.\nXMAS.S\n.X....\n") == 2


def test_find_vertical_diag_matches():
    assert find_vertical_diag_matches(test_input) == 13
    assert find_vertical_diag_matches("..X...\n.SAMX.\n.A..A.\nXMAS.S\n.X....\n") == 2