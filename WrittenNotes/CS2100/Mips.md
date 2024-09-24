# MIPS
All instruction in Mips has a fixed length of 32 bits
and they come in three different formats
* R format(Register format): for instructions with 2 src and1 dest
* I format(immediate format): for instruction with 1 src and 1 immediate and 1 dest
* J format(jump format): uses only 1 immediate 

### R format
| 6 | 5 | 5 | 5 | 5 | 6 |
| - | - | - | - | - | - | 
| opcode | rs | rt | rd | shamt | funct | 

Each field is an independent 5/ 6 bit **unsigned** int  <br>
the opcode for R format is always 0 (as the information on
what kind of instruction is from the func)

> [!Note]
> since there are only 32 registers, 5 bits is more than
> enough to represent all. Similarly for shamt, shifting
> 32 bits in any direction clears the register

##### Encoding Mips 
1. notice your Mips instruction are always in form 
<instruction name> <rd> <rs> <rt>
2. opcode is trivally 0, your funct is obtained from green sheet
3. move the rd to the back to get the form in step 1 
4. write it all out in binary representation
5. convert them to hex


