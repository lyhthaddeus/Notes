# Pipelining 
### MIPS Pipeline stages
There are **5** Execution stage
* IF: Instruction Fetch
* ID: Instruction Decode and Register Read 
* EX: Execute an operation or calculate an address 
* MEM: Access an operand in data memory 
* WB: Write back the result into a register 

![Pipeline](https://github.com/lyhthaddeus/Notes/blob/main/WrittenNotes/CS2100/comp/PipelineDataControlPath.png) 

### Comparison of Performance
1. Single-Cycle Processor
    * The cycle time (CT<sub>seq</sub> would be the longest instruction (for e.g lw)
    * Execution time for I instructions => Time = I * CT<sub>seq</sub>              
    * it is held back by the slowest instruction
2. Multi-Cycle Processor 
    * The cycle time (CT<sub>multi</sub>) would be longest operation at a given stage (such as Inst Mem)
    * Execution time for I instructions => I * *Average CPI* CT<sub>multi</sub> 




