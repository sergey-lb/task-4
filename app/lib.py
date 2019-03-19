def uniq(data):
    """
    >>> uniq([2, 15, 28, 100, 2, 0, 15, 1])
    [28, 100, 0, 1]
    """
    result = []

    for datum in data:
        number_of_occurrences = data.count(datum)
        if(number_of_occurrences == 1):
            result.append(datum)

    return result
