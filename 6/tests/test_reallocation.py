from reallocation.reallocation import reallocation


def test_reallocation():
    assert reallocation([0, 2, 7, 0]) == (5, 4)


def test_problem_reallocation():
    problem = '0	5	10	0	11	14	13	4	11	8	8	7	1	4	12	11'
    cycles = reallocation([int(i) for i in problem.split()])
    assert cycles == (7864, 1695)
