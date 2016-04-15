def BinarySearch(list, first, last, item_sought):
    item_found = False
    search_failed = False
    while not item_found:
        midpoint = (first + last) / 2
        if list[midpoint] = item_sought:
            item_found = True
        else:
            if first >= last:
                search_failed = True
            else:
                if list[midpoint] > item_sought
