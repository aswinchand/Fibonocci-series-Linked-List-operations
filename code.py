class Node:
    def __init__(self, data, next = None):
        self.val = data
        self.next = next

def insert(data):
    head = Node(data[0])
    for n in data[1:]:
        ptr = head
        while ptr.next:
            ptr = ptr.next
        ptr.next = Node(n)

    return head

def display(head):
    ptr = head
    while ptr:
        print(ptr.val, end = ", ")
        ptr = ptr.next


class LinkedList(object):
    def reverse(self, head):
        return  self.solve(head,None)

    def solve(self, head, back):
        if not head:
            return head
        temp= head.next
        head.next = back
        back = head
        if not temp:
            return head
        head = temp
        return self.solve(head,back)
        
fibnumbers = [0, 1]
for i in range(2,100):
    fibnumbers.append(fibnumbers[i-1]+fibnumbers[i-2])
#n=len(fibnumbers)
list1 = insert(fibnumbers)
mylist = LinkedList()
#print("The original list :\n")
#display(list1)
list2 = mylist.reverse(list1)
print("\nThe new list :\n")
display(list2)

