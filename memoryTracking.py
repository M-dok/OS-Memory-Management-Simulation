from LinkedList import LinkedList
from Block import Block

class FreeBlockTracker(LinkedList):# Two instances one from tracking free blocks and on for tracking in-use blocks 
    def __init__(self, maxSize):
        super().__init__()
        self._maxSize = maxSize # Stores the maximum size of main memory (in Kb) / Size -> the current size of list 
        self._pointer = None    #Points to the last allocated block or 
        self._items = 0         #Number of blocks inside list 
         
    def addNode(self, elt_or_node, size=None): #Adds Block to list 
        if isinstance(elt_or_node, Block):  #If elt_or_node is a block 
            block = elt_or_node #block is assigned the value in elt_or_node
        else: #If elt_or_node is a block class object 
            elt = elt_or_node
            if size is None: #If size is equal to None 
                raise ValueError("Size must be provided when adding an element") #Raise a ValueError 
            block = Block(size, elt,None, None) #Create an instance of a Block 

        if self._size + block.size > self._maxSize: #If the size of block and the current size of list is greater than maxSize 
            raise MemoryError("Size of list exceeded the limit")    #Raise a MemoryError 

        if self._size == 0: #If list is empty 
            self._head = block #assgin block to head of list 
            self._tail = self._head #Tail is equal to head 
            self._size += block.size #Increase current size of list by size of block being added 
            self._items += 1  #increment items by 1
        else: #If list isn't empty 
            block.prev = self._tail #Block prev pointer assign to tail of list 
            self._tail.next = block # tail of list next pointer assigned to block 
            self._tail = block # block is assigned to tail of list 
            self._size += block.size #Increase current size of list by size of block being added 
            self._items += 1   #increment items by 1

        # Establish circular linking
        self._tail.next = self._head
        self._head.prev = self._tail


    ###Getters/Setters 
    def getMaxSize(self):
        return self._maxSize
    
    def setMaxSize(self, new_size):
        self._maxSize = new_size

    def getPointer(self):
        return self._pointer

    def setPointer(self, node):
        if isinstance(node, Block) ==False:
            raise ValueError("Needs object needs to be a block")
        else:
            self._pointer = node


    ###Properties
    maxSize = property(getMaxSize, setMaxSize)
    pointer = property(getPointer, setPointer)


    def __str__(self) -> str: 
        current = self._head
        marker = 0
        der =[]
        if self._items == 0: #if ist is empty 
            return "[ ]"
        while current is not None:
            if self._items == marker: #if marker is equal to length of list 
                return str(der) #return der 
            else:
                der.append(str(current.size)) #add block size to der 
                current = current.next #moves to next block in list 
                marker +=1 #increment by 1 

class UsedBlockTracker(FreeBlockTracker): #Used to track used blocks 
    def __init__(self, maxSize):
        super().__init__(maxSize)



if __name__ == "__main__":
    free_blocks = FreeBlockTracker()  #Tracks free memory blocks
    in_use_blocks = UsedBlockTracker()#Tracks block in use 