class Node:
   def __init__(self,data):
       self.data = data
       self.next = None
numbers = list(map(int, input("Enter numbers: ").split()))
head = None
tail = None
value = int(input("Enter value to delete: "))
            
for number in numbers:
   new_node = Node(number)
   if head is None:
       head = new_node
       tail = new_node
   else:
       tail.next = new_node
       tail = new_node
if head is not None and head.data == value:
    head = head.next

    if head is None:
        tail = None

elif head is not None:
    current = head

    while current.next is not None:
        if current.next.data == value:
            if current.next == tail:
              tail = current
            current.next = current.next.next
            break
        current = current.next
#del problem6
