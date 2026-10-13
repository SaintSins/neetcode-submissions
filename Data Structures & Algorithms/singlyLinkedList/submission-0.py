class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    
    def __init__(self):
        self.head = ListNode(-1)
        self.tail = self.head
    
    def get(self, index: int) -> int:
        if index < 0:
            return -1
        curr = self.head.next
        for _ in range(index):
            if not curr:
                break
            curr = curr.next
        if curr is None:
            return -1
        else:
            return curr.val

    def insertHead(self, val: int) -> None:
        new_node = ListNode(val)
        new_node.next = self.head.next
        self.head.next = new_node
        if not new_node.next:
            self.tail = new_node

    def insertTail(self, val: int) -> None:
        new_node = ListNode(val)
        self.tail.next = new_node
        self.tail = new_node

    def remove(self, index: int) -> bool:
        if index < 0:
            return False
        curr = self.head
        for _ in range(index):
            if not curr:
                break
            curr = curr.next
        if not curr or not curr.next:
            return False
        if curr.next == self.tail:
            self.tail = curr
        curr.next = curr.next.next
        return True

    def getValues(self) -> List[int]:
        values = []
        curr = self.head.next
        while curr:
            values.append(curr.val)
            curr = curr.next
        return values
