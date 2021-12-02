class MyLinkedStack:

    justTesting = 56 # This is a class attribute (like static)

    def __init__(self):
        self.first = None # Everything set here becomes instance attributes

    # Private public används inte riktigt i python. Man kan köra _ för protected och __ för private som konvention men det är inte lika vanligt som i Java
    def push(self,data):
        node = self.StackNode(data)
        node.next = self.first
        self.first = node

    def pop(self):
        if self.first is None:
            return None
        tmp = self.first
        self.first = self.first.next
        return tmp.data

    class StackNode:
        def __init__(self, data):
            self.data = data
            self.next = None

class MyLinkedQueue:

    def __init__(self):
        self.last = None
        self.size = 0        

    def offer(self, data):
        tmp = self.QueueNode(data)
        if self.last is None:
            self.last = tmp
            self.last.next = self.last
        else: 
            tmp.next = self.last.next
            self.last.next = tmp
            self.last = tmp
        self.size += 1

    def poll(self):
        if self.last is None:
            return None
        else:
            ret = self.last.next
            if self.size == 1:
                self.last = None
            else:
                self.last.next = ret.next
            self.size -= 1
            return ret.data
            

    def peek(self):
        if self.last is None:
            return None
        else:
            return self.last.next.data

    class QueueNode():
        def __init__(self, data):
            self.next = None
            self.data = data
