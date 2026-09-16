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
current = head
count = 0
while current is not None:
    count += 1
    current = current.next
print("Number of nodes in the linked list is:", count)