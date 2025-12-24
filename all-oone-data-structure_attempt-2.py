class Node:
    def __init__(self, count: int):
        self.prev = None
        self.next = None
        self.count = count
        self.strings = set() # O(1) access, add, remove: thanks to __hash__() MM.

class AllOne:
    '''
    Approach:
    1.  We need to employ 2 data structures, in order to achieve the O(1) complexity across all operations:
    2.  HashMap (dictionary): mapping of key (str) -> pointer into the linked list.
    3.  Doubly Linked List (DLL):
    a.  Each node tracks the count and which keys have that count.
    b.  It has prev/next pointers to move around in the DLL.
    4.  There are a few things we need to worry about:
    a.  inc() - when we increment, what if the key does not yet exist?
    b.  dec() - what happens if the key's count reaches zero?
    c.  When a key moves from an existing node (src) to another (dst), what happens if src then holds no more keys?
    d.  Always keep the mapping dict up to date (i.e. repoint to new nodes, delete keys no longer tracking a valid node, etc.)
    '''

    def __init__(self):
        # Initialize the Doubly Linked List.
        self.head = Node(0)
        self.tail = Node(0)
        self.head.next = self.tail
        self.tail.prev = self.head
        # Initialize the mapping of {string -> Node}
        self.mapping = dict()

    def inc(self, key: str) -> None:
        srcNode = self.mapping.get(key)
        if srcNode:
            # Move from existing node to dstNode (i.e. whichever node tracking the incremented count).
            newCount = srcNode.count + 1
            if srcNode.next.count == newCount:
                # The destination node already exists.
                dstNode = srcNode.next
                dstNode.strings.add(key)
                self.mapping[key] = dstNode
            else:
                # Create such node if it does not yet exist.
                dstNode = Node(newCount)
                dstNode.strings.add(key)
                # Relink to/from adjacent nodes: srcNode <-> dstNode <-> srcNode.next
                dstNode.next = srcNode.next
                srcNode.next.prev = dstNode
                srcNode.next = dstNode
                dstNode.prev = srcNode
                self.mapping[key] = dstNode
            # Remove the key from the srcNode
            srcNode.strings.remove(key)
            # Is the srcNode now empty? If so, delete it entirely.
            self.deleteIfEmpty(srcNode)
        else:
            # Count = 1.
            newCount = 1
            # Place key in the node tracking count=1; else, create that node.
            firstNode = self.head.next
            if firstNode.count == 1:
                # Node tracking count=1 exists. Put the key there.
                firstNode.strings.add(key)
                self.mapping[key] = firstNode
            else:
                # Need to create new node tracking count=1.
                newNode = Node(1)
                newNode.strings.add(key)
                # Relink outside of the new node: self.head | +newNode+ | self.head.next
                newNode.prev = self.head
                newNode.next = self.head.next
                self.head.next.prev = newNode
                self.head.next = newNode
                self.mapping[key] = newNode

    def dec(self, key: str) -> None:
        srcNode = self.mapping.get(key)
        # Move from existing node to dstNode (i.e. whichever node tracking the incremented count).
        newCount = srcNode.count - 1
        if newCount == 0:
            # Delete the key from mapping
            del self.mapping[key]
        else:
            if srcNode.prev.count == newCount:
                # The destination node already exists.
                dstNode = srcNode.prev
                dstNode.strings.add(key)
                self.mapping[key] = dstNode
            else:
                # Create such node if it does not yet exist.
                dstNode = Node(newCount)
                dstNode.strings.add(key)
                # Relink to/from adjacent nodes: srcNode.prev | +dstNode+ | srcNode
                dstNode.next = srcNode
                dstNode.prev = srcNode.prev
                srcNode.prev.next = dstNode
                srcNode.prev = dstNode
                self.mapping[key] = dstNode
        # Remove the key from the srcNode
        srcNode.strings.remove(key)
        # Is the srcNode now empty? If so, delete it entirely.
        self.deleteIfEmpty(srcNode)

    def getMaxKey(self) -> str:
        if self.tail.prev == self.head:
            return ''
        return next(iter(self.tail.prev.strings)) # O(1) as set is already iterable.

    def getMinKey(self) -> str:
        if self.head.next == self.tail:
            return ''
        return next(iter(self.head.next.strings)) # O(1) as set is already iterable.

    @staticmethod
    def deleteIfEmpty(node: Node):
        if node.strings:
            return
        # Relink adjacent nodes: node.prev | XnodeX | node.next
        node.prev.next = node.next
        node.next.prev = node.prev
        del node


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
