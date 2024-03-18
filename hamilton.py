from math import log10, ceil

"""
the idea:
every time a bit is introduced,
take the previously made list
and flip it with the new bit,
which makes it never cycle back
until every added bit that's introduced
has all earlier bit permutations put
into the cycle.

this makes every following list the basis of the one before it,
so then take the final product made and print it
"""


def print_hypercube_hamiltonian_cycle(n):
    if n <= 1:
        return
    built_lists = [[] for _ in range(n)]
    built_lists[0] = [0, 1]
    built_lists[1] = [0, 1, 11, 10]

    for i in range(n - 2):
        built_lists[i + 2] = built_lists[i + 1] + [x + (10 ** (i + 2)) for x in built_lists[i + 1]][::-1]

    for i in built_lists[n - 1]:
        if i == 0:
            print("{" + "0" * n + ",", end='')  # starts off at here
            continue
        expand = "0" * ceil(n - log10(i) - 1) + str(i)
        print(" " + expand + "}")  # places second vertex of edge
        print("{" + expand + ",", end='')  # sets up next edge
    print(" " + "0" * n + "}")


print_hypercube_hamiltonian_cycle(5)

