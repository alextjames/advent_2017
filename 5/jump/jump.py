import click


def traverse_jumps(jumps):
    i = 0
    steps = 0

    while 0 <= i < len(jumps):
        step = jumps[i]
        jumps[i] += 1
        i = i + step
        steps += 1

    return steps


def traverse_jumps_negative(jumps):
    i = 0
    steps = 0

    while 0 <= i < len(jumps):
        step = jumps[i]

        if step >= 3:
            jumps[i] -= 1
        else:
            jumps[i] += 1

        i = i + step
        steps += 1

    return steps


@click.command()
@click.option('--input_file', type=click.File())
@click.option('--negative', default=False, is_flag=True)
def cli(input_file, negative):
    if negative:
        print(traverse_jumps_negative([int(jump.strip()) for jump in input_file.read().split('\n') if len(jump.strip())]))
    else:
        print(traverse_jumps([int(jump.strip()) for jump in input_file.read().split('\n') if len(jump.strip())]))


if __name__ == '__main__':
    cli()

