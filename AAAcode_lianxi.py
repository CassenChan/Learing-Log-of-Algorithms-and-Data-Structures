class Node(object):
    def __init__(self, item):
        self.elem = item
        self.next = None
        self.prev = None

class DoubleLinkList(object):
    def __init__(self, node=None):
        self._head = node

    def travel(self):
        ptr = self._head
        while(ptr!=None):
            print(ptr.elem)
            ptr = ptr.next

    def append(self, item):
        node = Node(item)
        if self._head == None:
            self._head = node
        else:
            ptr = self._head
            while (ptr.next != None):
                ptr = ptr.next
            ptr.next = node
            node.prev = ptr

    def add(self, item):
        node = Node(item)
        if self._head == None:
            self._head = node
        else:
            node.next = self._head
            self._head.prev = node
            self._head = node

    def delete(self, item):
        if self._head.elem == item:
            self._head.next.prev = None
            self._head = self._head.next
        else:
            ptr = self._head
            while(ptr.next != None):
                if not ptr.elem == item:
                    ptr = ptr.next
                else:
                    ptr.next.prev = ptr.prev
                    ptr.prev.next = ptr.next
                    break
            if ptr.next == None:
                ptr.prev.next = None

    def insert(self, pos, item):
        if pos==0:
            self.add(item)
        else:
            node = Node(item)
            ptr = self._head
            for i in range(pos-1):
                ptr = ptr.next
            node.next = ptr
            node.prev = ptr.prev
            ptr.prev.next = node
            ptr.prev = node

# class Node(object):
#     def __init__(self, item):
#         self.elem = item
#         self.next = None
#
# class CycleLinkList(object):
#     def __init__(self, node=None):
#         self._head = node
#
#     def travel(self):
#         if self._head==None:
#             return
#         ptr = self._head
#         while(ptr.next!=self._head):
#             print(ptr.elem)
#             ptr = ptr.next
#         if ptr.next==self._head:
#             print(ptr.elem)
#
#     def add(self, item):
#         node = Node(item)
#         if self._head == None:
#             self._head = node
#             node.next = self._head
#         else:
#             ptr = self._head
#             while (ptr.next != self._head):
#                 ptr = ptr.next
#             node.next = self._head
#             ptr.next = node
#             self._head = node
#
#     def append(self, item):
#         node = Node(item)
#         if self._head == None:
#             self._head = node
#             node.next = self._head
#         else:
#             ptr = self._head
#             while (ptr.next != self._head):
#                 ptr = ptr.next
#             ptr.next = node
#             node.next = self._head
#
#     def delete(self, item):
#         if self._head.next == self._head:
#             self._head = None
#         else:
#             if self._head.elem == item:
#                 ptr = self._head
#                 while (ptr.next != self._head):
#                     ptr = ptr.next
#                 ptr.next = self._head.next
#                 self._head = ptr.next
#             else:
#                 ptr = self._head
#                 prev = ptr
#                 ptr = ptr.next
#                 while (ptr != self._head):
#                     if not ptr.elem == item:
#                         prev = ptr
#                         ptr = ptr.next
#                     else:
#                         prev.next = ptr.next
#                         break
#
#     def insert(self, pos, item):
#         if pos==0:
#             self.add(item)
#         else:
#             node = Node(item)
#             ptr = self._head
#             for i in range(pos):
#                 pre = ptr
#                 ptr = ptr.next
#             if ptr != self._head:
#                 node.next = ptr
#                 pre.next = node
#             else:
#                 self.append(item)

# class Node(object):
#     def __init__(self, item):
#         self.elem = item
#         self.next = None
#
# class SingleLinkList(object):
#     def __init__(self,node=None):
#         self._head = node
#
#     def travel(self):
#         ptr = self._head
#         while(ptr!=None):
#             print(ptr.elem)
#             ptr = ptr.next
#
#     def move(self, step):
#         ptr = self._head
#         for i in range(step):
#             ptr = ptr.next
#         return ptr.elem
#
#     def append(self, item):
#         node = Node(item)
#         if self._head == None:
#             self._head = node
#         else:
#             ptr = self._head
#             while (ptr.next != None):
#                 ptr = ptr.next
#             ptr.next = node
#
#     def length(self):
#         if self._head == None:
#             return 0
#         else:
#             ptr = self._head
#             i = 0
#             while (ptr != None):
#                 ptr = ptr.next
#                 i += 1
#         return i
#
# def reverse(sl, res):
#     len = sl.length()
#     for i in range(len-1, -1, -1):
#         v = sl.move(i)
#         res.append(v)
#     return res
#
# def merge(sl1, sl2, res):
#     len1 = sl1.length()
#     len2 = sl2.length()
#     i1 = 0
#     i2 = 0
#     while(1):
#         if sl1.move(i1)<=sl2.move(i2):
#             res.append(sl1.move(i1))
#             i1 += 1
#         else:
#             res.append(sl2.move(i2))
#             i2 += 1
#         if i1==len1 and i2!=len2:
#             while(1):
#                 res.append(sl2.move(i2))
#                 i2 += 1
#                 if i2==len2-1:
#                     return
#         elif i1!=len1 and i2==len2:
#             while(1):
#                 res.append(sl1.move(i1))
#                 i1 += 1
#                 if i1==len1-1:
#                     return
#         elif i1 == len1 and i2 == len2:
#             return

if __name__=="__main__":
    dl = DoubleLinkList()
    dl.append(1)
    dl.append(2)
    dl.append(3)
    dl.append(4)
    dl.append(5)
    dl.add(0)
    dl.insert(0, 10)
    dl.travel()
    # sl = SingleLinkList()
    # sl.append(1)
    # sl.append(2)
    # sl.append(3)
    # sl.append(4)
    # sl.append(5)
    # sl.append(6)
    # sl.append(7)
    # sl.append(8)
    # sl.append(9)
    # res = SingleLinkList()
    # res = reverse(sl, res)
    # res.travel()

    # sl1 = SingleLinkList()
    # sl1.append(1)
    # sl1.append(3)
    # sl1.append(5)
    # sl1.append(7)
    # sl1.append(9)
    # sl1.append(10)
    # sl1.append(11)
    # sl1.append(12)
    # sl1.append(13)
    #
    # sl2 = SingleLinkList()
    # sl2.append(2)
    # sl2.append(4)
    # sl2.append(6)
    # sl2.append(8)
    #
    # res = SingleLinkList()
    # merge(sl1, sl2, res)
    # res.travel()


    # cl = CycleLinkList()
    # cl.append(1)
    # cl.append(2)
    # cl.append(3)
    # cl.append(4)
    # cl.append(5)
    # cl.append(6)
    # cl.insert(6, 10)
    # cl.travel()

