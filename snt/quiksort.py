ll = [7, 2, 9, 8, 0, 7, 12, 3, 53, 32, 4]


def qs(ll):
    if ll == []:
        return []
    center = ll.pop()
    left = [s for s in ll if s <= center]
    right = [ i for i in ll if i > center]
    return qs(left) + [center] + qs(right)

print(ll)
print(qs(ll))

