from contextlib import contextmanager


def ListTx(l):
    copy = list(l)
    yield copy
    l[:] = copy
    print(l)
    return None

def changeList(l):
    l = [1,2,3]

l = [4,5,6]
changeList(l)
print(l)

# l -> mem 10,  100  ,  100 -> 4, 5, 6                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        ``
# changeList(l) -> mem 30, 200  (1, 2, 3)  