class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def append(listA, listB):
    return Node(listA.data, append(listA.next, listB)) if listA else listB