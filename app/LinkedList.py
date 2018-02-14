class LinkedList:
    class Node:
        def __init__(self, data):
            self.data = data
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

    def prepend(self, data):
        tmp = self.Node(data)
        tmp.next = self.head
        self.head = tmp

    def append(self, data):
	if(self.isEmpty()):
		self.head = self.Node(data)
        tmp = self.head
        while(tmp.next != None):
            tmp = tmp.next
        tmp.next = self.Node(data)

    def contains(self, data):
        tmp = self.head
        while(tmp.next != None):
            if(tmp.data == data):
                return True
            tmp = tmp.next
        if(tmp.data == data):
            return True
        return False

    def insert(self, index, data):
        if(index >= self.size()):
            return
        tmp = self.head
        for i in range(index-1):
            tmp = tmp.next
        new = self.Node(data)
        new.next = tmp.next
        tmp.next = new

    def index(self, index):
        if(index >= self.size()):
            return
        tmp = self.head
        for i in range(index):
            tmp = tmp.next
        return tmp.data

    def pop(self):
        tmp = self.head
        if(self.isEmpty()):
            return
        if(tmp.next == None):
            d = tmp.data
            tmp = None
            return d
        while(tmp.next.next != None):
            tmp = tmp.next
        d = tmp.next.data
        tmp.next = tmp.next.next
        return d
    
    def peek(self):
        if(self.isEmpty()):
            return
        tmp = self.head
        if(tmp.next == None):
            return tmp.data
        while(tmp.next.next != None):
            tmp = tmp.next
        return tmp.next.data

    def remove(self, data):
        tmp = self.head
        if(tmp.data == data):
            self.head = tmp.next
            return
        while(tmp.next != None):
            if(tmp.next.data == data):
                tmp.next = tmp.next.next
            tmp = tmp.next

    def removeAt(self, index):
        if(index >= self.size()):
            return
        tmp = self.head
        if(index == 0):
            self.head = tmp.next
            return
        for i in range(index-2):
            tmp = tmp.next
        tmp.next = tmp.next.next

    def set(self, index, data):
        if(index >= self.size()):
            return
        if(index == 0):
            self.head.data = data
            return
        tmp = self.head
        for i in range(index):
            tmp = tmp.next
        tmp.data = data

