class Node(object):
    # Each node has its data and a pointer that points to next node in the Linked List
    def __init__(self, data, next = None):
        self.data = data;
        self.next = next;
 
    # function to set data
    def setData(self, data):
        self.data = data;
        
    # function to get data of a particular node
    def getData(self):
        return self.datalin
    
    # function to set next node
    def setNext(self, next):
        self.next = next
        
    # function to get the next node
    def getNext(self):
        return self.next

class LinkedList(object):
    # Defining the head of the linked list
    # def __init__(self):
    #     self.head = None
    #     self.count = 0
    def __init__(self, head = None):
        # if head == None:
        #     self.head = None
        #     self.count = 0
        # else: 
        #     self.head = head
        #     self.count = 1  
        self.head = head
        self.count = 0
    # printing the data in the linked list
    def printLinkedList(self):
        temp = self.head
        while(temp):
            print(temp.data, end=' ')
            temp = temp.next
            
    # inserting the node at the beginning
    def insertAtStart(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode # update LinkList head
        self.count += 1 # update count
        
    # inserting the node in between the linked list (after a specific node)
    def insertBetween(self, previousNode, data):
        if (previousNode.next is None):
            print('Previous node should have next node!')
        else:
            newNode = Node(data)
            newNode.next = previousNode.next
            previousNode.next = newNode
            self.count += 1 # update count
            
    # inserting at the end of linked list
    def insertAtEnd(self, data):
        newNode = Node(data)
        temp = self.head
        while(temp.next != None):         # get last node
            temp = temp.next
        temp.next = newNode
        self.count += 1 # update count
        
    # deleting an item based on data
    def delete(self, data):
        temp = self.head
        # if data to be deleted is the head
        if (temp.next is not None): 
            if(temp.data == data):
                self.head = temp.next
                self.count -= 1
                temp = None
                return
            else:
                #  else search all the nodes
                while(temp.next != None):
                    if(temp.data == data):
                        break
                    prev = temp          #save current node as previous so that we can go on to next node
                    temp = temp.next
                
                # node not found
                if temp == None:
                    return
                
                prev.next = temp.next # if found, then drop the node by omiting it from the link
                self.count -= 1
                return
            
    # iterative search
    def search(self, node, data):
        if node == None:
            return False
        if node.data == data:
            return True
        return self.search(node.getNext(), data)
    # iterative search return found item instead of True/False
    def search_list(self, node, data):
        while node and node.data != data:
            node = node.next
        return node