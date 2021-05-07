from hello import add, my_sub


def test_add():
    assert 2 == add(1, 1)

def test_sub():
    assert 0 == my_sub(1, 1) 