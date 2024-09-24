# MIPS
There are 32 registers in a MIPS assembly language <br>
| Name | Register Number | Usaage | 
| - | - | - |
| $zero | 0 | constant 0 | 
| $v0 - $v1 | 2-3 | values for results and expression evals | 
| $a0 - $a3 | 4-7 | arguments | 
| $t0 - $t7 | 8-15 | temp | 
| $s0 - $s7 | 16-23 | program variables | 
| $t8 - $t9 | 24-25 | more temps | 
| $gp | 28 | Global pointer | 
| $sp | 29 | stack pointer | 
| $fp | 30 | frame pointer | 
| $ra | 31 | return address | 

All instruction in Mips has a fixed length of 32 bits
and they come in three different formats
* R format(Register format): for instructions with 2 src and1 dest
* I format(immediate format): for instruction with 1 src and 1 immediate and 1 dest
* J format(jump format): uses only 1 immediate 

> [!TIP]
> later you will see rs, rt and rd. to avoid being confused
> they each respectively stand for src, targ, dest.

### R format (Register)
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

#### Encoding R format 
1. notice your Mips instruction are always in form that
dest comes right after instruction name
2. opcode is trivally 0, your funct is obtained from green sheet
3. move the rd to the back to get the form in step 1 
4. write it all out in binary representation
5. convert them to hex

> [!WARNING]
> shamt is only used in shift (eg sll/ srl) it is 0
> otherwise, and in these
> shift operations, rs will be 0.

Example 1.0: <br>
add $8, $9, $10 (add 9 and 10 then store to 8) <br>
| R format fields | Value | 
| - | - | 
| opcode | 0 | 
| rs | 9 | 
| rt | 10 | 
| rd | 8 | 
| shamt | 0 | 
| funct | 32(greensheet) | 

results: 000000 01001 01010 01000 00000 100000 <br>

conversion: 0000 0001 0010 1010 0100 0000 0010 0000 <br>
=> 0x012A4020 <br>

Example 1.1: <br>
sll $8, $9, 4
| R format fields | Value | 
| - | - | 
| opcode | 0 | 
| rs | 0 | 
| rt | 9 | 
| rd | 8 | 
| shamt | 4 | 
| funct | 0(greensheet) | 

results: 000000 00000 01001 01000 00100 000000 <br>

conversion: 0000 0000 0000 1001 0100 0001 0000 0000<br>
=> 0x00094100 <br>

### I format (Immediate)
used for all instruction that require a immediate.
| 6 | 5 | 5 | 16 | 
| - | - | - | - |
| opcode | rs | rt | immediate |

> [!NOTE]
> rd, shamt and funct are merch to form 16 bits immediate

> [!CAUTION]
> unlike in R where everything is unsigned, the immediate is 
> signed int in 2s complement

#### Encoding I format
1. notice that similar to R format, the target comes right
after the instruction name (swapping required) except for 
branch
2. Get opcode from greensheet
3. move the rt to the back, unless it is branch (then keep it the same)
4. write it all out in binary
5. convert to hex

Example 2.0 <br>
addi $21, $22 , -50
| I format field | value | 
| - | - | 
| opcode | 8(greensheet) | 
| rs | 22 | 
| rt | 21 | 
| immediate | -50 |

results: 001000 10110 10101 (1111 1111 1100 1110)<sub>2s</sub> <br> 

conversion: 0010 0010 1101 0101 1111 1111 1100 1110 <br> 
=> 0x22D5FFCE <br>

Example 2.1 <br>
lw $9, 12($8)
| I format field | value | 
| - | - | 
| opcode | 35(greensheet) | 
| rs | 8 | 
| rt | 9 | 
| immediate | 12 |

results: 100011 01000 01001 (0000 0000 0000 1100)<sub>2s</sub> <br>

conversion: 1000 1101 0000 1001 0000 0000 0000 1100 <br>
=> 0x8D09000C <br>

Example 2.2 <br> 
```asm
Loop:   beq     $9, $0, End ; Encode this line
        add     $8, $8, $10 ; Start counting jump from here PC + 4  
        addi    $9, $9, -1  ; 1
        j       Loop        ; 2
End:                        ; 3
```
> [!NOTE]
> immediate in branch instruction represents the *relative* jump from the
> PC + 4 location. since instructions are always word aligned, we / 4 to save
> 2 bits of space. that is if immediate is one => that represents a 4 byte jump

| I format field | value | 
| - | - |
| opcode | 4(greensheet) |
| rs | 9 | 
| rt | 0 | 
| immediate | 3 |
> [!TIP]
> There is no need to swap the rs rt positions

results: 000100 01001 00000 (0000 0000 0000 0011)<sub>2s</sub> <br>

conversion: 0001 0001 0010 0000 0000 0000 0000 0011 <br>
=> 0x1120003 <br>

### J format (Jump)
| 6| 26 | 
| - | - |
| opcode | target address | 

> [!NOTE]
> the address here is similar to branch address that it is word aligned, we can 
> count in words instead of bytes (last 2 digits are 00 always).

#### Encoding J format
1. find the opcode from greensheet
2. get the address to be jump towards, omit the last 2 digits (00)
3. copy all  28 bits
4. convert to hex

Example 3.0 <br> 
```asm
Loop:   beq     $9, $0, End ; addr: 8  <- target
        add     $8, $8, $10 ; addr: 12 
        addi    $9, $9, -1  ; addr: 16
        j       Loop        ; addr: 20 <- PC
End:                        ; addr: 24 <- PC + 4 (MSB of address 0000)
```
The immediate would only be 28 bits even after removing the last two digits (00)
The last 4 bits of information is obtained from the MSB of PC + 4, this restricts all 
jumps to a 256MB boundary <br>

| J format field | value | 
| - | - | 
| opcode | 2 |
| target address | 8 | 

results: 000010 (0000 0000 0000 0000 0000 0000 10) <br>

conversion: 0000 1000 0000 0000 0000 0000 0000 0010 <br>
=> 0x08000002 <br>

> [!NOTE]
> the resultant address for this specific example would be 
> (0000)<sub>MSB from PC+4</sub> (0000 0000 0000 0000 0000 0000 10)<sub>addr calculated</sub> (00)<sub>00 since we divide 4</sub>


