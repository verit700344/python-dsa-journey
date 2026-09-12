class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
numbers = list(map(int, input("Enter numbers to insert at the tail: ").split()))
head = None
tail = None
for number in numbers:
    new_node = Node(number)
    if head is None:
        head = new_node
        tail = new_node
    else:
       tail.next = new_node
       tail = new_node

# to delete at new node head

if head is not None:
    head = head.next
