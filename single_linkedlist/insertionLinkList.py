class SingleLinkedList:
    def __init__(self) -> None:
        self.Head=None
        self.Tail=None

    def __iter__(self):
        node=self.Head
        while node:
            yield node
            node=node.next
    # insert in linked list
    def insertSLL(self,value,location):
        newNode=Node(value)
        if self.Head is None:
            self.Head=newNode
            self.Tail=newNode
        else:
            if location==0:
                newNode.next=self.Head
                self.Head=newNode
            elif location==-1:
                newNode.next=None
                self.Tail.next=newNode
                self.Tail=newNode
            else:
                tempNode=self.Head
                index=0
                while index<location-1:
                    tempNode=tempNode.next
                    index+=1
                nextNode=tempNode.next
                tempNode.next=newNode  # current node
                newNode.next=nextNode

class Node:
    def __init__(self,value=None) -> None:
        self.value=value
        self.next=None


slinkedlist_obj=SingleLinkedList()

slinkedlist_obj.insertSLL(1,-1)

slinkedlist_obj.insertSLL(2,-1)

slinkedlist_obj.insertSLL(3,-1)

slinkedlist_obj.insertSLL(4,0)

slinkedlist_obj.insertSLL(8,3)  # after third element put here

print([nod.value for nod in slinkedlist_obj])

"""
time complexity O(n)  due to tempnode.next
and space complexity==O(1)

"""

        