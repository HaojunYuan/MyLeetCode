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
    
    def addToFront(self,node):
        node.next=self.head.next
        node.pre=self.head
        
        self.head.next.pre=node
        self.head.next=node
        
    def remove(self,node):
        node.pre.next=node.next
        node.next.pre=node.pre

    def get(self, key: int) -> int:
        if key in self.cache:
            node=self.cache[key]
            self.remove(node)
            self.addToFront(node)
            return node.val
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        newNode=Node(key,value)
        self.addToFront(newNode)
        self.cache[key]=newNode
        if len(self.cache)>self.capacity:
            n=self.tail.pre
            self.remove(n)
            self.cache.pop(n.key,None)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)