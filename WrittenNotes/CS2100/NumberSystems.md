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

> [!TIP]
> You can perform _quick maths_ with the common bases (2, 16)
> by splitting a long base 2 string of numbers into sets of 4
> you can convert each set to its corresponding base 16
> eg (1100 0100 -> 0xC4)

# Sign-and-Magnitude (SM)
The first bit represents the sign (+/-) while the rest represents
the number itself.
eg 10000100 -> 1 000 0100 -> -4

* Largest Value: 0111 1111 = +127
* Smallest Value: 1111 1111 = -127
* Zeros:
    * 0000 0000: +0
    * 1000 0000: -0

> [!WARNING]
> this is assuming Sign-and-Magnitude is 8 bits (Same for 1s and 2s 
> complement below)

# 1s Complement

* Largest Value: 0111 1111 = +127
* Smallest Value: 1000 0000 = -127
* Zeros:
    * 0000 0000: +0
    * 1111 1111: -0

> [!NOTE]
> The MSB here still represents the sign 

### Converting from base 10 
1. write the base 10 into binary
2. if sign is positive ? do nothing :D 
3. else: flip all the bits 

eg  (14)*10* = (0000 1110)*2* = (0000 1110)*1s*
    (-69)*10* = -(0100 0101)*2* = (1011 1010)*1s*

