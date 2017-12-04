import pytest
from passphrase.passphrase import validation


@pytest.fixture(params=[
    ('aa bb cc dd ee', True),
    ('aa bb cc dd aa', False),
    ('aa bb cc dd aaa', True),
    ('abcde fghij', True),
    ('abcde xyz ecdab', False),
    ('ia ab abc abd abf abj', True),
    ('iiii oiii ooii oooi oooo', True),
    ('oiii ioii iioi iiio', False),
])
def phrases_for_test(request):
    return request.param


def test_valid_pharses(phrases_for_test):
    if phrases_for_test[1]:
        assert phrases_for_test[0] in validation([phrases_for_test[0]])
    else:
        assert validation([phrases_for_test[0]]) == []

