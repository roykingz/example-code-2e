from tree import tree


def test_1_level():
    class One: pass
    expected = [('One', 0)]
    result = list(tree(One))
    print(result)
    assert expected == result


def test_2_levels_2_leaves():
    class Branch: pass
    class Leaf1(Branch): pass
    class Leaf2(Branch): pass
    expected = [
        ('Branch', 0),
            ('Leaf1', 1),
            ('Leaf2', 1),
    ]
    result = list(tree(Branch))
    print(result)
    assert expected == result

if __name__ == '__main__':
    test_1_level()
    test_2_levels_2_leaves()