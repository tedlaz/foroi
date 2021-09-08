def split2list(val, alist) -> list:
    """Splits val according to alist values

    :param val: Value to be splitted
    :param alist: List of values
    :return: List of splitted val with length = len(alist) + 1
    100, [10, 10, 10] -> [10, 10, 10, 70]
    """
    lval = []
    rest = val
    for step in alist:
        if rest > step:
            lval.append(step)
            rest -= step
        else:
            lval.append(rest)
            rest = 0
    lval.append(rest)
    return lval


def klimaka(value, scale, percent):
    """Calculate percent of value given scale, percent rate

    :param value: Decimal value
    :param scale:  list of decimal values
    :param percent:  List of decimal values
    :return: Calculated value
    """
    if (len(scale) + 1) != len(percent):
        raise ValueError
    dpercent = [i / 100.0 for i in percent]
    vall = split2list(value, scale)
    pval = [vall[i] * dpercent[i] for i in range(len(percent))]
    return round(sum(pval), 2)


def distribute(*, val, dist):
    """Distributes value according to alist
    :param value: Value to be distributed
    :param dist: Distribution list / tuple
    :return: Distribution list
    """
    # value = dec(value, decimals)
    val = round(val, 2)
    totald = sum(dist)
    dist = [round(val * i / totald, 2) for i in dist]
    rest = val - round(sum(dist), 2)  # if there is a rest
    dist[dist.index(max(dist))] += rest  # add it to max value
    assert round(sum(dist), 2) == val  # For safety purposes
    return dist


def dic_print(dic, format="%-30s: %12s") -> str:
    """Print dictionary's keys : values

    :param dic: Dictionary to be printed
    :param format: Format string
    :return: string of formatted pairs
    """
    return "\n".join(format % (i, j) for i, j in dic.items())


def relu(*, val, threshold=0):
    """
          /
         /
    ____/
    """
    return threshold if val < threshold else val


def limit(*, val, limit):
    """
       __________  όριο
      /
     /
    /
    """
    return val if val < limit else limit
