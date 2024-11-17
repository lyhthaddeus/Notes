# Datapath
Its literally just the Big diagram :)

![Datapath](https://github.com/lyhthaddeus/Notes/blob/main/WrittenNotes/CS2100/comp/Datapath.png)

> [!NOTE]
> The multiplexer at MemToReg is flipped (why? idk its probably a diagram thing)

# Data Control

### Types of Control Signals
| Control Signal | Execution Stage | Purpose | 
| - | - | - |
| RegDst | Decode/ Operand Fetch | Select the destination reg no. | 
| RegWrite | Decode / Operand Fetch / Reg Write | Enable Writing of reg | 
| ALUSrc | ALU | Select the 2nd operand for ALU | 
| ALUcontrol | ALU | Select the operation to be performed | 
| MemRead / MemWrite | Memory | Enable reading/ writing of data memory | 
| MemToReg | RegWrite | Select the result to be written back to register file | 
| PCSrc | Memory / RegWrite | Select the next PC value | 

### ALU CLoser Look

![ALU](https://github.com/lyhthaddeus/Notes/blob/main/WrittenNotes/CS2100/comp/ALU.png)
As seen in the table. the ALUcontrol quite literally is broken apart into three sections to help 
with the math <br>

To help us with designing the ALUControl, we generate a 2-bit ALUop signal from the Opcode first <br>
| Instruction type | ALUop |
| - | - |
| lw/sw | 00 | 
| beq | 01 | 
| R-type | 10 | 

with this we can work together with the funct field to make the ALUcontrol signal 
![ALUControl](https://github.com/lyhthaddeus/Notes/blob/main/WrittenNotes/CS2100/comp/ALUControl.png)

We then use big brain combinatorial circuits to get the answer from this :) <br>
![ALUControlCircuit](https://github.com/lyhthaddeus/Notes/blob/main/WrittenNotes/CS2100/comp/ALUControlCircuit.png)

> [!NOTE]
> This step is repeated again for all the other control signals 
> in fact, control design is just big brain combinatorial circuits 

### Control Design: Outputs
![Datapath+Control](https://github.com/lyhthaddeus/Notes/blob/main/WrittenNotes/CS2100/comp/Datapath+Control.png)


| _ | RegDst | ALUSrc | MemToReg | RegWrite | MemRead | MemWrite | Branch | ALUop | 
| - | ------ | ------ | -------- | -------- | ------- | -------- | ------ | ----- |
| R-Type | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 10 |
| lw | 0 | 1 | 1 | 1 | 1 | 0 | 0 | 00 |
| sw | X | 1 | X | 0 | 0 | 1 | 0 | 00 |
| beq | X | 0 | X | 0 | 0 | 0 | 1 | 01 | 

### Instruction Execution 
* Instruction Execution = 
    1. Read contents of one or more storage elements 
    2. Perform computation through some combinational logix 
    3. Write result to one or more storage elements
* All these perfromed **within a clock period**

### Single Cycle Implementation
To calculate time taken (assuming negligible delays) is to simply add them up. The clock cycle is simply the longest instruction. <br>
However, you realise that all instruction take as much time as the slowest one! 

* Solution 1: Multicycle implementation 
    * break up the instruction into execution steps
    * each execution step **take one clock cycle**
        * cycle time is much shorter (clock freq is higher)
    * Instruction would thus take *variable number of clock cycle* to complete execution
* Solution 2: Pipelining 
    * Refer to [Pipelining](https://github.com/lyhthaddeus/Note/blob/main/WrittenNotes/CS2100)  

    
