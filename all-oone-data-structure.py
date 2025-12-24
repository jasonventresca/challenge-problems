class DllNode:
    def __init__(self, count: int):
        self.count = count
        self.prev = None
        self.next = None
        self.strings = set()

class AllOne:
    def __init__(self):
        # Create anchor nodes so that we always have a handle from which to quickly reach the min/max.
        self.head = DllNode(0)
        self.tail = DllNode(0)
        # Doubly link the empty DLL, to initialize it.
        self.head.next = self.tail
        self.tail.prev = self.head
        # Set up a mapping of strings (keys) -> DllNodes.
        self.stringToNode = dict()

    def inc(self, key: str) -> None:
        print(f'inc({key})')
        # Is this string being tracked by an existing node?
        node = self.stringToNode.get(key)
        if node:
            # Remove key from node
            node.strings.remove(key)
            # Move it to the larger node
            newCount = node.count + 1
            if node.next == self.tail or node.next.count != newCount:
                # Need to create another node in between node and node.next
                newNode =  DllNode(newCount)
                newNode.strings.add(key)
                newNode.next = node.next
                newNode.prev = node
                node.next.prev = newNode
                node.next = newNode
                self.stringToNode[key] = newNode
            else:
                node.next.strings.add(key)
                self.stringToNode[key] = node.next
    
            # Delete whole node, if it's now empty.
            self.deleteNodeIfEmpty(node)
        else:
            # Put it in the node with count of 1 (create node, if necessary)
            firstNode = self.head.next
            if firstNode == self.tail or firstNode.count != 1:
                newNode = DllNode(1)
                newNode.next = firstNode
                newNode.prev = self.head
                newNode.strings.add(key)
                self.head.next = newNode
                firstNode.prev = newNode
                self.stringToNode[key] = newNode
            else:
                firstNode.strings.add(key)
                self.stringToNode[key] = firstNode

    def dec(self, key: str) -> None:
        print(f'dec({key})')
        ''' Basically same/opposite as inc() '''
        node = self.stringToNode.get(key)
        # Remove key from node
        node.strings.remove(key)
        # Move it to the larger node
        newCount = node.count - 1
        if newCount == 0:
            del self.stringToNode[key]
        else:
            if node.prev == self.head or node.prev.count != newCount:
                # Need to create another node in between node.prev and node
                newNode =  DllNode(newCount)
                newNode.strings.add(key)
                newNode.next = node
                newNode.prev = node.prev
                node.prev.next = newNode
                node.prev = newNode
                self.stringToNode[key] = newNode
            else:
                node.prev.strings.add(key)
                self.stringToNode[key] = node.prev

        # Delete whole node, if it's now empty.
        self.deleteNodeIfEmpty(node)

    def getMaxKey(self) -> str:
        if self.tail.prev != self.head:
            # Return the first iterable in the set of strings at the end of the DLL.
            return next(iter(self.tail.prev.strings))
        return ''

    def getMinKey(self) -> str:
        if self.head.next != self.tail:
            return next(iter(self.head.next.strings))
        return ''

    def deleteNodeIfEmpty(self, node: DllNode) -> str:
        '''
        1. Check if node.strings is empty; if so, proceed with deletion.
        2. Link up prev and next nodes.
        3. del node.
        '''
        if node.strings:
            return
        node.next.prev = node.prev
        node.prev.next = node.next
        del node

# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
