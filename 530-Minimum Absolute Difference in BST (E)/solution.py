# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getRightMost(self, root: Optional[TreeNode]):
        if root == None:
            return None

        if root.right != None:
            return self.getRightMost(root.right)
        elif root.right == None:
            return root.val

    def getLeftMost(self, root: Optional[TreeNode]):
        if root == None:
            return None

        if root.left != None:
            return self.getLeftMost(root.left)
        elif root.left == None:
            return root.val

    def getMinimumDifferenceHelper(self, root: Optional[TreeNode]) -> int:
        diffs_list = []

        if(root == None):
            return []

        if (root.left != None):
            diffs_list += [root.val - root.left.val]

            right_most = self.getRightMost(root.left)

            if (right_most!= None):
                diffs_list += [root.val - right_most]

        if (root.right != None):
            diffs_list += [root.right.val - root.val]

            left_most = self.getLeftMost(root.right)

            if (left_most!= None):
                diffs_list += [left_most - root.val]

        diffs_list += self.getMinimumDifferenceHelper(root.left) + self.getMinimumDifferenceHelper(root.right)

        return diffs_list

    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        if (root.left == None and root.right == None):
            return 0

        return min(self.getMinimumDifferenceHelper(root))
        
        