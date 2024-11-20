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
    * Execution time for I instructions => I * *Average CPI* * CT<sub>multi</sub> 
3. Pipeline Processer 
    * Cycle time (CT<sub>pipeline</sub>) would be longest operation + pipeline overhead (time require to read pipline reg)
    * **IN IDEAL SCENARIO** cycle require for I instructions = I + N - 1 (require N-1 cycle to fill the pipeline)
    * Execution time for I instructions => (I + N - 1) * CT<sub>pipeline</sub>

$$\text{Speedup}_{\text{pipeline}} = \frac{\text{Time}_{\text{seq}}}{\text{Time}_{\text{pipeline}}}$$
$\sqrt{3x-1}+(1+x)^2$ <br>




