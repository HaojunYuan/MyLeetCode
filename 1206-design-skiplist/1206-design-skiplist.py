import random
class Node:
    def __init__(self, val = -1, right = None, down = None):
        self.val = val
        self.right = right
        self.down = down

# Create a dummy head node for each level
class Skiplist:
    def __init__(self):
        self.head = Node()
    
    def search(self, target: int) -> bool:
        cur = self.head
        while cur:
            # Move right if the next node is not None and its value is less than target
            while cur.right and cur.right.val < target:
                cur = cur.right
            if cur.right and cur.right.val == target:
                return True
            # Move down if the next node is None or its value is greater than target
            cur = cur.down
        return False
    
    def erase(self, num: int) -> bool:
        cur = self.head
        found = False
        while cur:
            # Move right if the next node is not None and its value is less than target
            while cur.right and cur.right.val < num:
                cur = cur.right
            if cur.right and cur.right.val == num:
                found = True
                cur.right = cur.right.right
            # Move down if the next node is None or its value is greater than target
            cur = cur.down
        return found
    
    def add(self, num: int) -> None:
        # Create a stack to store the nodes that need to be updated
        stack = []
        cur = self.head
        while cur:
            # Move right if the next node is not None and its value is less than target
            while cur.right and cur.right.val < num:
                cur = cur.right
            stack.append(cur)
            # Move down if the next node is None or its value is greater than target
            cur = cur.down
        insert = True
        down = None
        while insert and stack:
            cur = stack.pop()
            cur.right = Node(num, cur.right, down)
            down = cur.right
            insert = random.random() < 0.5
        # If insert is True and stack is empty, we need to create a new level
        if insert:
            self.head = Node(-1, None, self.head)