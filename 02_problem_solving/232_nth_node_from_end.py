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
first = head
second = head
for _ in range(n):
    first = first.next
while first is not None:
        first = first.next
        second = second.next
print("Nth node from end:", second.data)