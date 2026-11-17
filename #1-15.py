def zip_lists(*lists, fill=None):
    if len(lists) == 0:
        return []

    max_len = 0
    for list in lists:
        if len(list) > max_len:
            max_len = len(list)

    result = []
    for i in range(max_len):
        num = []
        for list in lists:
            if i < len(list):
                num.append(list[i])
            else:
                num.append(fill)
        result.append(tuple(num))
    return result
print(zip_lists([2, 3], [1], fill=None))
