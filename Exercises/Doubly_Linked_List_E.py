class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class DoublyLinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_begining(self, data):
        node = Node(data, self.head, None)
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None, None)
            return

        itr = self.head

        while itr.next:
            itr = itr.next

        itr.next = Node(data, None, itr)
    
    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count+=1
            itr = itr.next

        return count
    
    def print_forward(self):
        itr = self.head
        while itr:
            print(f"{itr.data}-->", end="")
            itr = itr.next
        print()

    def print_backward(self):
        itr = self.head
        while itr.next:
            itr = itr.next
        while itr:
            print(f"{itr.data}-->", end="")
            itr = itr.prev
        print()




if __name__ == "__main__":
    ll = DoublyLinkedList()
    ll.insert_at_end(1)
    ll.insert_at_end(2)
    ll.insert_at_end(3)
    ll.insert_at_end(4)
    ll.print_forward()
    ll.print_backward()