def sum_of_multiples(limit, multiples):
    return sum(
        {
            i
            for i in range(1, limit)
            for factor in multiples
            if factor != 0 and i % factor == 0
        }
    )
