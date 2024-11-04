# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        """
        Calculates the number of paths that sum up to targetSum.
        
        :param root: The root of the binary tree.
        :param targetSum: The target sum for each path.
        :return: The count of paths that sum to targetSum.
        """
        if not root:
            return 0
        # Count paths starting from this node, and count in left and right subtrees
        return self.process(root, targetSum) + self.pathSum(root.left, targetSum) + self.pathSum(root.right, targetSum)
    
    def process(self, node: Optional[TreeNode], t: int) -> int:
        """
        Counts paths that start from the given node and sum up to t.
        
        :param node: The starting node of the current path.
        :param t: The remaining target sum for this path.
        :return: The count of paths starting from node that sum to t.
        """
        if not node:
            return 0
        
        # Check if the current node completes a path with the required sum
        count = 1 if node.val == t else 0
        
        # Recursively count paths in the left and right subtrees with the updated target sum
        count += self.process(node.left, t - node.val)
        count += self.process(node.right, t - node.val)
        
        return count
