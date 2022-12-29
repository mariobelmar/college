from statistics import median
from math import floor




def medianne(ll: list[int]) -> int:
    """
    if even: e.g. l = [1, 7, 6, 0]
                          ^  ^
                          L  R
                          1  2
      median = (L + R)/2
    else:
      # e.g. l = [2, 6, 6 , 30, 5]
                        ^
                        C idx:2
      len(l)/2 == 2.5
      floor(2.x) == 2
      median = l[floor(len(l)/2)]
    """
    liste = ll.copy()
    liste.sort()
    size = len(liste)
    if size % 2 == 0:
        R_idx = int((size / 2))
        L_idx = int((size / 2) - 1)
        median = (liste[L_idx] + liste[R_idx]) / 2
    else:
        mid = int(floor(size/2))
        median = liste[mid]

    return median


if __name__ == '__main__':

    liste = [1, 7, 6 , 0]
    liste = [2, 6, 6 , 30, 5]
    liste = [2, 4 ,3, 6, 6 ,3 ,7, 10, 30, 2]
    liste = [2, 4 ,3, 6, 6 ,3, 1, 3, 7, 10, 30, 2, 2400]

    print(liste)
    print(f'mine :{medianne(liste)}')
    print(f'stat: {median(liste)}')
    print(liste)
