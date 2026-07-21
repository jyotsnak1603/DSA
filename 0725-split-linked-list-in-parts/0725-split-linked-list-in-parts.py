# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        curr=head
        length=0
        while curr:
            length+=1
            curr=curr.next
        base_size= length//k
        remainder = length%k

        ans = []
        curr=head
        
        for i in range(k):
            part_head=curr
            current_part_size=base_size+(1 if i<remainder else 0)

            for _ in range(current_part_size-1):
                if curr:
                    curr=curr.next
            
            if curr:
                next_part = curr.next
                curr.next=None
                curr=next_part
            ans.append(part_head)
        return ans