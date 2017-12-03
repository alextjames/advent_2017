import pytest
from captcha import sum_consecutive


@pytest.fixture(params=[
    ('1122', 3),
    ([1, 1, 2, 2], 3),
    ('21122', 5),
    ('1111', 4),
    ('91212129', 9),
])
def sequence(request):
    return request.param


@pytest.fixture(params=[
    ('1212', 6),
    ('1221', 0),
    ('123425', 4),
    ('123123', 12),
    ('12131415', 4),
])
def sequence_gap(request):
    return request.param


def test_captcha(sequence):
    assert sum_consecutive(sequence[0]) == sequence[1]


def test_captcha_gap(sequence_gap):
    assert sum_consecutive(sequence_gap[0], int(len(sequence_gap[0])/2)) == sequence_gap[1]

