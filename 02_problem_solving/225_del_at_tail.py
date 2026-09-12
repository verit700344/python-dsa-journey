from shapely import node


class Node:
   def __init__(self,data):
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
# to remove tail node
current = head

if head is None:
    head = None
    tail = None

elif head.next is None:
    head = None
    tail = None

else:
    while current.next.next is not None:
        current = current.next

    current.next = None
    tail = current