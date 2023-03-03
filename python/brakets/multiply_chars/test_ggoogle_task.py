from main import convert_to_flat_str


def test_first():
    assert convert_to_flat_str('3[a]') == 'aaa'


def test_second():
    assert convert_to_flat_str('3[a]2[bc]') == 'aaabcbc'


def test_three():
    assert convert_to_flat_str('2[a2[b]]') == 'abbabb'


def test_four():
    assert convert_to_flat_str('2[a2[b2[c]]]') == 'abccbccabccbcc'