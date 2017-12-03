import click


def checksum_min_max(line):
    return max(line) - min(line)


def checksum_divisable(line):
    for dividend_idx, dividend in enumerate(line):
        for divisor_idx, divisor in enumerate(line):
            if dividend_idx == divisor_idx:
                continue

            result, mod = divmod(dividend, divisor)
            if not mod:
                return result

    raise RuntimeError('There were no divisable numbers on this line')


def checksum(spreadsheet, checksum_func):
    numbers = [[int(i) for i in line.split()] for line in spreadsheet.split('\n') if len(line.strip())]
    diffs = [checksum_func(line) for line in numbers]
    return sum(diffs)


@click.group()
def cli():
    pass


@click.command()
@click.option('--sheet', type=click.File())
def min_max(sheet):
    print(checksum(sheet.read(), checksum_min_max))


@click.command()
@click.option('--sheet', type=click.File())
def divisable(sheet):
    print(checksum(sheet.read(), checksum_divisable))


cli.add_command(min_max)
cli.add_command(divisable)

if __name__ == '__main__':
    cli()




