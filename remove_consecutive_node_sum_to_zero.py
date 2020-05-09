class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

def removeConsecutiveSumTo0(node):
    dummy = Node(0)
    dummy.next = node
    temp_head = dummy 
    sum_dict, cum_sum = {}, 0
    while dummy:
        cum_sum += dummy.value
        sum_dict[cum_sum] = dummy 
        dummy = dummy.next 
    cum_sum = 0
    head = temp_head
    while head:
        cum_sum += head.value
        head.next = sum_dict[cum_sum].next
        head = head.next
    return temp_head.next




node = Node(10)
node.next = Node(5)
node.next.next = Node(-3)
node.next.next.next = Node(-3)
node.next.next.next.next = Node(1)
node.next.next.next.next.next = Node(4)
node.next.next.next.next.next.next = Node(-4)
node = removeConsecutiveSumTo0(node)
while node:
  print(node.value)
  node = node.next