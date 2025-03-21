import sys
sys.path.append("D:/work/WHPython/stilsoft/fullstack/code_base/12_2/src")
from src.divide import divide

def test_divide():
    assert divide(10,5) == 2
    assert divide(20,5) == 4

def test_divide_division_zero():
    pass