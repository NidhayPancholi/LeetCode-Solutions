# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return None
        if not list1:
            output=list2
            temp2=list2.next
            temp1=None
        elif not list2:
            output=list1
            temp1=list1.next
            temp2=None
        elif list1.val<list2.val:
            output=list1
            temp1=list1.next
            temp2=list2
        else:
            output=list2
            temp2=list2.next
            temp1=list1
        last_node=output
        while temp1 and temp2:
            if temp1.val<temp2.val:
                last_node.next=temp1
                temp1=temp1.next
                last_node=last_node.next
            else:
                last_node.next=temp2
                temp2=temp2.next
                last_node=last_node.next
        if temp1 and not temp2:
            while temp1:
                last_node.next=temp1
                temp1=temp1.next
                last_node=last_node.next
        elif temp2 and not temp1:
            while temp2:
                last_node.next=temp2
                temp2=temp2.next
                last_node=last_node.next    
        return output
                
        
        
            
        
        