def sum_of_multiples(limit, multiples):
    result_set = set()
    for i in range(1, limit):
        for factor in multiples:
            if factor != 0 and i % factor == 0:
                result_set.add(i)
    return sum(result_set)
