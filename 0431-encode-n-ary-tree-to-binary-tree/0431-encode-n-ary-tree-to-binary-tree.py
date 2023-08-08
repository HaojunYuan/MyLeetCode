"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""

class Codec:
    # Encodes an n-ary tree to a binary tree.
    def encode(self, root: 'Optional[Node]') -> Optional[TreeNode]:
        if not root:
            return root
        head=TreeNode(root.val)
        head.left=self.en(root.children)
        return head
    
    def en(self, children):
        head=None
        curr=None
        for child in children:
            tNode=TreeNode(child.val)
            if not head:
                head=tNode
            else:
                curr.right=tNode
            curr=tNode
            curr.left=self.en(child.children)
        return head
	
	# Decodes your binary tree to an n-ary tree.
    def decode(self, root: Optional[TreeNode]) -> 'Optional[Node]':
        if not root:
            return root
        return Node(root.val, self.de(root.left))
    def de(self, root):
        children=[]
        while root:
            curr=Node(root.val,self.de(root.left))
            children.append(curr)
            root=root.right
        return children

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(root))