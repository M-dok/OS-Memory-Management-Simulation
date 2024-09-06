def next_fit(self, require_size):
    """
    Allocate memory using the next fit algorithm.
    
    Args:
        require_size (int): Represents the size of memory required by the process.
    """
    # Helper function to allocate memory and update pointers
    def allocate_memory(block, remaining_size):
        if block.size > remaining_size:
            # Split the block if it's larger than required_size
            split_block = Block(block.size - remaining_size, None, block.prev, block.next)
            block.size = remaining_size
            self._freeBlocks.removeNode(block, split_block)
            self.swapping(block, self._usedBlocks)
            self.pointer = split_block
        else:
            self.pointer = block.next
            self._freeBlocks.removeNode(block)
            block.free = False
            self.swapping(block, self._usedBlocks)

    if self._freeBlocks.size == self._freeBlocks.maxSize:
        # Perform first fit if free block list is full
        cNode = self._freeBlocks.head
        while cNode is not None:
            if cNode.size >= require_size:
                allocate_memory(cNode, require_size)
                break
            cNode = cNode.next
    else:
        # Continue from the previous position if free block list is not full
        cNode = self.pointer
        while cNode is not None:
            if cNode.size >= require_size:
                allocate_memory(cNode, require_size)
                break
            cNode = cNode.next


#this gotten from chat GPT might me better next_fit than our own 


#my version:
def next_fit(self, require_size):#Needs a fail state
        '''
        args: working set: A list representing the working set of the process 
            require_size: represents the size of memory that the
        '''
        cNode = self._freeBlocks.head
        if self._freeBlocks.size == self._freeBlocks.maxSize:  #If free block list is full perform first fit
            while cNode is not None:    #While current block is not Null 
                if cNode.size == require_size:  #If the current block is the required size allocated process to it
                    #Need to remove cNode from list and add it to in-use blocks list 
                    self.pointer = cNode.next#Search will start here in the next iteration 
                    temp = self._freeBlocks.removeNode(cNode)
                    temp.invertAccessBit()
                    self.swapping(temp,self._usedBlocks)
                    break
                elif cNode.size > require_size:
                    memory_waste = cNode.size - require_size
                    split_block = Block(memory_waste, None,cNode.prev, cNode.next)#Internal Fragmentation. Replaces cNodes place in free list
                    self._freeBlocks.removeNode(cNode, split_block)
                    cNode.size =require_size
                    cNode.free = False
                    self.swapping(cNode,self._usedBlocks)
                    self.pointer = split_block #Search will start here in the next iteration 
                    break
                else:
                    cNode = cNode.next  #Move onto next block in list 

        else:
            cNode = self.pointer
            while cNode != None:
                if cNode.size == require_size:  #If the current block is the required size allocated process to it
                    #Need to remove cNode from list and add it to in-use blocks list 
                    self.pointer = cNode.next#Search will start here in the next iteration 
                    self._freeBlocks.removeNode(cNode)
                    cNode.free = False
                    self.swapping(cNode, self._usedBlocks)
                elif cNode.size > require_size:
                    memory_waste = cNode.size - require_size
                    split_block = Block(memory_waste, None,cNode.prev, cNode.next)#Internal Fragmentation
                    cNode.size = require_size #allocates the requested memory to block
                    self._freeBlocks.removeNode(cNode,split_block)
                    cNode.free = False
                    self.swapping(cNode, self._usedBlocks) 
                    self.pointer = split_block #Search will start here in the next iteration 
                    
                else:
                    cNode = cNode.next  #Move onto next block in list