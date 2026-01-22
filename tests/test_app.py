from app import add

def test_add():
    # Indented 4 spaces
    assert add(2, 3) == 5
    assert add(-1, 1) == 0