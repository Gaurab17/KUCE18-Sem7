from global_vars import grammar, nonterms, terms
from slr_parser import perform_action


def parse_input_string(start, error, parse_table):
    input_str = input('\nEnter Input String' +
                      '(Whitespaces is required in between lexemes): ')
    parse_str = (input_str + ' $').split()
    inp_ptr = 0
    stack = ['0']

    print(
        '\n+--------+----------------------------+----------------------------+----------------------------+'
    )
    print('|{:^8}|{:^28}|{:^28}|{:^28}|'.format('Step', 'Stack', 'Input',
                                                'Action'))
    print(
        '+--------+----------------------------+----------------------------+----------------------------+'
    )

    step = 1

    while True:
        curr_symbol = parse_str[inp_ptr]
        stack_top = int(stack[-1])
        stack_content = ''
        input_content = ''

        print('|{:^8}|'.format(step), end=' ')

        for i in stack:
            stack_content += i
        print('{:27}|'.format(stack_content), end=' ')
        i = inp_ptr

        while i < len(parse_str):
            input_content += parse_str[i]
            i += 1

        print('{:>26} | '.format(input_content), end=' ')

        step += 1
        action = perform_action(stack_top, curr_symbol, start, error,
                                parse_table)

        if '/' in action:
            print('{:^26}|'.format(action + '. Multiple conflicting actions.'))

            break

        if 's' in action:
            print('{:^26}|'.format(action))
            stack.append(curr_symbol)
            stack.append(action[1:])
            inp_ptr += 1
        elif 'r' in action:
            print('{:^26}|'.format(action))
            i = 0

            for head, prods in grammar.items():
                for prod in prods:
                    if i == int(action[1:]):
                        for _ in range(2 * len(prod)):
                            stack.pop()

                        state = stack[-1]
                        stack.append(head)
                        stack.append(
                            parse_table[int(state)][len(terms) +
                                                    nonterms.index(head)])
                    i += 1
        elif action == 'acc':
            print('{:^26}|'.format('Accepted'))

            break
        else:
            print('ERROR: Illegal symbol', curr_symbol, '|')

            break
    print(
        '+--------+----------------------------+----------------------------+----------------------------+'
    )
