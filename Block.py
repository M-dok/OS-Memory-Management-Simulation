from LinkedList import Node,LinkedList

class Block(Node):
    def __init__(self, size, value=None, prev=None, next=None):
        '''
        prev: pointer to previous block
        size: Size of the block
        free: status of block True --> Free, False--> Used
        value --> linked list that will store the working set of block 
        next: pointer to next block  
        '''
        super().__init__(prev, value, next)
        if value is None: # value is equal to None 
            self._value = LinkedList() #creates an instance of a linked list 
        self._size = size   #Key for block/Max of block can hold (in Kb)
        self._cSize = 0     #Current amount of block memory being used (in Kb)
        
        self._accessBit = 0 #Will change when block is accessed on
        self._free = True   #status of block True --> Free, False--> Used

    def invertAccessBit(self):
        cNode = self._value.head #assigns page in head of working set to cNode 
        if cNode is None: #if working set is empty 
            return None #Exit method 
        marker= 0 #Tracks index of list 
        while marker < self._value.items: #loops while marker is less than length of working set 
            cNode.invertPageAccessBit() #Inverts the value of current page frame 
            print(f"{cNode}: {cNode.accessBit}", end=", ") #Print the page frame and value of its access bit 
            cNode = cNode.next #Move to page frame in working set 
            marker += 1 #increment marker by 1
    
    def pageRequest(self,PageTracker): #Request page frame and adds to working set of block 
        try:
            if self._cSize + 4 > self._size: #If block is already full raise a MemoryError 
                raise MemoryError("Size of list exceeded the limit")
            else: #Otherwise

                if self._cSize == 0: # If list is empty 
                    self._value.head = PageTracker.removeNode(PageTracker.tail) #Remove page from pages list in main memory, store in head of working set 
                    self._value.tail = self._value.head #Assign tail to head
                    self._value.tail.next = self._value.head #Assign tail next pointer to head of working set (Circular Linked list)
                    self._value._items += 1 #Increment by 1 
                    self._cSize +=4 #Increase current size by 4Kb 
                    print(f"_ {self._value.head} to block")
                
                else: #Otherwise 
                    temp = PageTracker.removeNode(PageTracker.tail) ##Remove page from pages list in main memory, store in temp variable 
                    self._value.tail.next = temp # Assign tail next pointer to temp 
                    self._value.tail = temp #Assign temp to tail of working set 
                    self._value.tail.next = self._value.head #Assign tail next pointer to head of working set (Circular Linked List)
                    self._value._items += 1 #Increment by 1 
                    self._cSize +=4 #Increase current size by 4Kb 
        except MemoryError:#If a MemoryError occurs : raise a MemoryError 
            raise MemoryError
    ###### Getters/Setters
    def getSize(self):
        return self._size
    
    def setSize(self, size):
        self._size = size

    def getAccessBit(self):
        return self._accessBit
    
    def setAccessBit(self, bit):
        self._accessBit = bit 

    def getFree(self):
        return self._free
    
    def setFree(self, free):
        if free not in ["Free,Used"]:
            return
        
        self._free = free

    def getVal(self):
        return self._value
    
    def setVal(self, list):
        if isinstance(list, LinkedList)==False:
            raise ValueError("self._value is a linked list")
        
        self._value = list

    def __str__(self) -> str:
        return f"block {self._size}Kb"

    size = property(getSize, setSize)
    free = property(getFree, setFree)
    accessBit = property(getAccessBit, setAccessBit)
    value = property(getVal,setVal)

class Page(Node):
    def __init__(self, value,prev,next):
        '''
        prev: pointer to previous page frame in list
        value: data stored in page frame
        next: pointer to next page frame in list
        '''
        super().__init__(prev, value, next)
        self._accessBit = 0
        self._size = 4 #4kb

    def invertPageAccessBit(self): #Inverts value of access bit to either 0 or 1
        if self._accessBit == 0:
            self._accessBit =1 
        else:
            self._accessBit = 0

    ###Getter/Setters
    def getAccessBit(self):
        return self._accessBit
    
    def setAccessBit(self, bit):
        self._accessBit = bit

    def getSize(self):
        return self._size
    
    def setSize(self, new_size):
        self._size =new_size

    def __str__(self) -> str:
        return super().__str__()
    
    accessBit = property(getAccessBit, setAccessBit)
    size = property(getSize, setSize)


class PageTracker(LinkedList): #Tracks all pages in memory
    def __init__(self,):
        super().__init__()

    def addNode(self, elt_or_node): #Adds Page to PageTracker 
        if isinstance(elt_or_node, Page): #If elt_or_node is an instance of a Page class 
            page = elt_or_node
        else: #Otherwise
            elt = elt_or_node

            page = Page(elt,None, None) #Creates an instance of the Page class 


        if self._items == 0: #If list is empty 
            self._head = page
            self._tail = self._head
            self._size += page.size
            self._items += 1 
        else: #If list isn't empty 
            page.prev = self._tail
            self._tail.next = page
            self._tail = page
            self._size += page.size
            self._items += 1 
        
        #Ensures circular structure is maintained 
        self._tail.next = self._head
        self._head.prev = self._tail


    def __str__(self) -> str: #Prints working set
        current = self._head
        marker = 0 
        der =[]
        if self._items == 0:
            return "[ ]"
        while current is not None:
            if self._items == marker:
                return str(der)
            else:
                der.append(str(current.size))
                current = current.next
                marker +=1 

if __name__ == "__main__":
    test = Block(4)
    #test.pageRequest("Hi")
    test.invertAccessBit()
    