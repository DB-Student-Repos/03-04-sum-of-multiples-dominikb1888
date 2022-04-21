def sum_of_multiples(limit, multiples):
    return sum({i for f in multiples if f for i in range(f, limit, f)})

def sum_of_multiples_lc(limit, multiples):
    return sum(
        {
            i
            for i in range(1, limit)
            for factor in multiples
            if factor != 0 and i % factor == 0
        }
    )

def sum_of_multiples_loop(limit, multiples):
    result_set = set()
    for i in range(1, limit):
        for factor in multiples:
            if factor != 0 and i % factor == 0:
                result_set.add(i)
    return sum(result_set)