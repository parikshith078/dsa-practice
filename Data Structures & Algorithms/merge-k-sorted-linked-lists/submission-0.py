# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        return self.merge_sort(lists, 0, len(lists) -1 )
    
    def merge_sort(self, nodes: List[ListNode], start: int, end: int) -> Optional[ListNode]:
        if start == end:
            return nodes[start]
        
        mid = (end + start) // 2
        n1 = self.merge_sort(nodes, start, mid)
        n2 = self.merge_sort(nodes, mid+1, end)

        return self.merge(n1, n2)
    
    def merge(self, n1: ListNode, n2: ListNode) -> Optiona[ListNode]:
        dummy = tail = ListNode()
        while n1 and n2:
            if n1.val <= n2.val:
                tail.next = n1
                n1 = n1.next
            else:
                tail.next = n2
                n2 = n2.next
            
            tail = tail.next
        
        while n1:
            tail.next = n1
            n1 = n1.next
            tail = tail.next
        while n2:
            tail.next = n2
            n2 = n2.next
            tail = tail.next
        
        tail.next = None

        return dummy.next


        