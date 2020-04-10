class ListNode(object):
  def __init__(self, x):
    self.val = x
    self.next = None

class Solution:
  def addTwoNumbers(self, l1, l2):
    carry = 0
    result = ListNode(-44)
    ans = result
    while l1 or l2:
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0

        add_val = val1 + val2 + carry
        result.next = ListNode(add_val%10)
        result = result.next 
        carry = add_val//10

        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
    
    #if carry is left
    if carry == 1:
        result.next = ListNode(carry)
    
    return ans.next
    
l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)
l1.next.next.next = ListNode(9)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)
l2.next.next.next = ListNode(1)

result = Solution().addTwoNumbers(l1, l2)
while result:
  print(result.val)
  result = result.next