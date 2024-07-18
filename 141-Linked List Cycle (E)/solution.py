# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr_node = head

        node_dict = {}

        while (curr_node):

            node_repetitions = node_dict.get(curr_node,None)
            
            
            if not node_repetitions:
                node_dict[curr_node] = 1
            else:
                return True

            

            curr_node = curr_node.next

        return False
        