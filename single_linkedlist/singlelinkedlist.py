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
                newNode.next=Node
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
Node1_obj=Node(1)
Node2_obj=Node(2)

""" linked the nodes between head and tail"""
SingleLinkedList.Head=Node1_obj
SingleLinkedList.Head.next=Node2_obj
SingleLinkedList.Tail=Node2_obj

        