class Node:
    def __init__(self,key=0,value=0):
        self.key=key
        self.val=value
        self.pre=None
        self.next=None
        
class LRUCache:

    def __init__(self, capacity: int):
        self.cache={}
        self.capacity=capacity
        self.head,self.tail=Node(),Node()
        self.head.next=self.tail
        self.tail.pre=self.head
    
    def insert(self,node):
        node.pre=self.head
        node.next=self.head.next
        self.head.next.pre=node
        self.head.next=node
    
    def remove(self,node):
        node.next.pre=node.pre
        node.pre.next=node.next

    def get(self, key: int) -> int:
        if key in self.cache:
            node=self.cache[key]
            self.remove(node)
            self.insert(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        newNode=Node(key,value)
        self.cache[key]=newNode
        self.insert(newNode)
        if len(self.cache)>self.capacity:
            toRemove=self.tail.pre
            self.remove(toRemove)
            self.cache.pop(toRemove.key,None)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)