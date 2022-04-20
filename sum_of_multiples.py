def sum_of_multiples(limit, multiples):
    return sum({i for f in multiples if f for i in range(f, limit, f)})
