
def givenString():
    string = input('Give string: ')
    final = acceptString(dfa, 0, {2}, string)

    if final:
        print('String is accepted')
    else:
        print('String is not accepted')


def acceptString(t, i, a, s):
    state = i
    for x in s:
        state = t[state][x]
    return state in a


dfa = {
    0: {'0': 3, '1': 1},
    1: {'1': 1, '0': 2},
    2: {'0': 2, '1': 1},
    3: {'0': 3, '1': 3},
}

# FUNCTION CAll
givenString()
