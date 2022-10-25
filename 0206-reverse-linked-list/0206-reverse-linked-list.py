# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        stack=[]
        temp=[]
        t=head
        
        while t:
            temp.append(t)
            stack.append(t.val)
            t=t.next
        
        for x in temp:
            x.val=stack.pop()
        return head
        