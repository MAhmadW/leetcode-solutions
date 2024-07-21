# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        def getChildrenAverage(parents: List[TreeNode]):
            total = 0
            count = 0

            children = []
            for parent in parents:
                if parent == None:
                    continue

                if (parent.left != None):
                    children += [parent.left]
                    total += parent.left.val
                    count += 1

                if (parent.right != None):
                    children += [parent.right]
                    total += parent.right.val
                    count += 1
            
            if (count == 0):
                return []

            return [total/count] + getChildrenAverage(children)

        return [root.val] + getChildrenAverage([root])