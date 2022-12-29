from statistics import median


liste = [2, 4 ,3, 6, 6 ,3 ,7, 10, 30, 2]
liste = [2, 6, 6 , 30, 5]
liste = [1, 7, 6 , 0]


def medianne(ll: list[int]) -> int:
    """
    if even: e.g. l = [1, 7, 6, 0]
      median = (L + R)/2
      L = xxx
      R = xxx
    else:  # e.g. l = [2, 6, 6 , 30, 5]
      median = l[floor(len(l)/2)]
    """
    liste = ll.copy()
    liste.sort()
    size = len(liste)


    mid = int(size/2)
    mid1 = mid + 1
    # if even
    if not size % 2 == 0:
        mid = int((liste[mid] + liste[mid1]) / 2)
    # if odd

    return liste[mid]


if __name__ == '__main__':
    print(liste)
    print(f'mine :{medianne(liste)}')
    print(f'stat: {median(liste)}')
    print(liste)
