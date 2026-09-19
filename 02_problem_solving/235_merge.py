class  Node :
   def __init__(self,data):
       self.data = data
       self.next = None
numbers1 = list(map(int, input("Enter numbers: ").split()))
numbers2 = list(map(int, input("Enter numbers: ").split()))
head1 = None
tail1 = None
head2 = None
tail2 = None
for number in numbers1 :
    new_node = Node(number)
    if head1 is None:
           head1 = new_node
           tail1 = new_node
    else:
           tail1.next = new_node
           tail1 = new_node
for number in numbers2 :
    new_node = Node(number)
    if head2 is None:
           head2 = new_node
           tail2 = new_node
    else:
           tail2.next = new_node
           tail2 = new_node
current1 = head1
current2 = head2
merged_head = None
merged_tail = None
while current1 is not None and current2 is not None:

    if current1.data <= current2.data:
        selected = current1
        current1 = current1.next
    else:
        selected = current2
        current2 = current2.next

    if merged_head is None:
        merged_head = selected
        merged_tail = selected
    else:
        merged_tail.next = selected
        merged_tail = selected

if current1 is not None:
    merged_tail.next = current1
else:
    merged_tail.next = current2
if current1 is not None:
    merged_tail.next = current1
else:
    merged_tail.next = current2

current = merged_head

while current is not None:
    print(current.data, end=" ")
    current = current.next