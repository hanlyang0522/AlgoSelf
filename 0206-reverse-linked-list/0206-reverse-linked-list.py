# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None

        target = ListNode()
        target_head = target

        li = []

        while head != None:
            li.append(head.val)
            head = head.next            

        for i in range(len(li)):
            target.val = li[-(1+i)]

            if i!=len(li)-1:
                target.next = ListNode()
                target = target.next

        return target_head