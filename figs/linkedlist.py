class Node:
    data := 0
    next : Node = None

class LinkedList:
    root : Node = None

    def insert(self, value : int):
        old := self.root
        self.root = Node()
        self.root.data = value
        self.root.next = old

    def contains(self, value : int) -> bool:
        curr := self.root
        while curr != None:
            if value == curr.data:
                return True
            curr = curr.next
        return False

    # Other LinkedList methods omitted for brevity
