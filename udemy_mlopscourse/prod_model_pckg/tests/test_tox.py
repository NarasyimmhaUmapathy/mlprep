from typing import Optional
import pytest

h = [1,2,3,-4]

#@pytest.mark.parametrize("test_input,expected",

 #                        ([1,2,3],6),
  #                       ([4,5,6],15),
   #                       ([4,6,7],17)
 #)

@pytest.mark.xfail
def test_divide_by_zero():
     assert 1/0 == 1


def test_absolutes(absoluter):
    assert min(absoluter(h))>0

def test_summer(summer,absoluter):
    assert summer(absoluter(h))==10




