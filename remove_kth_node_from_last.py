class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
    def __str__(self):
        current_node = self
        result = []
        while current_node:
            result.append(current_node.val)
            current_node = current_node.next
        return str(result)

def remove_kth_from_linked_list(head, k):
    dummy_node = Node(-44) 
    dummy_node.next = head
    head_1 = head_2 = dummy_node
    while k>0:
        head_1 = head_1.next
        k -= 1
    while head_1:
        head_2 = head_2.next
        head_1 = head_1.next
        
    head_2.next = head_2.next.next
    return dummy_node.next

head = Node(1, Node(2, Node(3, Node(4, Node(5)))))
print(head)
# [1, 2, 3, 4, 5]
head = remove_kth_from_linked_list(head, 1)
print(head)
# [1, 2, 4, 5]