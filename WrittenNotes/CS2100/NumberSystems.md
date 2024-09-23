# Number System Basics
Converting from base 10.
* if >= 0 
    * perform repeated division by 2 
    * record the remainders from LSB -> MSB
* if < 0
    * perform repeated multiplication by 2 
    * record the number in the 1s position from 
        LSB -> MSB

Converting from Base x to Base y
1. First convert Base x to Base 10
2. Convert the resultant Base 10 to Base y

> [!NOTE]
> You can perform _quick maths_ with the common bases (2, 16)
> by splitting a long base 2 string of numbers into sets of 4
> you can convert each set to its corresponding base 16
> eg (1100 0100 -> 0xC4)
