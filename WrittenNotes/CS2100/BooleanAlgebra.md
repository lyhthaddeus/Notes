# Boolean Algebra
### Laws of Boolean Algebra
| Law | OR | AND | 
| ------------ | ----------------- | ------------- | 
| Identity Law | A + 0 = 0 + A = A | A.1 = 1.A = A | 
| Inverse/ Complement Law | A + A' = A' + A = 1 | A.A' = A'.A = 0 | 
| Commutative Law | A + B = B + A | A.B = B.A | 
| Associative Law | A + (B + C) = (A + B) + C | A.(B.C) = (A.B).C | 
| Distributive Law | A.(B + C) = (A.B) + (A.C) | A + (B.C) = (A + B).(A + C) | 

### Theorem 
| Law | OR | AND |  
| - | - | - |
| Idepotency | X + X = X | X.X = X | 
| One / Zero element | X + 1 = 1 + X = 1 | X.0 = 0.X = 0 | 
| Involution | (X')' = X | _ | 
| Absorption 1 | X + X.Y = X | X.(X + Y) = X |
| Absorption 2 | X + X'.Y = X + Y | X.(X' + Y) = X.Y |
| DeMorgans' | (X + Y)' = X'.Y' | (X.Y)' = X' + Y' |
| Consensus | X.Y + X'.Z + Y.Z = X.Y + X'.Z | (X+Y).(X'+Z).(Y+Z) = (X + Y).(X' + Z) | 

### Standard Forms
We have two standard forms:
* Sum-of-Products (SOP)
    * A product term or logical sum of several product terms
    * A + B'.C.D + D.A
* Product-of-Sum (POS)
    * A sum term or a logical product of several sum terms
    * (A + B).(C + D).A

> [!NOTE]
> All literal such as x and x' etc are trivially SOP and POS alone
> This is because literals are also product/ sum terms

> [!CAUTION]
> X + Y + Z is a POS and a SOP. Since we can view it as (X + Y + Z) i.e one sum term
> similarly X.Y.Z' is also both SOP and POS as it is a singular product term

### Minterm/ Maxterms
* Minterms of n variables is a **product term** that contains n literals
* Maxterms of n variables is a **sum term** that contains n literals

Notation wise we can simply view minterm as the "binary value" (e.g m3 => A'.B'.C.D => 0011 => binary 3) <br>
Maxterms are the opposite where M3 is A + B + C' + D' => 1100 => *flip bits* 0011 => binary 3 

> [!TIP]
> To gather "Canonical Form" representation, obtain sum-of-minterms expression by gathering the minterms of the function where output is 1 and opposite for the maxterms (gather when output is 0)

Example :)
| x | y | z | F1 | F2 | F3 | 
| - | - | - | - | - | - |
| 0 | 0 | 0 | 0 | 0 | 0 | 
| 0 | 0 | 1 | 0 | 1 | 1 | 
| 0 | 1 | 0 | 0 | 0 | 0 | 
| 0 | 1 | 1 | 0 | 0 | 1 | 
| 1 | 0 | 0 | 0 | 1 | 1 |
| 1 | 0 | 1 | 0 | 1 | 1 | 
| 1 | 1 | 0 | 1 | 1 | 0 |
| 1 | 1 | 1 | 0 | 1 | 0 |

F1 = x.y.z' = m6 <br> 
F2 = (x+y+z).(x+y'+z).(x+y'+z') = M0.M2.M3 = M(0, 2, 3)
