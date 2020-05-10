import heapq
class Node(object):
  def __init__(self, val, next=None):
    self.val = val
    self.next = next

  def __str__(self):
    c = self
    answer = ""
    while c:
      answer += str(c.val)+" " if c.val else ""
      c = c.next
    return answer

def merge(lists):
    tempHead = dummyHead = Node(0)
    node_list = []
    for l in lists:
        if l:
            node_list.append((l.val, l))
    heapq.heapify(node_list)
    
    while node_list:
        val, head = heapq.heappop(node_list)
        dummyHead.next = Node(val)
        dummyHead = dummyHead.next
        head = head.next
        if head:
            heapq.heappush(node_list, (head.val, head))
    return tempHead.next


a = Node(1, Node(3, Node(5)))
b = Node(2, Node(4, Node(6)))
print(merge([a, b]))