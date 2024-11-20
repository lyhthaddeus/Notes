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

> [!NOTE]
> in an ideal world, Speedup_pipeline = Time_seq / Time_pipeline ≈ N 
> However our world is far from ideal

### Pipeline Hazards
Our ideal pipeline works on the hope and dreams assumption that a new instruction 
can be 'pumped' into pipeline every cycle (aka no delays). However that is not true as there are pipeline Hazards
* Stuctural Hazards (simultaneous use of hardware resource)
* Data Hazards (data dependencies between instructions)
* Control Hazards (Change in program flow like in branch)

we will discuss some possible solutions and limitations

### Structural Hazards 
This is the most striaght forward fix 
* Stall the Pipeline (delay to "wait for your turn")
* Seperate the hardware for Data and Instruction Memory to avoid the clash
* Split cycle into half (first half write; second half read)
    * this is only possible bc register are fast

### Data Hazards
One of the main reason data hazards occur is due to **Instruction Dependencies** such as 
RAW (Read after Write), WAW (Write after Write), WAR (Write after Read) <br>

![TrueDataDependency](path) 

Solution: **Forwarding**: forward the result from one stage to anther and bypass data read from register file <br>

![Forwarding](path) 

> [!TIP]
> The logic for forward lies in the fact that the data has already been calculated (just not written to register yet)
> instead of waiting for the WB stage, we just take it from the previous stage directly.

![LOADForwarding](path) 

> [!CAUTION]
> Forwarding **CANNOT** be used as a solution for lw as load instructions only get the data after MEM stage 
> to solve this we have no choice but to stall the pipeline then forward after the MEM stage
