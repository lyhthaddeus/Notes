# Sequential Circuits
There are two kinds of sequential circuits 
* Synchronous: output change only at specific times (latches)
* Asynchronous: outputs change at any time (flip-flops)

Next is just a bunch of latches/ flip-flops to memorise :)

### S-R Latch (Active high)

| S | R | Q | Q' | _ |
| - | - | - | - | - |
| 0 | 0 | NC | NC | Q(t) no change |
| 0 | 1 | 0 | 1 | 0 Latch RESET | 
| 1 | 0 | 1 | 0 | 1 Latch SET | 
| 1 | 1 | 0 | 0 | Indeterminate | 

Q(t + 1) = S + R'.Q <br> 
S.R = 0 <br>

> [!NOTE]
> Active Low was in lecture slides (but said can skip). it is just the opposite.

> [!NOTE]
> Gated S-R Latch are also tested, it works exactly the same except now with enable at 1 and memorises when enable at 0 (no change)

### D-Latch (Gated)

| EN | D | Q(t + 1) | 
| - | - | - | 
| 1 | 0 | 0 RESET | 
| 1 | 1 | 1 SET | 
| 0 | X | Q(t) No Change | 

When EN = 1; Q(t + 1) = D

### S-R Flip-flop 

| S | R | CLK | Q(t + 1) | 
| - | - | - | - |
| 0 | 0 | X | Q(t) No change | 
| 0 | 1 | ↑ | 0 RESET | 
| 1 | 0 | ↑ | 1 SET | 
| 1 | 1 | ↑ | ? Invalid | 

> [!NOTE]
> Similar to the S-R latch, Q(t + 1) = S + R'.Q 

### D Flip-flop

| D | CLK | Q(t + 1) | 
| - | - | - | 
| 1 | ↑ | 1 SET | 
| 0 | ↑ | 0 RESET | 

> [!NOTE]
> Similar to the D latch, Q(t + 1) = D 

One main application for a D Flip-flop would be to transfer logic-circuit outputs to flip-flops for storage purposes

### J-K Flip-flop

| J | K | CLK | Q(t + 1) | 
| - | - | - | - |
| 0 | 0 | ↑ | Q(t) No change | 
| 0 | 1 | ↑ | 0 RESET | 
| 1 | 0 | ↑ | 1 SET | 
| 1 | 1 | ↑ | Q(t)' Toggle | 

> [!TIP]
> It work **nearly** identical to S-R Flip-flop except for the invalid state become a toggle 

### T flip-flop 

| T | CLK | Q(t + 1) | 
| - | - | - | 
| 0 | ↑ | Q(t) No Change | 
| 1 | ↑ | Q(t)' Toggle |

> [!TIP]
> Its a single input version of the J-K flip-flops formed by tying both inputs together. 
> It can be viewed as a J-K flip-flops without the set/ reset 

### Asynchronous inputs
For all 3 (without T) flip-flops, we can make them asynchronous by adding the PRE/CLR 
* when PRE = HIGH; Q is **immediately** HIGH
* when CLR = HIGH; Q is **immediately**

### Sequential Circuits Analysis
To be blunt, no easy way to git gud besides practise :). Here are the steps 
1. From the circuit diagram, get the state equations (e.g A'.x)
2. From the state equation and output function (y), derive the state table (i.e the truth table)
3. From the state table we can draw out the state diagram (the circles with the arrows)

> [!CAUTION]
> For unused states, the circuit is known to be **self-correcting** if the unused state point back to a used state after a finite number of cycles 

### Sequential Circuits Design
Similarly to analysis, no easy way but practise. Heres the step by step 
1. From the given set of specifications (state equations, state table, state diagram) get your **excitation table**
2. Derive the state table then perform any state reduction if needed 
3. K-Map for all the input functions to get their simplified state equations
4. Using this draw the circuit diagram :)

> [!WARNING]
> The K-Map in this case is unique for each input. Meaning a J-K flip-flops would require 4 K-Maps 

### Memory 
Memory stores program and data (duh) and come in a hierachy 
1. Registers (Fast but ex)
2. Main memory 
3. Disk storage 
4. Magnetic Tape (Slow and cheap)

Data transfer from processcor to memory also include two additonal Registers
* MAR (Memory Address Register)
    * k-bit address bus
    * used to "locate" address of memory 
* MDR (Memory Data Register)
    * n-bit data bus 
    * used for Read/ Write of data to/ from memory
* Control line 
    * it is either R (read) or W (write)
    * R = W' (they are opposite of each other)

| Memory Enable | Read/ Write | Memory Operation | 
| - | - | - | 
| 0 | X | None | 
| 1 | 0 | Write to selected word | 
| 1 | 1 | Read from selected word | 

Lastly theres the memory cell, they come in two types
* Static RAM (uses flip-flops as memory cells)
* Dynamic RAM (uses capacitors charges to represent data) 

we string a bunch of them together to form memory arrays

4x3 Memory Array <br>
![4x3Ram](https://github.com/lyhthaddeus/Notes/blob/main/WrittenNotes/CS2100/comp/4x3Ram.png) <br>

4k x 8 Memory Array <br>
![4kx8Ram](https://github.com/lyhthaddeus/Notes/blob/main/WrittenNotes/CS2100/comp/4Kx8Ram.png) <br> 
