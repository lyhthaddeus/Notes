# ISA
There are 5 main concepts of the ISA design.
* [Data Storage](https://github.com/lyhthaddeus/Notes/blob/main/WrittenNotes/CS2100/ISA.md#data-storage) 
* [Memory Addressing Mode](https://github.com/lyhthaddeus/Notes/blob/main/WrittenNotes/CS2100/ISA.md#memory-addressing-mode) 
* [Operations in the instruction sets](https://github.com/lyhthaddeus/Notes/blob/main/WrittenNotes/CS2100/ISA.md#operations-in-the-instruction-sets) 
* [Instruction format](https://github.com/lyhthaddeus/Notes/blob/main/WrittenNotes/CS2100/ISA.md#instruction-format) 
* [Encoding the instruction set](https://github.com/lyhthaddeus/Notes/blob/main/WrittenNotes/CS2100/ISA.md#encoding-the-instruction-set) 

## RISC vs CISC
### Complex Instruction Set Computer
Example: x86-32 <br> 
* Single instruction performs complext operations 
* Complex implementation leave no room for hardware improvement 

### Reduced Instruction Set Computer
Example: ARM, MIPs
* Keep instruction set small and simple 
* Easy to optimise hardware

> [!NOTE]
> RISC is more common in the modern days due to more/ cheaper memory and 
> better optimised compilers

# Data Storage
the few concerns with **storage architecture** 
* Where do we store the operands so computation can be performed?
* Where do we store the computation results afterwards?
* How do we specify operands?

> [!NOTE]
> Operands may be implicit (taken from data structures like stacks or queue) 
> or explicit(Literally the address)

### Stack Architecture 
In this architecture, operands are implicitly on the top of the stack <br>
Exactly the same as in CS2040s

### Accumulator Architecture 
One operand is implicaitly in the accumulator (a special register): IBM 701

### General-purpose register Architecture (GPR)
Only explicit operands 
* Register-memory architecture: Intel 80386/ Motorola 68000
* Register-register (load-store) architecture: MIPs/ ARM/ M1

> [!NOTE]
> Most modern processors uses GPR

### Memory-memory architecture
All operands are read from memory: DEC VAX <br>
there is no use of registers, operans are taken from memory directly

# Memory Addressing Mode
There are three lines that connects the processors to the memory (*assume k-bit is 32*)
* k-bit address bus (32 bits)
    * stores the address
    * Uni-directional (processor => memory)
* n-bit data bus
    * stores the data 
    * Bi-directional
* control line
    * Controls whether the operation is a Read/ Write process 

### Process of Addressing
For **read**  access
1. processor place the respective address to address bus
2. set control line to read
3. data at that specific address is place in data bus
4. then data will be read via the data bus 

For **write** access
1. processor place the respective address to address bus
2. set control line to write
3. the data in the memory data register will then be written to the address 

> [!TIP]
> The ooga booga version is. data register tell you who you are 
> address register tell you where you are. control tell you what to do. 
> In the famous words of El-Melloi, Whodunnit, Wheredunnit, Whydunnit
> busses are just "pipes" for data transfer

### Endianness (lol Indian)
the relative order of bytes in a multi byte word stored.
* (high -> low): MSB -> LSB (Big-Endian)
    * MIPs/ IBM 360/ Motorola 68000
* (high -> low): LSB -> MSB (Little-Endian)
    * Intel 80x86/ DEC VAX

### Addressing Mode
![Addressing Mode](https://github.com/lyhthaddeus/Notes/blob/main/WrittenNotes/CS2100/comp/Addressing%20Mode.png) 

> [!NOTE]
> MIPs uses Register, Immediate and Displacement

# Operations In The Instruction Sets
Nothing much here. Just make sure your architecture caters to the more common 
instructions. Most frequently used instructon are (Load, Conditional Branch, Comapre and Store)

# Instruction Format
You have to consider two aspect of the instruction set
* Instruction Length
    * Variable Length: Intel 80x86 (var from 1 t 17 bytes)
        * Allow for more flexibility in instruction set
        * Usually used in CISC 
    * Fixed Length: MIPs
        * Simplify pipelining and parallelism
        * Allow fro easy fetch and decode

* Instruciton Field (Type and size of operand)
    * opcode (unique identifier)
    * operands (zero or more additional information required)

# Encoding The Instruction Set
