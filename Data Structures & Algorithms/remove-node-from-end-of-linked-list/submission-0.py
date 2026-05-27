# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #you have a head to a list
        ptr = head
        #find the length of the list
        length = 0
        while ptr:
            length+=1
            ptr = ptr.next

        #consider cases:
        # 1) if the list is empty, then return head... do nothing
        # 2) if n = 1, and length = 1, then return []
        # 2) if the n = length... then you are deleting at the beginning of the list
        # 3) if the n = 0... then you are deleting at the end of the list..
        # 4) if else, then it is the middle of the list... delete between 2 nodes...
        if not head: #case 1
            return head #placeholder

        ptr = head
        prev = None

        if length == 1:
            return None
        if n == 1: #end
            while ptr.next:
                prev = ptr
                ptr = ptr.next
            prev.next = None
        elif n == length:
            head = head.next
        else:
            num = length + 1 - n
            for i in range(1, num):
                prev = ptr
                ptr = ptr.next
            prev.next = ptr.next
        return head
