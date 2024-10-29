# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # The second element in the returned tuple represents the maximum path sum in the tree
        return self.calculatePathSums(root)[1]
    
    def calculatePathSums(self, node: Optional[TreeNode]) -> (int, int):
        """
        Recursive helper function to calculate:
        - `max_single_path`: maximum path sum starting from the current node and extending downward to a leaf.
        - `max_path_sum`: maximum path sum considering paths that might pass through or not pass through the current node.
        
        Returns:
            Tuple (max_single_path, max_path_sum).
        """
        # Base case: If node is None, max single path is 0 and max path sum is negative infinity (no path exists).
        if not node:
            return 0, -math.inf
        
        # Recursively calculate values for left and right subtrees
        left_single_path, left_max_path_sum = self.calculatePathSums(node.left)
        right_single_path, right_max_path_sum = self.calculatePathSums(node.right)
        
        # Max path starting from this node and extending downward
        max_single_path = max(node.val, node.val + max(left_single_path, right_single_path), 0)

        # Maximum path sum for the subtree rooted at this node
        max_path_sum = max(left_max_path_sum, right_max_path_sum, node.val + left_single_path + right_single_path)
        
        # Return the maximum single path sum and the maximum path sum seen so far
        return max_single_path, max_path_sum