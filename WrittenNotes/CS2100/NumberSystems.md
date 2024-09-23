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
* Range: -127 -> +127

> [!NOTE]
> The MSB here still represents the sign 

### Converting from base 10 
1. write the base 10 into binary
2. if sign is positive ? do nothing :D 
3. else: flip all the bits 

eg  &ensp(14)<sub>10<sub> = (0000 1110)<sub>2<sub> = (0000 1110)<sub>1s<sub> <br>
    &emsp(-69)<sub>10<sub> = -(0100 0101)<sub>2<sub>  (1011 1010)<sub>1s<sub> <br>

# 2s Complement

* Largest Value: 0111 1111 = +127
* Smallest Value: 1000 0000 = -127
* Zeros:
    * 0000 0000: +0
* Range: -128 -> +127

### Converting from base 10 
1. write the base 10 into binary
2. if sign is positive ? do nothing :D 
3. else: flip all the bits
4. add 1 to the resultant binary

> [!TIP]
> You dont actually have to do it the long way a short cut would be: 
> starting from LSB copy everything until a 1 is encountered.
> copy that specific one then flip everything else

eg  &ensp(14)<sub>10<sub> = (0000 1110)<sub>2<sub> = (0000 1110)<sub>2s<sub> <br>
    &emsp(-69)<sub>10<sub> = -(0100 0101)<sub>2<sub>  (1011 1011)<sub>2s<sub> <br>

> [!Question]
> But why do we need 1s and 2s complement? the reason is so that we can 
> quickly perform addition. subtraction is hard for computers, so we instead
> do subtraction by means of adding a negative value. 1s and 2s complement
> allow us to perform these.
> A - B = A + (-B)


