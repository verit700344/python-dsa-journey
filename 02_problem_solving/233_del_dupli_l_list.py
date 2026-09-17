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
class Node:
   def __init__(self,data):
       self.data = data
       self.next = None
numbers = list(map(int, input("Enter numbers: ").split()))
head = None
tail = None
n = int(input("Enter n (position from end): "))
            
for number in numbers:
   new_node = Node(number)
   if head is None:
       head = new_node
       tail = new_node
   else:
       tail.next = new_node
       tail = new_node
current = head
while current is not None and current.next is not None:
    if current.data == current.next.data:
        current.next = current.next.next
    else:
        current = current.next
print("Linked list after removing duplicates:")
current = head

while current is not None:
    print(current.data, end=" → ")
    current = current.next

print("None")