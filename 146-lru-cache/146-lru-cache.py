class Node:
    def __init__(self,key=0,value=0):
        self.key=key
        self.value=value
        self.pre=None
        self.next=None

class LRUCache:
    def addToFront(self,node):
        node.pre=self.head
        node.next=self.head.next
        
        self.head.next.pre=node
        self.head.next=node
    
    def remove(self,node):
        pre=node.pre
        nextNode=node.next
        
        pre.next=nextNode
        nextNode.pre=pre

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.cache={}
        self.head,self.tail=Node(),Node()
        self.head.next=self.tail
        self.tail.pre=self.head
        

    def get(self, key: int) -> int:
        if key in self.cache:
            node=self.cache[key]
            self.remove(node)
            self.addToFront(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        n = Node(key, value)
        self.addToFront(n)
        self.cache[key] = n
        if len(self.cache) > self.capacity:
            n = self.tail.pre
            self.remove(n)
            self.cache.pop(n.key,None)
            


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)