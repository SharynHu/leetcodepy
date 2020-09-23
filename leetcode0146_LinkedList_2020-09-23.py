    def __init__(self):
        self.head = None
        self.tail = None
    
    def insertToTail(self, node):
        #将节点node插入双链表末尾
        if not self.head:
            self.head = node
            self.tail = node
            return
        node.prev = self.tail
        self.tail.next = node
        self.tail= node
        return
        
    def deleteFromHead(self):
        if self.head == self.tail:
            self.head = None
            self.tail = None
            return
        newHead = self.head.next
        self.head.next= None
        self.head = newHead
        return
    
    def deleteFromTail(self):
        if self.head == self.tail:
            self.head = None
            self.tail = None
            return
        self.tail = self.tail.prev
        self.tail.next = None
        return
    
    def delete(self, node):
        if node==self.head:
            self.deleteFromHead()
            return
        if node == self.tail:
            self.deleteFromTail()
            return
        prevNode = node.prev
        nextNode = node.next
        node.prev = None
        node.next = None
        print prevNode, nextNode
        prevNode.next = nextNode
        nextNode.prev = prevNode
        return

class Node(object):
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None
        

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.linkedlist = BiDirectLinkedList()
        self.keyToNode = {}
        self.capacity = capacity

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.keyToNode:
            return -1
        #需要现将节点从链表中删除
        node = self.keyToNode[key]
        self.linkedlist.delete(node)
        #再将该节点加入链表尾部
        self.linkedlist.insertToTail(node)
        return self.keyToNode[key].val

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        #1.如果节点已经存在
        if self.get(key)!=-1:
            self.keyToNode[key].val = value
            return
        #2. 如果节点不存在，需要新建一个node
        newNode = Node(key, value)
        #3. 将该节点加入链表尾部，更新hashmap
        self.linkedlist.insertToTail(newNode)
        self.keyToNode[key] = newNode
        #4. 决定是否要pop out一个node
        if self.capacity>0:
            self.capacity -= 1
            return
        head = self.linkedlist.head
        self.linkedlist.deleteFromHead()
        self.keyToNode.pop(head.key)
        return


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
