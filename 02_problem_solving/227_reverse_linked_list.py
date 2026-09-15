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
previous = None
current = head
while current.next is not None:
    next_node = current.next
    current.next = previous
    previous = current
    current = next_node
    old_head = head
tail = old_head
head = previous

