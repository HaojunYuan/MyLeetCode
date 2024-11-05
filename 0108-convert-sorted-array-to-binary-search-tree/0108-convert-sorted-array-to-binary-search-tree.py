# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.process(nums)
    
    def process(self, nums):
        if not nums:
            return
        rootIndex = len(nums) // 2
        root = TreeNode(nums[rootIndex])
        root.left = self.process(nums[:rootIndex])
        root.right = self.process(nums[rootIndex + 1:])
        return root