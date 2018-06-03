
def bin_search(list,item):
    low = 0
    high = len(list)-1

    while low <= high:
        mid = (low + high)
        guess = list[mid]
        if guess == item:
            return (mid+1)
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

