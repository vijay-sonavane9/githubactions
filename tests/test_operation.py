from src.math_operation import add, sub

def test_add():
    assert add(2,3) == 5
    assert add(-1,1) == 0
    assert add(5,3) == 8
    #The keyword assert is used to check if the answer is correct. If the answer is wrong, the program will stop and say there's a problem.

def test_sub():
    assert sub(5,3) == 2
    assert sub(4,3) == 1
    assert sub(3,3) == 0
