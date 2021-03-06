import click
from collections import namedtuple
from math import sqrt, ceil

Coord = namedtuple('Coord', ['x', 'y'])


def spiral_distance(addr):
    x, y = spiral_coords(addr)
    return abs(x) + abs(y)


def spiral_coords(addr):

    if addr == 1:
        return 0, 0

    side_size = ceil(sqrt(addr))
    side_size = side_size if side_size % 2 else side_size + 1
    layer = int(side_size / 2)
    prev_max = pow(side_size - 2, 2)
    max_in_layer = pow(side_size, 2)

    index_in_layer = addr - prev_max
    layer_size = max_in_layer - prev_max
    index_in_layer = index_in_layer % layer_size

    quadrant, quadrant_index = divmod(index_in_layer, int((layer_size / 4)))
    in_layer_distance = quadrant_index - layer
    distnace_to_layer = layer

    if quadrant == 0:
        return Coord(distnace_to_layer, in_layer_distance)
    elif quadrant == 1:
        return Coord(-in_layer_distance, distnace_to_layer)
    elif quadrant == 2:
        return Coord(-distnace_to_layer, -in_layer_distance)
    elif quadrant == 3:
        return Coord(in_layer_distance, -distnace_to_layer)

    raise RuntimeError('Did not compute correct quadrant {} / {} = {}'.format(index_in_layer, layer_size / 4, quadrant))


def spiral_value(input):
    mem = {
        Coord(0, 0): 1
    }
    value = 1
    i = 1

    while value <= input:
        i += 1
        coords = spiral_coords(i)
        value = 0
        value += mem.get(Coord(coords.x + 1, coords.y + 0), 0)
        value += mem.get(Coord(coords.x + 1, coords.y + 1), 0)
        value += mem.get(Coord(coords.x + 0, coords.y + 1), 0)
        value += mem.get(Coord(coords.x - 1, coords.y + 1), 0)
        value += mem.get(Coord(coords.x - 1, coords.y + 0), 0)
        value += mem.get(Coord(coords.x - 1, coords.y - 1), 0)
        value += mem.get(Coord(coords.x - 0, coords.y - 1), 0)
        value += mem.get(Coord(coords.x + 1, coords.y - 1), 0)
        mem[coords] = value

    return value


@click.command()
@click.option('--addr', type=int)
@click.option('--value', type=int)
def cli(addr, value):
    if addr:
        print('Distance {}'.format(spiral_distance(addr)))

    if value:
        print('Value {}'.format(spiral_value(value)))


if __name__ == '__main__':
    cli()



