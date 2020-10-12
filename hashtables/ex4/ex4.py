def has_negatives(a):
    """
    YOUR CODE HERE
    """
    result = []
    ht = {}
    for val in a:
        if (absval := abs(val)) not in ht.keys():
            ht[absval] = 0
        else:
            result.append(absval)

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
