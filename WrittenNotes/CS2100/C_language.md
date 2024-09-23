# C Deez Nuts in your mouth
This md file is for anything C related and is in no way a proper notes. Its more like random shit I found interesting to note while coding in C.

### Data types
```c
#include <stdio.h>

int main (void) {
    printf("Size of 'int' (in bytes): %d\n", sizeof(int));
    printf("Size of 'float' (in bytes): %d\n", sizeof(float));
    printf("Size of 'double' (in bytes): %d\n", sizeof(double));
    printf("Size of 'char' (in bytes): %d\n", sizeof(char));

    return 0;
}
```

| DataType   | Memory    |
|--------------- | --------------- |
| int   | 4   |
| float   | 4   |
| double   | 8   |
| char  | 1   |

### Gcc flags
* -o: names the output file
* -Wall: option turns on all warnings
* -D<text>: compile with <text> as a macro

### I/O format specifiers
| placeholder | type | function use | 
| - | - | - |
| %c | char | printf/ scanf | 
| %d | int | printf/ scanf | 
| %f | float or double | printf |
| %f | float | scanf | 
| %lf | double | scanf | 
| %e | float or double | printf(scientific notation) | 
| %p | pointers | printf/ scanf | 
| %s | string | printf/ scanf/ fgets | 

### I/O escape sequences
| escape sequence | action | 
| - | - |
| \n | new line | 
| \t | horizontal tab | 
| \" | double quote | 
| %% | percent | 
| \r | carraige return |
| \0 | null deliminator | 


### Bitwise opertaions
| operator | description | 
| - | - |
| & | bitwise AND | 
| \| | bitwise OR | 
| ^ | bitwise XOR | 
| ~ | btiwise NOT | 
| << | left shift | 
| >> | right shift | 

### Pointer :(
* int *p: means pointer called p that point to some int
* &i: address value of variable i  
* *p = i: reassign the variable p was pointing to to i 
* p = &j: reassign the pointer p to new address of j (now points to j) 

> [!NOTE]
> Funny thing about pointer and arrays
> arr[0], *arr: both returns element at index 0
> arr, &arr: address of the first element

### Arrays and Strings
```c
#define N 10
int source[N] = {1,2,3,4,5};
int dest[N];
dest = source; //ILLEGAL!!
```
> [!CAUTION]
> You cannot do this as **An Array name is a fixed constant pointer** and cannot be reassigned

```c
char *str1 = "罗睺is my wife";
str2 = "瑟琳is my wife";
str1[0] = 'h'; //Allowed
str2[0] = 'h'; //ILLEGAL!!
```
> [!CAUTION]
> Similar to how you cannot reassign an arr name, **String literals are immutable**, remember
> string in c are just char arrays ending with '\0', declaring it as a literal makes it constant

### Structures
```c
typedef struct {
    int length, width, height;
} name_t;

typedef struct {
    int uId;
    float IEEE;
    name_t nestedName;
} user_t;

user_t user1 = {9, 1.2, {10, 10, 20}};
user1.IEEE = 1.4; //reassign value of IEEE
printf("%d\n", user1.nestedName.height); //prints 20
```

> [!NOTE]
> we can pass addresses of structure to function by doing foo(&struck)
> in a function as we receive the pointer <br>
> foo(struck_t *struck_ptr) <br>
> strcpy((*struck_ptr).waifi, "罗睺is my wife") <br>
> *can be shorten to struck->waifu* 
