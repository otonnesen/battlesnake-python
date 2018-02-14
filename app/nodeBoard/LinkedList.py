# You can probably just assume in this class works (hopefully)
# Method names should be pretty self-explanatory

class LinkedList:
    class Node:
        def __init__(self):
            self.data = {}
            self.next = None

        def __str__(self):
            return str(self.data)

    def __init__(self):
        self.head = None

    def __str__(self):
        if(self.isEmpty()):
            return
        s = ['[',']']
        tmp = self.head
        while(tmp.next != None):
            s.insert(-1,str(tmp)+', ')
            tmp = tmp.next
        s.insert(-1,str(tmp))
        return ''.join(s)

    def isEmpty(self):
        return self.head == None

    def size(self):
        if(self.isEmpty()):
            return 0
        l = 1
        tmp = self.head
        while(tmp.next != None):
            l += 1
            tmp = tmp.next
        return l

    def append(self):
	if(self.isEmpty()):
		self.head = self.Node()
        tmp = self.head
        while(tmp.next != None):
            tmp = tmp.next
        tmp.next = self.Node()

    def get(self, index):
        if(index >= self.size()):
            return
        tmp = self.head
        for i in range(index):
            tmp = tmp.next
        return tmp.data

    def set(self, index, field, data):
        if(index >= self.size()):
            return
        if(index == 0):
            self.head.data[field] = data
            return
        tmp = self.head
        for i in range(index):
            tmp = tmp.next
        tmp.data[field] = data
