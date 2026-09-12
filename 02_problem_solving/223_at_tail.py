class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
numbers = list(map(int, input("Enter numbers: ").split()))
head = None
tail = None
for number in numbers:
    new_node = Node(number)
    if tail is None:
        tail = new_node
        head = new_node
    else:
       head.next = new_node
       head = new_node

# to insert at new node head
new_node = Node(int(input("Enter a number to insert at the head: ")))

new_node.next = tail
tail = new_node