import pytest

from main import RowingBoat, Paddle

TEST_MAX_WEIGHT = 100
TEST_TOTAL_HOOKS = 2

@pytest.fixture()
def generic_boat():
    return RowingBoat(TEST_MAX_WEIGHT, TEST_TOTAL_HOOKS)

class MockPaddle(Paddle):

    rowed = 0

    def row(self):
        MockPaddle.rowed += 1

def test_boat_launch(generic_boat):
    generic_boat.in_water = True
    assert generic_boat.is_afloat()

def test_boat_load(generic_boat):
    generic_boat.in_water = True
    generic_boat.add_weight(42)
    assert generic_boat.is_afloat()

def test_boat_overload(generic_boat):
    generic_boat.in_water = True
    generic_boat.add_weight(100500)
    assert not generic_boat.is_afloat()

def test_boat_paddle(generic_boat):
    generic_boat.add_paddle(Paddle())
    assert TEST_TOTAL_HOOKS - 1 == generic_boat.get_current_free_hooks()

def test_sailing(generic_boat):
    generic_boat.add_paddle(MockPaddle())
    generic_boat.add_paddle(MockPaddle())
    generic_boat.in_water = True
    generic_boat.add_weight(42)
    generic_boat.sail(5)
    assert MockPaddle.rowed > 0