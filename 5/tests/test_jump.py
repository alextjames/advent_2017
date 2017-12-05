import pytest
from jump.jump import traverse_jumps, traverse_jumps_negative


@pytest.fixture(params=[
    ('0 3 0 1 -3', 5, 10)
])
def jump_path(request):
    return request.param


def test_jump_path(jump_path):
    assert traverse_jumps([int(jump) for jump in jump_path[0].split()]) == jump_path[1]


def test_jump_path_negative(jump_path):
    assert traverse_jumps_negative([int(jump) for jump in jump_path[0].split()]) == jump_path[2]
