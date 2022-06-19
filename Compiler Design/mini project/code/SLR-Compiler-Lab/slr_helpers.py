# first and follow


from global_vars import grammar, nonterms, terms


def get_first(symbol, seen_syms=None):
    if seen_syms is None:
        seen_syms = []

    first_syms = []

    if symbol not in seen_syms:
        seen_syms.append(symbol)

    if symbol in terms:  # For terminal symbols
        first_syms.append(symbol)
    elif symbol in nonterms:  # For nonterminal symbols
        for prod in grammar[symbol]:
            if prod[0] in terms and prod[0] not in first_syms:
                first_syms.append(prod[0])
            elif prod[0] in nonterms:
                if prod[0] not in seen_syms:
                    first_syms += [
                        term for term in get_first(prod[0], seen_syms)
                        if term not in first_syms
                    ]

    return first_syms


def get_follow(symbol, start, seen_syms=None):
    if seen_syms is None:
        seen_syms = []

    follow_syms = []

    if symbol not in seen_syms:
        seen_syms.append(symbol)

    if symbol == start:  # Add $ to follow set of start symbol
        follow_syms.append('$')

    for head, prods in grammar.items():
        for prod in prods:
            to_follow = False

            if symbol in prod:
                next_sym_pos = prod.index(symbol) + 1

                if next_sym_pos < len(prod):
                    follow_syms += [
                        term for term in get_first(prod[next_sym_pos])
                        if term not in follow_syms
                    ]
                else:
                    to_follow = True

                if to_follow and (head not in seen_syms):
                    follow_syms += [
                        term for term in get_follow(head, start, seen_syms)
                        if term not in follow_syms
                    ]

    return follow_syms


def get_closure(items):
    closure = {**items}

    while True:
        item_len = len(closure) + sum(len(v) for v in closure.values())

        for head in list(closure):
            for prod in closure[head]:
                dot_pos = prod.index('.')

                # Checks whether or not item final

                if dot_pos + 1 >= len(prod):
                    continue

                # Item not final
                prod_after_dot = prod[dot_pos + 1]

                if prod_after_dot not in nonterms:
                    continue

                for prd in grammar[prod_after_dot]:
                    itm = ['.'] + prd

                    if prod_after_dot not in closure:
                        closure[prod_after_dot] = [itm]
                    elif itm not in closure[prod_after_dot]:
                        closure[prod_after_dot].append(itm)

        if item_len == len(closure) + sum(len(v) for v in closure.values()):

            return closure
