import pytest
from solver.main import Solver


@pytest.fixture(scope='module')
def solver():
    return Solver()
