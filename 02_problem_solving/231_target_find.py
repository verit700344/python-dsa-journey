class Node:
   def __init__(self,data):
       self.data = data
       self.next = None
numbers = list(map(int, input("Enter numbers: ").split()))
head = None
tail = None
target = int(input("Enter target number: "))
            
for number in numbers:
   new_node = Node(number)
   if head is None:
       head = new_node
       tail = new_node
   else:
       tail.next = new_node
       tail = new_node
current = head

while current is not None:
    if current.data == target:
        print("Target number found in the linked list.")
        break

    current = current.next
else:
    print("Target number not found in the linked list.")