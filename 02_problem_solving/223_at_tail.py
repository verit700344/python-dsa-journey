class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
numbers = list(map(int, input("Enter numbers: ").split()))
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

# to insert at new node head
new_node = Node(int(input("Enter a number to insert at the head: ")))

new_node.next = head

head = new_node