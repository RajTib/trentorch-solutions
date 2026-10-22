def is_truthy(value) -> bool:
    """
    Return the truthiness of `value` exactly as Python's own
    rules would determine it (equivalent to bool(value), but
    implement the logic explicitly rather than calling bool()
    directly, handle None, numbers, strings, lists, tuples,
    dicts, and sets).
    """

    falsy = [False, None, 0, 0.0, "", [], (), {}, set()]
    if value not in falsy:
        return True
    else:
        return False
    pass


def first_truthy(values: list):
    """
    Return the first value in `values` that is truthy. If no
    value in the list is truthy, return None.
    Do not use Python's built-in `any()`, implement the scan
    explicitly using is_truthy-style checks.
    """

    falsy = [False, None, 0, 0.0, "", [], (), {}, set()]
    for i in range(len(values)):
        if values[i] not in falsy:
            return values[i]
    return None
    
    pass
