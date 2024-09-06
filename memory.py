#Michael O'Keeffe 122383206
from memoryTracking import FreeBlockTracker, UsedBlockTracker
from Block import Block,PageTracker
import random
class Memory(object):
    def __init__(self, maxSize):
        self._freeBlocks = FreeBlockTracker(maxSize)#Circular Linked List to track free blocks in memory
        self._usedBlocks = UsedBlockTracker(maxSize)#Circular Linked List to track used blocks in memory 
        self._pages = PageTracker()#Circular Linked list that stores all pages being used 
        self._pointer = self._usedBlocks.head #Used in process method to iterate through blocks 


    def next_fit(self, require_size):

        """
        Allocate memory using the next fit algorithm.
        
        Args:
            require_size (int): Represents the size of memory required by the process.
        """
        if self._freeBlocks.items ==0: #If list is empty
            print("All blocks are in use")
            raise MemoryError


        marker =0   #controlling variable that indicates the amount of items iterated through 
        block = None #returning variable 
        def allocate_memory(block, require_size): # Helper function to allocate memory and update pointers
            if block.size > require_size:#If the block size is bigger than the amount requested
                # Split the block if it's larger than required_size
                split_block = Block(block.size - require_size, None, block.prev, block.next) #Spit block. Internal fragmentation 
                self._freeBlocks._items += 1 #increase the size of freeBlock list 
                block.size = require_size   #change block size to the amount requested 
                removed_block = self._freeBlocks.removeNode(block, split_block) #remove block from list and replace with split block
                self.swapping(removed_block, self._usedBlocks)  #transfer block (swap) to used block list 
                self._freeBlocks.pointer = split_block  # set the split block as the pointer 
                
                #Ensuring pointer variables are maintained 
                if block == self._freeBlocks.head:
                    self._freeBlocks.head = split_block
                
                if block == self._freeBlocks.tail:
                    self._freeBlocks.tail = split_block
                
                return removed_block #return the removed block
                
            else:#If block is equal to the required size
                self._freeBlocks.pointer = block.next #setting the next block in queue as the 

                #Ensuring pointer variables are maintained 
                if block == self._freeBlocks.head:
                    self._freeBlocks.head = block.next
                
                if block == self._freeBlocks.tail:
                    self._freeBlocks.tail = block.next
                
                removed_block = self._freeBlocks.removeNode(block) # remove node
                block.free = False #Block is now in use
                self.swapping(block, self._usedBlocks)  #transfer block (swap) to used block list 
                return removed_block
        

        if self._freeBlocks.size == self._freeBlocks.maxSize:   #If the free block list is full 
            # Perform first fit if free block list is full
            cNode = self._freeBlocks.head #Assign the head of free block list to cNode
            while cNode is not None:
                if cNode.size >= require_size: #if cNode's size is equal or greater than requested amount of memory
                    block = allocate_memory(cNode, require_size) #invoke inner function 
                    return block #return removed block 
                elif marker > self._freeBlocks.items:#If marker is greater than length of list 
                    raise MemoryError("No Block is big enough") #Raise MemoryError 
                else:
                    cNode = cNode.next #Assign the next block in list to cNode
                    marker +=1 #Increment marker by 1 
            

        else:
            # Continue from the previous position if free block list is not full
            cNode = self._freeBlocks.pointer #Assign value in free list pointer to cNode
            while cNode is not None: 
                if cNode.size >= require_size:
                    block = allocate_memory(cNode, require_size) #invoke inner function
                    return block
                elif marker > self._freeBlocks.items:#If marker is greater than length of list 
                    raise MemoryError("No Block is big enough")#Raise MemoryError
                else:
                    cNode = cNode.next #Assign the next block in list to cNode
                    marker +=1 #Increment marker by 1 
    
    def swapping(self, node,destination):
        '''
        Swaps blocks or pages from  main memory to disk or virtual memory
        node: Block or page that is being swapped
        destination: list that node is being swapped to 
        '''
        try:
            destination.addNode(node)
        except MemoryError: #If destination list is full then a MemoryError is raised 
            print("Memory is full")
            raise MemoryError

    def secondChance_Page(self,Block,new_page=None):#Page replacement algorithm 
        '''
        Args: 
            Block --> Is the block working set which is being examined
            new page --> Page which is replacing the old page 
        '''
        if Block.items ==0: #If the block doesn't have a working set 
            print("Block is empty")
            return

        if new_page == None: #If a replacement page isn't specified 
            new_page = self._pages.removeNode(self._pages.tail) #Take a page at the end of pages list from main memory and assign it to new_page 
        if Block.head.accessBit == 0:   #If page at the head of queue is has a access bit equal to 0
            #Insert new_page into the old pages position
            new_page.prev = Block.head.prev 
            new_page.next = Block.head.next
            removed_page = Block.removeNode(Block.head) #remove the old page and store in variable removed_page 
            self.swapping(Block.head, self._pages)  #transfer removed_page into pages list
            Block.head = new_page   # Assign head pointer to new_page to maintain LL structure 
            return removed_page
        else: #If access bit is equal to 1
            Block.head.accessBit = 0 #Invert access bit
            temp = Block.head 

            Block.head = temp.next #Assign the next block in list as the head of the queue 
            #place block at the end of the queue 
            Block.tail.next = temp 
            temp.prev = Block.tail
            temp.next = None 
            Block.tail = temp
            self.secondChance_Page(Block, new_page) #recursive call: examine the new head of queue


    def initialiseMemory(self):# initialise memory into four equal sized blocks 
        
        der = self._freeBlocks.getMaxSize()//4 #
        for i in range(0, 4):   
            self._freeBlocks.addNode(Block(der)) #creates four equal sized blocks 

        for i in range(256):
            self._pages.addNode(f"Page{i}") #creates pages and stores them in a Linked list 
        


        


    def Process(self):#Allocates blocks to main memory till it is full 

        page_numbers = [2,4,8,16,32,64,128,256,512]    #Amount of pages that can be in a block
        while True: #Infinite Loop
            der = random.choice(page_numbers) # chooses random item inn  page_numbers list 
            try:
                    print("Block allocation")
                    self.next_fit((4*der)) #invokes next_fit algorithm 
                    print("Process Size: ", der*4)
                    print("free blocks: ", self._freeBlocks)
                    print("used blocks: ", self._usedBlocks, "\n")
            except MemoryError: #If a MemoryError occurs 
                    print("Memory is full")
                    break #Exit Loop
            
        
        self.test() #invokes test() 
    
    ###Getters/Setters
    def getPointer(self):
        return self._pointer
    
    def setPointer(self, node):
        if isinstance(node, Block)==False:
            raise AttributeError("Pointer needs to be a Block class object")
        
        self._pointer = node

    pointer = property(getPointer, setPointer)

    def test(self):

        while True: #Infinite Loop 
                try:
                                print("Accessing Blocks")
                                self.pointer.invertAccessBit() #Iterates through working set of block and inverts page frames access bits to simulate a process occurring 
                                print("free blocks: ", self._freeBlocks) #Prints blocks in free blocks list 
                                print("used blocks: ", self._usedBlocks, "\n") #Prints blocks in used block list 
                except AttributeError:# If self.pointer is not assigned a value 
                                self.pointer = self._usedBlocks.head # Assigns the head of used block list as the pointer 
                                self.pointer.invertAccessBit() #Iterates through working set of block and inverts page frames access bits to simulate a process occurring 
                                self._pointer = self._pointer.next  #Assigns next block as pointer 
                                print("free blocks: ", self._freeBlocks) #Prints blocks in free blocks list
                                print("used blocks: ", self._usedBlocks, "\n") #Prints blocks in used block list 
                try:
                                self.pointer.pageRequest(self._pages)#adds page frame to block assign to pointer
                                print("Pages in Block: ", self.pointer.getVal()) #Prints working set of block assign to pointer 
                                self.pointer = self.pointer.next # Moves pointer to next block in list 
                                print("Free blocks: ", self._freeBlocks) #Prints blocks in free blocks list
                                print("Used blocks: ", self._usedBlocks, "\n") #Prints blocks in used block list 
                except MemoryError: # If MemoryError occurs 
                                print("Page replacement")
                                der = self.secondChance_Page(self.pointer.getVal())#Invoke Second Chance page replacement algorithm 
                                print("Removed Page: ",der) # Print removed page frame 
                                print("Pages in Block: ", self.pointer.getVal()) #Prints working set of block assign to pointer 
                                self.pointer = self.pointer.next #Assigns next block as pointer 
                                print("Free blocks: ", self._freeBlocks) #Prints blocks in free blocks list
                                print("Used blocks: ", self._usedBlocks, "\n") #Prints blocks in used block list
                except AttributeError:
                            raise AttributeError
                            #self._pointer = self._usedBlocks.head
            
if __name__ == "__main__":
    der = Memory(4096)  #4096Kb 
    der.initialiseMemory()
    der.Process()
            
    
    #der.Process()
    
    

    