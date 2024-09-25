# ISA
There are 5 main concepts of the ISA design.
* [Data Storage](https://github.com/lyhthaddeus/Notes/blob/main/WrittenNotes/CS2100/ISA.md#data-storage) 
* [Memory Adderssing Mode](https://github.com/lyhthaddeus/Notes/blob/main/WrittenNotes/CS2100/ISA.md#memory-addressing-mode) 
* [Operations in the instruction sets](https://github.com/lyhthaddeus/Notes/blob/main/WrittenNotes/CS2100/ISA.md#operations-in-the-instruction-sets) 
* [Instruction format](https://github.com/lyhthaddeus/Notes/blob/main/WrittenNotes/CS2100/ISA.md#instruction-format) 
* [Encoding the instruction set](https://github.com/lyhthaddeus/Notes/blob/main/WrittenNotes/CS2100/ISA.md#encoding-the-instruction-set) 

# RISC vs CISC
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

# Operations In The Instruction Sets

# Instruction Format

# Encoding The Instruction Set
