# Logic Circuits
Nothing much here just the symbols for the circuits. We have AND, OR, NAND, NOR, XOR, NOT, just memorise those :D 

### Gray Code 
Its honestly a fancy way of binary where each increment only flips one bit. WHY IS THIS IMPT?? bc of Kmaps. heres 
an example gray code for reference 
| Decimal | Binary | Gray Code | 
| - | - | - | 
| 0 | 0000 | 0000 |
| 1 | 0001 | 0001 | 
| 2 | 0010 | 0011 | 
| 3 | 0011 | 0010 | 
| 4 | 0100 | 0110 | 
| 5 | 0101 | 0111 | 
| 6 | 0110 | 0101 |

etc etc. notice how each step only require one bit to be flip as opposed to traditional binary. this is good for error detection

### Karnaugh maps (The meat of logic circuits)
* Its a systematic method to obtain simplified SOP expression
* fun fact this is classified as an abstract form of a Venn Diagram organised as a matrix of squares

###### Example K-Map
![PreferedKMap](https://github.com/lyhthaddeus/Notes/blob/main/WrittenNotes/CS2100/comp/PreferedKMap.jpg)

###### Valid Groupings
![ValidGroupings](https://github.com/lyhthaddeus/Notes/blob/main/WrittenNotes/CS2100/comp/ValidGroupings.png) 

# Combinatorial Circuits
There are two kind of design methods for combinatorial circuits
* Gate-level design method (with logic gates)
* BLock-level design method (with functional blocks)

Here are the one we maybe probably need to memorise :)
### Half Adder
![HalfAdder](https://github.com/lyhthaddeus/Notes/blob/main/WrittenNotes/CS2100/comp/HalfAdder.png)

Nothing special here its just minterms => kmap => find simplified SOP <br>
the block diagram shown is just an abstraction of the combinatorial circuit (fyi its just a XOR for S and a AND for C)

### Full Adder
![FullAdder](https://github.com/lyhthaddeus/Notes/blob/main/WrittenNotes/CS2100/comp/FullAdder.png)

As expected, a "full" adder is two half adders and we use a OR gate to handle the carry. The abstraction 
from the block diagram really helps to simplify the design process (lesser gates to look at)

### 16-bit Parallel Adder 
![16bitParallelAdder](https://github.com/lyhthaddeus/Notes/blob/main/WrittenNotes/CS2100/comp/16bitParallelAdder.png)

Same thing again just larger now (4 full adder => 1 16bit parallel adder)

### BCD to Excess-3 Converter
![BCDtoE-3](https://github.com/lyhthaddeus/Notes/blob/main/WrittenNotes/CS2100/comp/BCDtoExcess-3.png)

We not only can string circuits together, we can also make use of other designed circuits for specialised task like here

### 4-bit Magnitude Comparator
![Comparator](https://github.com/lyhthaddeus/Notes/blob/main/WrittenNotes/CS2100/comp/4bitMagnitudeComparator.png)

for my sanity in making the notes, i will not show the circuit (its quite cancerous). 
Just know it takes in A3A2A1A0 and B3B2B1B0 and compare which is greater 

> [!NOTE]
> A3 here is the MSB which mean its the "largest" number
> we compare A3 > B3 then A2 > B2 ... A0 > B0 

### 6 Person Voting System (idk wtf this for)
![SNAFU](https://github.com/lyhthaddeus/Notes/blob/main/WrittenNotes/CS2100/comp/6PersonVotingSystem.png)

# MSI Components
Here are even more block diagrams... yay..

### 3x8 Decoders
![Decoder](https://github.com/lyhthaddeus/Notes/blob/main/WrittenNotes/CS2100/comp/Decoder.png) 

### 2x4 Decoder with Enable
![DecoderWithEnable](https://github.com/lyhthaddeus/Notes/blob/main/WrittenNotes/CS2100/comp/DecoderWithEnable.png) 

### 8x3 Encoders
![Encoder](https://github.com/lyhthaddeus/Notes/blob/main/WrittenNotes/CS2100/comp/Encoder.png) 

### 4x2 Priority Encoders
![prioEncoder](https://github.com/lyhthaddeus/Notes/blob/main/WrittenNotes/CS2100/comp/PriorityEncoder.png) 

### 4x1 Multiplexer
![mult](https://github.com/lyhthaddeus/Notes/blob/main/WrittenNotes/CS2100/comp/Multiplexer.png) 

### 1x4 Demultiplexer
![demult](https://github.com/lyhthaddeus/Notes/blob/main/WrittenNotes/CS2100/comp/Demultiplexer.png) 
