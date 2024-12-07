from part_2 import find_xmax_xs

test_input = """MMMSXXMASM\nMSAMXMSMSA\nAMXSXMAAMM\nMSAMASMSMX\nXMASAMXAMM\nXXAMMXXAMA\nSMSMSASXSS\nSAXAMASAAA\nMAMMMXMMMM\nMXMXAXMASX"""

def test_find_xmax_xs():
    assert find_xmax_xs(test_input) == 9