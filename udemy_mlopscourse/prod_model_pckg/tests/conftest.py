import pytest
import math

@pytest.fixture(scope='session') #function runs once and gets cached
def absoluter(c:list[int]) -> list[int]:
    absoluted = [math.fabs(i) for i in c]
    return absoluted

@pytest.fixture(scope='session')
def summer(d:list[int]):
    summed = sum(d)
    return summed




