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

eg  &ensp;(14)<sub>10</sub> = (0000 1110)<sub>2</sub> = (0000 1110)<sub>1s</sub> <br>
    &emsp;&emsp;(-69)<sub>10</sub> = -(0100 0101)</sub>2<sub>  (1011 1010)<sub>1s</sub> <br>

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

eg  &ensp;(14)<sub>10</sub> = (0000 1110)<sub>2</sub> = (0000 1110)<sub>2s</sub> <br>
    &emsp;&emsp;(-69)<sub>10</sub> = -(0100 0101)<sub>2</sub>  (1011 1011)<sub>2s</sub> <br>

> [!Note]
> But why do we need 1s and 2s complement? the reason is so that we can 
> quickly perform addition. subtraction is hard for computers, so we instead
> do subtraction by means of adding a negative value. 1s and 2s complement
> allow us to perform these.
> A - B = A + (-B)

# Binary Maths 

> [!WARNING]
> Signed numbers are of fixed range. if the result of additon/ subtraction goes
> out of range, an overflow occurs.
> can be detected easily by: p + p = n || n + n = p 
> this would not happen to p + n (positive and negative addition will always be in range)

### 2s complement addition
1. convert all negatives values into their respective 2s complement representation 
2. if there is subtraction involved, format equation into form A + (-B)
3. simply add them as you would for normal binary numbers
4. throw away the carry out of the MSB

### 1s complement addition
1. if positive ? perform binary addition as per usual
2. if there is a carry out MSB, add 1 to the result
3. for subtraction, convert into form A + (-B)
4. perform step 1 and 2 again

> [!NOTE]
> The main difference between 2s and 1s complement addition is the extra step of adding the
> carry out of the MSB to the result

# Excess representation
Very simply, excess *x* simply means we minus x from the binary number such that our 
range is from -x -> x - 1 

eg excess-8 (4 bits)
| Excess-8 | Value(-) | Excess-8 | Value(+) |
| ------------- | -------------- | -------------- | - |
| 0000 | -8 | 1000 | 0 |
| 0001 | -7 | 1001 | 1 | 
| 0010 | -6 | 1010 | 2 |
| 0011 | -5 | 1011 | 3 | 
| 0100 | -4 | 1100 | 4 |
| 0101 | -3 | 1101 | 5 | 
| 0110 | -2 | 1110 | 6 |
| 0111 | -1 | 1111 | 7 |

# IEEE 754
There are 3 components making up the IEEE 754 floating point representation
1. sign
2. exponent
3. mantissa

it represents the binary in **normalised** format (3.0 * 10<sup>8</sup>) <br>
eg -1.101 * 2<sup>2</sup>

### sign 
Its either 1(-) or 0(+) 

### exponent
Expressed in excess-127 (8 bits)

### mantissa
23 bit number in binary

### converting from base 10 
1. convert your float into binary representation
2. record the sign bit
3. normalise your binary such that it is in the form 1.xxx * 10<sup>y</sup>
4. record your exponent y 
5. ignore the first digit of the mantssa (the 1 as its is trivially assumed) then record the decimals (xxx) into the mantissa. Append 0 to the left until 23 bits
6. string it all together as <sign><exponent><mantissa>
7. convert the long 32 bit number into hex 

eg -6.5 <br>
&emsp;&emsp; -6.5 = -(0110.10) <br>
&emsp;&emsp; sign: 1 <br>
&emsp;&emsp; 0110.10 -> 1.101 * 2<sup>2</sup> <br> 
&emsp;&emsp; exponent: 2 <br>
&emsp;&emsp; matissa: 101 -> 101 0000 0000 0000 0000 0000 (23bits)
&emsp;&emsp; All together: 1 1000 0001 101 0000 0000 0000 0000 0000 -> <br>
&emsp;&emsp; 1100 0000 1101 0000 0000 0000 0000 0000 <br> 
&emsp;&emsp; 0xC0D00000
