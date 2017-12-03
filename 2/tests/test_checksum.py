import pytest
from checksum import checksum, checksum_min_max, checksum_divisable


@pytest.fixture(params=[
    ("""5 1 9 5
    7 5 3
    2 4 6 8""", 18)
])
def spreadsheet(request):
    return request.param


@pytest.fixture(params=[
    ("""5 9 2 8
        9 4 7 3
        3 8 6 5""", 9)
])
def spreadsheet_div(request):
    return request.param


def test_checksum_min_max(spreadsheet):
    assert checksum(spreadsheet[0], checksum_min_max) == spreadsheet[1]


def test_checksum_divisable(spreadsheet_div):
    assert checksum(spreadsheet_div[0], checksum_divisable) == spreadsheet_div[1]
