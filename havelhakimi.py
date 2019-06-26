def warmup1(values: list):
    return [x for x in values if not x == 0]


def warmup2(values: list):
    return sorted([x for x in values], reverse=True)


def warmup3(n: int, values: list):
    return True if n > len(values) else False


def warmup4(n: int, values: list):
    result = []
    for x, y in enumerate(values):
        if (x + 1) <= n:
            result.append(y - 1)
        else:
            result.append(y)
    return result


def hh(values: list):
    if not warmup1(values):
        return True

    seq = warmup1(values)

    while True:
        if not warmup1(seq):
            return True
        seq = warmup1(seq)
        seq = warmup2(seq)
        n = seq[0]
        seq.remove(n)

        if warmup3(n, seq):
            return False
        seq = warmup4(n, seq)
