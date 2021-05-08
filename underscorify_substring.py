def underscorify_substring(string, substring):
    start_end_pairs = tuple(
        (start, end)
        for start in range(len(string))
        if substring == string[start: (end := start + len(substring))]
    )

    underscore_indices = []
    i = 0
    while i < len(start_end_pairs):

        start, end = start_end_pairs[i]

        last_used_j = None
        # start with the next pair
        j = i + 1
        while j < len(start_end_pairs):
            start_prime, end_prime = start_end_pairs[j]
            # start_prime == end would mean: testtest
            # Let's collapse these two instances.
            if start_prime <= end:
                end = end_prime
                last_used_j = j
            j += 1
        underscore_indices.extend((start, end))
        i = i + 1 if last_used_j is None else last_used_j + 1
        pass

    u = 0
    result = []
    for i in range(len(string)):
        if u < len(underscore_indices) and i == underscore_indices[u]:
            result.append('_')
            u += 1
        result.append(string[i])

    if u < len(underscore_indices):
        result.append('_')

    return ''.join(result)
