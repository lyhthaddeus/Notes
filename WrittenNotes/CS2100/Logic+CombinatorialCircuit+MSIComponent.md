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

