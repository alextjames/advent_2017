import click
from itertools import tee, cycle, islice


def sum_consecutive(numbers, gap=1):

    if type(numbers) == str:
        numbers = [int(c) for c in numbers]

    total = 0

    # Get a second iterator to numbers
    itr1, itr2 = tee(numbers)

    # Advance by the gap
    itr2 = cycle(itr2)
    [next(itr2) for _ in range(0, gap)]

    for i, j in zip(itr1, itr2):
        if i == j:
            total += i

    return total


@click.command()
@click.option('--numbers')
@click.option('--half/ --no_half', default=False)
def cli(numbers, half):

    print(sum_consecutive(numbers, 1 if not half else int(len(numbers)/2)))


if __name__ == '__main__':
    cli()


