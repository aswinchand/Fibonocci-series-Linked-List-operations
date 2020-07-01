from functools import lru_cache

@lru_cache(maxsize = 1000)


class Node:
    def __init__(self, data):
        self.data=data
        self.next=None

class Linked_list:
    def __init__(self):
        self.head=None

   

    def append(self,data):
        new_node= Node(data)
        if self.head is None:
            self.head=new_node
            return
        current_node=self.head
        while True:
            if current_node.next is None:
                current_node.next=new_node
                break
            current_node=current_node.next
       
    def display(self):
       cur_node=self.head
       while cur_node:
           print(cur_node.data)
           cur_node=cur_node.next

def fibseries(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    elif n==2:
        return 1
    elif n>2:
        return fibseries(n-1) + fibseries(n-2)


my_list = Linked_list()
for n in range(0,100):
    #print(fibseries(n))
    my_list.append(fibseries(n))
my_list.display()




