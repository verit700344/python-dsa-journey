class  Node :
   def __init__(self,data):
       self.data = data
       self.next = None
numbers = list(map(int, input("Enter numbers: ").split()))
head = None
tail = None
for number in numbers :
    new_node = Node(number)
    if head is None:
           head = new_node
           tail = new_node
    else:
           tail.next = new_node
           tail = new_node
k = int(input("Enter k: "))


previous_group_tail = None
current = head

while current is not None:

    # 1. Check whether k nodes remain
    check = current
    count = 0

    while check is not None and count < k:
        check = check.next
        count += 1

    if count < k:
        break

    # 2. Reverse this group
    previous = None
    group_tail = current

    for _ in range(k):
        next_node = current.next
        current.next = previous
        previous = current
        current = next_node

    # 3. Connect previous group to this group
    if previous_group_tail is None:
          head = previous
    else:
          previous_group_tail.next = previous

    previous_group_tail = group_tail

current = head

while current is not None:
    print(current.data, end=" ")
    current = current.next