# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return None
        
        while head and head.val == val:
            head = head.next
        
        cur = head
        pre = None


        while cur:
            if cur.val == val:
                pre.next = cur.next
                cur = cur.next
            else:
                pre = cur
                cur = cur.next
                
        return head
        
