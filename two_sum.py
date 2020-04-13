def two_sum(_list, k):
    _hash = set()
    for num in _list:
        if num in _hash:
            return True
        _hash.add(k-num)
    return False
print(two_sum([4,7,1,-3,2], 80))