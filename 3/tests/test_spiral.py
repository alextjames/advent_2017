import pytest
from spiral_mem import spiral_distance, spiral_coords, spiral_value


@pytest.fixture(params=[
    (1, 0),
    (12, 3),
    (23, 2),
    (1024, 31),
    (9, 2),
])
def spiral_distance_result(request):
    return request.param


def test_spiral_distance(spiral_distance_result):
    assert spiral_distance(spiral_distance_result[0]) == spiral_distance_result[1]


@pytest.fixture(params=[
    (1, (0, 0)),
    (12, (2, 1)),
    (23, (0, -2)),
])
def spiral_coord_result(request):
    return request.param


def test_spiral_coord(spiral_coord_result):
    assert spiral_coords(spiral_coord_result[0]) == spiral_coord_result[1]


@pytest.fixture(params=[
    (800, 806),
    (700, 747),
    (330, 351),
    (1, 2),
    (2, 4),
    (4, 5)
])
def spiral_value_result(request):
    return request.param


def test_spiral_value(spiral_value_result):
    assert spiral_value(spiral_value_result[0]) == spiral_value_result[1]

