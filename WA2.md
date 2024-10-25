# Question 1: Contest T-Shirts (4 × 5 + 1 + 1 = 22 marks)
The following problem is actually available at a certain online judge,
but assume that you don’t have access to it.
Prof Halim and his Centre for Nurturing Computing Excellence (CeNCE) team
organizes many programming contests. In fact, he and his team will organise the
prestigious ICPC Asia Pacific Championship 2025 in SoC during recess week of
semester 2 of this AY24/25. One thing that is common in those contests is contest T-
shirts. CeNCE publishes the actual size (Singapore/Asian version) of those T-shirts
upfront in the contest webpage. Upon reading those T-shirt size information, usually
contestants declare their preferred T-shirt size upfront during contest registration.
We assume that these contestants correctly measure their T-shirt sizes and entered
their correct T-shirt sizes data to the registration system. But it can still happen
that:
• The T-shirt vendor doesn’t have enough T-shirts of certain size,
• The T-shirt vendor accidentally supplied less (more likely) or more (less likely)
T-shirts of certain size,
• A bundle of T-shirts of a certain size got accidentally damaged during transport,
• We have to cut budget and ignore those (much more) expensive XXXL size, etc. <br>
<br> 
For this problem, let’s assume that there are seven different available T-shirt sizes
from the largest to the smallest: XXXL, XXL, XL, L, M, S, and XS. CeNCE has
prepared a certain number of each T-shirt sizes. A contestant is happy if he/she
receives a contest T-shirt of exactly his/her size. He/she is still moderately happy if
he/she receives a contest T-shirt that is just one size slightly bigger/slightly smaller
than his/her size, e.g., prefers XL but receives either XXL or L. Obviously for
XXXL/XS size, there is only one other alternative, i.e., XXL/S, respectively.
Today is the registration and opening ceremony day. The registration committee
opens the T-shirt boxes and ask the following distribution problem (details below).

### Input
The first line of the input contains an integer T C that denotes the number of test
cases.
The first line of each test case is a blank separator line.
Then, we have a line that contains 7 integers that denotes the number of XXXL,
XXL, XL, L, M, S, and XS T-shirts that CeNCE has prepared. Then, we have a 1
line with just an integer N that denotes the number of contestants. Finally, we have
a line with contains N strings of either ‘XXXL’, ‘XXL’, ‘XL’, ‘L’, ‘M’, ‘S’, ‘XS’ that
denotes the T-shirt size that each contestant has selected during registration. These
strings are not sorted in any order.

### Output
For each test case you are to print a line containing:
• ‘ALL IS WELL’ if each contestant receives a (one) T-shirt exactly as he/she
prefer, or
• ‘still acceptable’ if each contestant receives a (one) T-shirt as he/she prefer
or at least +/- 1 size away compared to his/her preference, or
• ‘argh... :(’ if there is at least one contestant that has no proper T-shirt for
him/her (e.g., wants XXXL but only 1 XL left).
Constraints
• 1 ≤ T C
• 1 ≤ N
• The number of T-shirt of any size is non-negative and at most 200 000.

### Sample Input
3 <br>
0 0 2 1 0 0 1 <br>
3 <br>
XL XS L <br>
0 0 1 2 0 0 0 <br>
3 <br>
XL L XXL <br>
0 0 1 1 0 0 0 <br>
2 <br>
XXXL L <br>
Sample Output <br>
ALL IS WELL <br>
still acceptable <br>
argh... :( <br>

### Design and analyze an algorithm to fully-solve this problem. Follow the steps below:
1. Not-yet a greedy algorithm. Design a simple Θ(N ) pre-processing check to determine if
a test case can be answered with ‘ALL IS WELL’ ? Hint: Check the first test case of the
Sample Input/Output.

```python 
from enum import Enum 

class ShirtSize(Enum): 
    XXXL = 0 
    XXL = 1 
    XL = 2 
    L = 3 
    M = 4 
    S = 5
    XS = 6 

def pre_processing():
    test_cases = int(input())
    for _ in range(test_cases):
        supply = list(map(int, input().split())) # Shove the given t-shirt into arr 
        num_ppl = int(input())
        sizes = input().split()
        for size in sizes:
            sizes_sorted[ShirtSize[size].value] += 1 # count sort for next question
        for i in range(len(sizes_sorted)):
            if sizes_sorted[i] > supply[i]:
                return argh_or_acceptable(supply, sizes_sorted) # next question
        return "All is well" # if all demand is lesser than supply, we are happy
```

for this simple do a lookup. As you read in the available sizes provided by the vendor,
put them in a static array, where index 0 -> XXL; 1 -> XL ... and the element correspond
to the number available. (Its a one-to-one translation of the input data into a static arr) <br>
Next as we read the input for the desired size (in no particular order) and do a count sort 
to get a sorted static arr (same structure as the supply). <br>

Lastly we just compare the values of both arr. it is only "all is well" when supply > demand 
this is O(n) as count sort is O(n) and we loop through once more to check supply > demand 
overall T(n) = 2n => O(n)

2. Assuming that we are now under the case where ‘ALL IS WELL’ is not possible. Describe
the greedy choice that can be used to differentiate ‘still acceptable’ (there is an optimal
T-shirt distribution to make this happen) versus ‘argh... :(’ (even if the registration
committee members try their best, there is at least one contestant that has no proper
T-shirt for him/her) answers. Prove the correctness of your greedy choice. PS: If your
greedy choice is correct but your proof is not, you will still get partial marks.

```python
def argh_or_acceptable(supply, sizes_sorted):
    for i in range(len(sizes_sorted)):
        while sizes_sorted[i] > 0:
            # check larger first 
            # if larger not out of count(XXXL) or no larger size
            if i - 1 >= 0 and supply[i-1] > 0:
                supply[i-1] -= 1 
                sizes_sorted[i] -= 1
            # assign best suited actual size
            elif supply[i] > 0: 
                supply[i] -= 1 
                sizes_sorted[i] -= 1
            # lastly assign smaller 
            # if smaller not out of bount(XS) or no smaller size
            elif i + 1 <= len(sizes_sorted) and supply[i+1] > 0:
                supply[i+1] -= 1 
                sizes_sorted[i] -= 1
            else: 
                return "arghh"
    return "still acceptable"
```
Using the sorted demand sizes from prev question (using count sort) and the static arr 
of supply. we first start at the most restricted size (either XS or XXXL).
we try as much as possibly to greedily assign larger sizes assignments first. if demand for 
"L" and "L" is available, we give him XL first.
in the case where there is no larger suited size, we check actual size first than smaller 
(the reason in my head to check large first than small is bc we do not want to "steal" 
potential shirts from customers we have yet to give shirts to)

### Proof:
Invariant:after every assignment of t-shirt, the resultant remaining t-shirt supply will 
          have max(size <= customer desired size) (since we select large as much as possible) <br>
* If there were a better solution than the one produced by the greedy algorithm, it would mean 
the algorithm made a "suboptimal" choice at some point, leading to "argh..." instead of 
"still acceptable." 
* This could only happen if the algorithm assigned an exact or smaller size when a larger size 
was still available. 
* Doing so would prevent future contestants from receiving their exact size, resulting in a worse 
overall outcome. 
* However, since the algorithm always prioritizes assigning larger sizes first, this suboptimal 
scenario cannot occur. Therefore, the greedy approach guarantees the correct result.

3. Also on the case where ‘ALL IS WELL’ is not possible. Describe the optimal sub-structure
of this problem and prove its correctness.

Assuming we already have a optimal solution R* with C* customers and T* t-shirts, 
if we remove the i-th customer and his corresponding t-shirt size, the remaining 
C* - i-th customer and its corresponding T* - i-th t-shirt (corresponding to the removed 
customer will be an optimal sub-structure

### Proof:
* Initial Optimality: By assumption, R∗ is the optimal solution for all C∗ customers, meaning
no other assignment of T-shirts could result in "still acceptable"
This implies that each pairing in R∗ is the best possible assignment for the respective customer.
* Removing One Customer: When we remove the i-th customer and their assigned T-shirt: The remaining 
C∗−1 customers still have their T-shirts assigned optimally as no reassignment of the remaining 
customers is required. This is because, in the optimal solution, there is a one-to-one correspondence 
between the customers and the T-shirts they receive. Removing one such pair doesn’t affect the remaining 
customers, who still retain the best possible assignments.
* Subproblem Solution: The remaining C∗−1 customers and their corresponding T∗−1 T-shirts now form a subproblem 
that retains the same optimal properties as the original problem. The assignment for these
C∗−1 customers is still the best possible solution for them because it is a subset of the original 
optimal solution R∗.
* No Better Solution: If there were a better solution for the subproblem (the C∗−1 customers), that 
solution could have been extended to provide a better solution for the original problem (the C∗ customers). 
But this contradicts the assumption that R∗ was optimal for the original problem.


4. Greedy algorithm, once proven to be correct, can usually be implemented with a short
implementation. Combine all the information above to implement a short Θ(T C · N )
solution in pseudo-code (as you cannot really test this problem live this time) or in
C++|Python|Java (to at least self-test with the Sample Input/Output above).

```python 
from enum import Enum 

class ShirtSize(Enum): 
    XXXL = 0 
    XXL = 1 
    XL = 2 
    L = 3 
    M = 4 
    S = 5
    XS = 6 

def pre_processing():
    test_cases = int(input())
    for _ in range(test_cases):
        supply = list(map(int, input().split())) # Shove the given t-shirt into arr 
        num_ppl = int(input())
        sizes = input().split()
        for size in sizes:
            sizes_sorted[ShirtSize[size].value] += 1 # count sort for next question
        for i in range(len(sizes_sorted)):
            if sizes_sorted[i] > supply[i]:
                return argh_or_acceptable(supply, sizes_sorted) # next question
        return "All is well" # if all demand is lesser than supply, we are happy

def argh_or_acceptable(supply, sizes_sorted):
    for i in range(len(sizes_sorted)):
        while sizes_sorted[i] > 0:
            # check larger first 
            # if larger not out of count(XXXL) or no larger size
            if i - 1 >= 0 and supply[i-1] > 0:
                supply[i-1] -= 1 
                sizes_sorted[i] -= 1
            # assign best suited actual size
            elif supply[i] > 0: 
                supply[i] -= 1 
                sizes_sorted[i] -= 1
            # lastly assign smaller 
            # if smaller not out of bount(XS) or no smaller size
            elif i + 1 <= len(sizes_sorted) and supply[i+1] > 0:
                supply[i+1] -= 1 
                sizes_sorted[i] -= 1
            else: 
                return "arghh"
    return "still acceptable"
```

5. Suppose we generalizes this problem, i.e., a contestant is happy not just with his/her
preferred T-shirt size, or one size bigger, or one size smaller, but a specific subset of X
T-shirt sizes (7 ≤ X ≤ 100), with the first T-shirt size mentioned as the ‘most preferred
one’, some example scenarios:
• a coach (a father) prefers ‘XL’, but he is still happy to get ‘XS’ (which is FOUR sizes
smaller), because he actually has a young daughter whose t-shirt size is ‘XS’ and will
give the small-sized shirt for her,
• a contestant prefers ‘M’, but she is happy to get ‘XXXL’ or ‘XXL’ (4 or 3 sizes larger)
because she has a (rather big-sized) coach back home who collects contest t-shirts,
• a contestant can accept any t-shirt size, i.e., he is happy with any of the X available
t-shirt sizes (for memorabilia only, not to be worn), but because he has to nominate
one of the most preferred one, he put ‘XL’,
• a coach does NOT want to collect t-shirt, as he has gone through so many contests
and had too many t-shirts at home,
• a peculiar contestant prefers ‘L’ and will throw tantrum if given anything other than
‘L’, etc
For bonus 1 mark, show just one counter example that the greedy algorithm developed in
question 1-4 above cannot solve the generalized version.

> Counter Example: if a contestant who prefer 'XL' but is okay with any size occurs. My algorithm
> in the earlier parts will try to assign XL / XXL / L as much as possible (which may be taking
> shirts that could be given to other) example shown below 
> 0 0 1 0 0 0 1 (1 XL, 1 XS in supply)
> 2 
> XL (can be any size), XL 
> the algorithm i proposed will assign XL to the first customer (even tho he can/ and should take
> the XS). leaving no shirts for the other contestant to take. 

6. For another bonus 1 mark, solve the generalized version and analyze the time-complexity
in Big O notation.
Hint: You probably need an algorithm that is ‘out of syllabus’ for CS3230 S1 AY24/25...
Question 2: Binary Counter (4 × 5 = 20 marks)
Recall that a binary counter works as follows.
• Start with the number zero.
• In each step, the number is increased by one. The cost of an increment is defined by the
number of bits flipped in the binary representation.
In the class, we show that the amortized cost of each step (performed across n steps) is Θ(1),
despite that the worst-case cost of a step is Θ(log n).
Now consider two modifications to the problem.

### Modification 1: higher flexibility. In each step, the amount of increase can be any number
in {1, 2, 4, 8, 16, . . .}. For example,
· · · 00011001 +26 −→ cost=1 · · · 01011001 +23 −→ cost=3 · · · 01100001 +20 −→ cost=2 · · · 01100010.

### Modification 2: higher cost. The cost of an increment becomes x3, where x is the number
of bits flipped in the binary representation. For example,
· · · 00011001 +26 −→ cost=13=1 · · · 01011001 +23 −→ cost=33=27 · · · 01100001 +20 −→ cost=23=8 · · · 01100010.

1. Show that the amortized cost for n steps is still O(1) with Modification 1 only.
* All the bits start at 0 (given in the question)
* we define two types of actions:
    * flip bit to 1 
    * flip bit to 0 
* every increment will be a combination of those two actions
* we assign 2$ to flip bit to 1, 1$ for the actual cost of flipping 0 -> 1 
  the other 1$ is for the potential to flip it back to 0 (similar to the queue in tutorial)
* since we start at 0: the number of "flip bit to 1" >= "flip bit to 0" as you can flip a 0 -> 0 
* this mean we will always have "savings" will never be less than 0 
* amortized cost O(1)

2. Show that the amortized cost for n steps is still O(1) with Modification 2 only.

3. Show that the amortized cost for n steps is O(n2) with both Modifications 1 and 2.

4. In the setting where both Modifications 1 and 2 are applied, for every positive integer n,
demonstrate a sequence of n increments Sn such that f (n) ∈ Ω(n2), where f (n) is the
amortized cost for Sn.
