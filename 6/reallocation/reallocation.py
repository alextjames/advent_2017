from itertools import cycle, takewhile


def reallocation(banks):
    prev_states = []
    cycles = 0

    while banks not in prev_states:
        # Add current state to prev states
        prev_states.append(list(banks))
        cycles += 1

        # Find the max element
        max_bank = max(banks)

        # Find the max element
        index_of_max = banks.index(max_bank)
        banks[index_of_max] = 0

        # Create cycle of indexes
        indexes = cycle(range(0, len(banks)))

        for _ in range(0, index_of_max + 1):
            next(indexes)

        for i in range(0, max_bank):
            banks[next(indexes)] += 1

    return cycles, cycles - prev_states.index(banks)










