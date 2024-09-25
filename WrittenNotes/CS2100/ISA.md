# ISA
There are 5 main concepts of the ISA design.
* [Data Storage](https://github.com/lyhthaddeus/Notes/blob/main/WrittenNotes/CS2100/ISA.md#data-storage) 
* Memory Adderssing Mode
* Operations in the instruction sets
* Instruction format
* Encoding the instruction set 

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
In this architecture, operands are implifcitly on the top of the stack
