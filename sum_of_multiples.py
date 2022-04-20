def sum_of_multiples(limit, multiples):
    return sum({i for i in range(1, limit) for f in multiples if f != 0 and i % f == 0})
