def intersection(a, b):
    _hashset = set()
    while a or b:
        if a.val in _hashset:
            return a
        if b.val in _hashset:
            return b
        _hashset.add(a.val)
        _hashset.add(b.val)
        a = a.next if a.next else None
        b = b.next if b.next else None

class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None
    def prettyPrint(self):
        c = self
        while c:
            print(c.val)
            c = c.next

a = Node(1)
a.next = Node(2)
a.next.next = Node(3)
a.next.next.next = Node(4)
b = Node(6)
b.next = a.next.next
c = intersection(a, b)
c.prettyPrint()
