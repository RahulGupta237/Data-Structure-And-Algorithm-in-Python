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

    def traversalSSL(self):
        """
        Time complexity O(n)
        Space complexity O(1)
        
        """
        if self.Head is None:
            print("Single Linked Doesnot Exits")
        else:
            node=self.Head
            while node is not None:
                print(node.value)
                node=node.next

    def searchSLL(self,value):
        """
        Time complexity O(n)
        Space complexity O(1)
        
        """
        if self.Head is None:
            print("Single Linked Doesnot Exits")
        else:
            node=self.Head
            while node is not None:
                if node.value==value:
                    print(node.value)
                    return node.value
                node=node.next
            return "Doesnot exits value"

    def deleteNodeSLL(self,location):
        if self.Head is None:
            print("Singly linked list doesnot exit")
        else:
            if location==0:
                if self.Head==self.Tail:
                    self.Head=None
                    self.Tail=None
                else:
                    self.Head=self.Head.next
            elif location==1:
                if self.Head==self.Tail:
                    self.Head=None
                    self.Tail=None
                else:
                    node=self.Head
                    while node is not None:
                        if node.next==self.Tail:
                            break
                        node=node.next
                    node.next=None
                    self.Tail=node

            else:
                tempNode=self.Head
                index=0
                while index <location-1:
                    tempNode=tempNode.next
                    index+=1
                nextNode=tempNode.next
                tempNode.next=nextNode.next
            

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
slinkedlist_obj.deleteNodeSLL(3)
slinkedlist_obj.traversalSSL()
x=slinkedlist_obj.searchSLL(8)

print([nod.value for nod in slinkedlist_obj])
print(x)


"""
time complexity O(n)  due to tempnode.next
and space complexity==O(1)

"""

        