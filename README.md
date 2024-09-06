[Introduction]{.underline}

In this report, I will be programming and testing a set of memory
management algorithms. I will assume that the size of the memory user
space is 4MB, and the page size is 4KB. Main memory is organized into
blocks that contain page frames. The main memory can be organized into
ten different block sizes, for example:

- Block1: 2 pages -\> can fit 512 blocks into the main memory.

- Block2: 4 pages -\> can fit 256 blocks into the main memory.

- Block3: 8 pages -\> can fit 128 blocks into the main memory.

- Block4: 16 pages -\> can fit 64 blocks into the main memory.

- Block5: 32 pages -\> can fit 32 blocks into the main memory.

- Block6: 64 pages -\> can fit 16 blocks into the main memory.

- Block7: 128 pages -\> can fit 8 blocks into the main memory.

- Block8: 256 pages -\> can fit 4 blocks into the main memory.

- Block9: 512 pages -\> can fit 2 blocks into the main memory.

- Block10: 1024 pages -\> can fit 1 block into the main memory.

Initially, when my main memory is primed it will consist of four
fixed-size blocks of 1MB which can contain up to 256 pages. Memory
organization is maintained by the kernel. The kernel employs many
strategies/algorithms to maintain organization through managing free
memory, allocation, and page replacement.

For free memory tracking, I have chosen to implement a circular linked
list. Two circular linked lists will be maintained one for tracking
in-use blocks and one for tracking free blocks. Each item in the linked
list contains the address, size of the block and a pointer to the next
block in the list. Blocks are sorted by address this provides the
advantage that when a process terminates or is swapped out, updating the
list is straightforward. The reason for choosing this method for memory
tracking over other common methods such as bitmaps, is due to its
flexibility, efficiency, and scalability. When using a sorted linked
list several algorithms can be used to allocate memory such as first
fit, next fit, best fit, etc.

![A diagram of a circular linked list Description automatically
generated](media/image1.png){width="5.166932414698163in"
height="1.5695253718285214in"}

Figure 1 Circular Linked List data structure. This will be used to
maintain the two lists tracking free and used blocks.

Memory allocation can be done in a variety of ways by implementing
memory allocation algorithms such as *next-fit.* A next-fit algorithm
starts like a first-fit algorithm, where a free block is greater or
equal to the size of the process. However, the key difference between
them is when the algorithm starts searching again it begins where it
last left off. Next-fit is a quick and efficient searching algorithm
that contains many advantages over other allocation algorithms such as
first-fit. A problem with the first fit is that it tends to allocate
memory parts at the beginning of the memory, which may lead to more
internal fragments at the beginning. Next fit tries to address this
problem by starting the search for the free portion of parts not from
the start of the memory, but from where it ends last time. Next Fit is a
high-speed searching algorithm and is also comparatively faster than
First Fit and Best Fit Memory Management Algorithms.

![A diagram of a block diagram Description automatically
generated](media/image2.png){width="6.268055555555556in"
height="3.517361111111111in"}

Memory deallocation can be done in varying ways by implementing
deallocation algorithms such as First-In-First-Out (FIFO), Second
Chance, and Least Recently Used (LRU). The deallocation algorithm that I
will be implementing is a second chance. In a second chance algorithm
when a page fault occurs the page frame at the front of the queue is
examined, if the access bit is equal to zero the page frame is removed
from the queue. Otherwise, the bit is cleared and reinserted into the
tail of the queue where another page frame is then examined. There are
many advantages to the second chance algorithm, it improves system
performance of real-time systems by reducing the number of page faults
and ensuring that frequently accessed pages remain in main memory.
Another advantage of second chance algorithms is how it indirectly
promote fairness by considering the recent usage history of pages, which
prevents certain pages from being constantly evicted.

![A diagram of a flowchart Description automatically
generated](media/image3.png){width="3.8898304899387575in"
height="2.5797167541557307in"}

The interactions between the chosen algorithms are crucial to the
efficiency of OS memory management operations. The next-fit algorithm
when called will refer to the free block linked list and select a block
by the next-fit algorithm. When a block is selected it is split, with
the allocated portion being removed from the free block list and
inserted into the busy block linked list. The remaining portion in the
linked list remains in the free block linked list. However, if the
next-fit algorithm fails to allocate a process memory space due to a
page fault, the second chance page replacement algorithm is invoked.

[Task 2:]{.underline}

Next fit pseudocode:

![A screenshot of a computer program Description automatically
generated](media/image4.png){width="4.215494313210849in"
height="6.153093832020997in"}

Second chance pseudocode:

![A computer screen with white text Description automatically
generated](media/image5.png){width="4.291887576552931in"
height="2.8126443569553805in"}

Free block/ Used block list pseudocode:

![A screenshot of a computer program Description automatically
generated](media/image6.png){width="4.319666447944007in"
height="4.833581583552056in"}

![A screenshot of a computer program Description automatically
generated](media/image7.png){width="4.277997594050744in"
height="5.840577427821522in"}

[Task 3:]{.underline}

Memory Tracking code:

![A screenshot of a computer program Description automatically
generated](media/image8.png){width="6.268055555555556in"
height="4.175in"}

![A screen shot of a computer program Description automatically
generated](media/image9.png){width="4.507176290463692in"
height="4.9655325896762905in"}

![A screenshot of a computer program Description automatically
generated](media/image10.png){width="4.11132217847769in"
height="0.5625284339457568in"}

Next fit algorithm code inside memory class:

![A screenshot of a computer program Description automatically
generated](media/image11.png){width="6.268055555555556in"
height="2.689583333333333in"}

![A computer screen shot of text Description automatically
generated](media/image12.png){width="5.632234251968504in"
height="3.3612839020122482in"}

![A screenshot of a computer screen Description automatically
generated](media/image13.png){width="6.268055555555556in"
height="3.2743055555555554in"}

Swapping method in memory class used to transfer blocks or pages between
lists:

![A computer screen with text on it Description automatically
generated](media/image14.png){width="4.9794225721784775in"
height="1.5486909448818897in"}

Second chance page replacement algorithm code inside memory class:

![A screenshot of a computer program Description automatically
generated](media/image15.png){width="6.268055555555556in"
height="3.1680555555555556in"}

Memory class:

![A screen shot of a computer code Description automatically
generated](media/image16.png){width="6.19476268591426in"
height="0.9444925634295713in"}

![A screen shot of a computer code Description automatically
generated](media/image17.png){width="5.069704724409449in"
height="1.652863079615048in"}

Linked List:

![A screenshot of a computer Description automatically
generated](media/image18.png){width="5.007201443569554in"
height="1.1736712598425196in"}

![A screen shot of a computer program Description automatically
generated](media/image19.png){width="5.882246281714786in"
height="5.028035870516185in"}

![A screen shot of a computer program Description automatically
generated](media/image20.png){width="5.8127985564304465in"
height="5.194711286089239in"}

![A computer screen shot of a program Description automatically
generated](media/image21.png){width="5.916970691163605in"
height="3.312670603674541in"}

![A screen shot of a computer Description automatically
generated](media/image22.png){width="6.268055555555556in"
height="3.301388888888889in"}

Block class:

![](media/image23.png){width="6.268055555555556in" height="3.94375in"}

![](media/image24.png){width="6.268055555555556in"
height="2.248611111111111in"}

![](media/image25.png){width="4.354390857392826in"
height="5.041925853018372in"}

![](media/image26.png){width="4.590513998250219in"
height="2.340398075240595in"}

Page class:

![](media/image27.png){width="4.896084864391951in"
height="5.007201443569554in"}

[PageTracker class (used to track all pages in memory):]{.underline}

![](media/image28.png){width="5.423889982502187in"
height="4.125212160979878in"}

![](media/image29.png){width="3.7988068678915137in"
height="1.9237095363079615in"}

[Node class:]{.underline}

![](media/image30.png){width="3.5418482064741905in"
height="3.4793460192475942in"}

[Task 4:]{.underline}

Inside the memory class there are three methods used to simulate the
execution of my algorithms. These methods are initialiseMemory(),
Process() and test() located in the memory class. There code can be seen
below.

![A computer screen with many colorful text Description automatically
generated](media/image31.png){width="5.666957567804024in"
height="4.11132217847769in"}

![A computer screen shot of text Description automatically
generated](media/image32.png){width="6.268055555555556in"
height="2.6041666666666665in"}

This is the result of from execution of these methods:

After Process() stop running when memory was full or there as no space
left for next process. Main memory looked like this.

![](media/image33.png){width="5.375276684164479in"
height="0.33335083114610675in"}

The blocks in free blocks represent the internal fragment that can occur
in next fit allocation algorithms. This is illustrative of internal
fragmentation however in other implementations block location in main
memory would have been factored in.

Once a memory error occurred when the used block list size was about to
exceed the limit of the main memory. The test() method was invoked which
tested the page replacement algorithm second chance. Page replacement
occurred as shown below when a block's page request would have exceeded
the size of the block.

![](media/image34.png){width="6.268055555555556in"
height="0.7743055555555556in"}

Page request resulted in the working set of a block being printed out
like this.

![](media/image35.png){width="6.268055555555556in"
height="0.5208333333333334in"}

The working set of a block was also accessed where the values of its
working set access bits were inverted.

![](media/image36.png){width="6.268055555555556in"
height="0.4791666666666667in"}

![A black screen with white text Description automatically
generated](media/image37.png){width="2.3334536307961504in"
height="0.9444925634295713in"}
