class LinkedList(object):
    def __init__(self):
        self._head = None #Pointer to the Node at the start of the list 
        self._tail = None  #Pointer to Node at the end of the list 
        self._size = 0 #Tracks current size of the list
        self._items = 0 #Counts the number of Nodes in list 


    def removeNode(self,node,replacement_node=None):  #remove node from list
        if node == self.head: #If node is the head of list 
            if replacement_node is not None: #If a value for replacement_node is given 
                self._head = replacement_node #Assigns replacement_node to head of list 
                # Alters surrounding Nodes pointers so they are pointing to replacement_node
                node.prev.next = replacement_node
                node.next.prev = replacement_node
                #Unlink node  from list 
                node.prev = None
                node.next = None
                #decrement size and items of list 
                self._size -= node.size
                self._items -=1
                return node #return removed node 
            else: #If a value for replacement_node isn't given 
                try:
                    # Alters surrounding Nodes pointers so they aren't pointing to the removed node 
                    node.next.prev = node.prev
                    node.prev.next = node.next

                    self._head = node.next #Assign the next Node in list as the head of the list 
                    #Unlike node from list 
                    node.next = None
                    node.prev = None
                    #decrement size and items of list 
                    self._size -= node.size
                    self._items -=1
                    return node #Return the removed node 
                except AttributeError:  #List will be empty 
                    #Unlink Node 
                    node.next = None 
                    node.prev = None
                    #Decrement size and items 
                    self._size -= node.size
                    self._items -=1
                    return node #return removed node 
        elif node == self.tail: #If node is the tail of list 
            if replacement_node is not None:   #If a value for replacement_node is given 
                # Alters surrounding Nodes pointers so they are pointing to replacement_node
                node.prev.next = replacement_node
                node.next.prev = replacement_node

                self._tail = replacement_node #Assign replacement_node as the tail of list
                #Decrement size and items 
                self._size -= node.size
                self._items -=1
                return node #return removed node 
            else: #If no value is given for replacement_node
                #Alter surrounding nodes so the aren't pointing to node being removed 
                node.prev.next = node.next
                node.next.prev = node.prev

                self._tail = node.prev #Assign the previous block in list as the tail of queue
                #Unlink node from list 
                node.prev =None
                node.next = None
                #Decrement size and items 
                self._size -= node.size
                self._items -=1
                return node #Return removed node 
            
        else:# Node being replaced is in the middle of list 
            if replacement_node is not None: #If value is given for replacement_node
                #Alter surrounding node pointers so that the are pointing to replacement_node
                node.next.prev = replacement_node
                node.prev.next = replacement_node 
                #Unlink node from list 
                node.next = None
                node.prev = None
                #Decrement size and items 
                self._size -= node.size
                self._items -=1
                return node #Return removed node 
            else:# a value isn't given for replacement_node
                #Alter surrounding node pointers so that the are pointing to replacement_node
                node.next.prev = node.prev
                node.prev.next = node.next 
                #Unlink node from list 
                node.next = None
                node.prev = None
                #Decrement size and items 
                self._size -= node.size
                self._items -=1
                return node #Return removed node 

    def addNode(self, elt): 
        #arg: elt-> element stored in node
        if self._size == 0: #If lsit is empty 
            self._head = Node(None,elt, None) #creates instance of Node and assigns it to head of list 
            self._tail = self._head #Assign tail to val in head 
            self._items +=1 #increment items by 1 
        
        else:
            temp = Node(self._tail,elt,None)    #Creates instance of Node 
            self._tail.next = temp #Assigns tail next pointer to new Node 
            self._tail = temp #Assigns new Node as tail of list 
            self._items +=1 # Increment items by 1 

    def __str__(self) -> str:
        current = self._head
        marker = 0
        der =[]
        if self._items == 0:
            return "[ ]"
        while current is not None:
            if self._items == marker:
                return str(der)
            else:
                der.append(str(current._value))
                current = current.next
                marker +=1 

    #######Getters/Setters 
    def getFirst(self):
        return self._head
    
    def setFirst(self, node):
        self._head = node

    def getSize(self):
        return self._size
    
    def setSize(self, size):
        if size != int:
            return
        self._size = size

    def getLast(self):
        return self._tail

    def setLast(self, node):
        self._tail = node

    def getItems(self):
        return self._items
    
    def setItems(self, items):
        self._items =items

    ###Properties
    head = property(getFirst, setFirst)
    size = property(getSize, setSize)
    tail = property(getLast, setLast)
    items = property(getItems, setItems)

class Node(object): # Change to a Block Node
    def __init__(self,prev, value, next):
        self._prev = prev #Pointer to previous node  in list 
        self._value = value  #Value stored in Node 
        self._next = next #Pointer to the next Node in list 

    def getNext(self):
        return self._next
    
    def setNext(self, node):
        self._next = node

    def getPrev(self):
        return self._prev
    
    def setPrev(self, prev):
        self._prev = prev


    def __str__(self) -> str: #Prints value of Node 
        return str(self._value)

    next = property(getNext,setNext)
    prev = property(getPrev, setPrev)

