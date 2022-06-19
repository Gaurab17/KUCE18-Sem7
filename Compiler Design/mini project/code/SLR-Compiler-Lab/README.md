# SLR-Parser

G:

```sh
E -> E + T | T
T -> T F | F
F -> F * | a | b
```

The input to the program is a given context-free grammar and a string(your choice). Outputs reverse of the
right most derivation of the string from the given grammar.\
a. Computation of LR (0) Sets of Items.\
b. Computation of SLR parsing table.\
c. Simulation of SLR parser on the given string.

#### Grammar File

A text file containing the grammar is required. For example, the contents of a grammar file `grammar.txt` looks like this

```sh
E -> E + T | T
T -> T F | F
F -> F * | a | b
```

### Get Started

```sh
$ python main.py

Grammar
 E -> E + T | T
 T -> T F | F
 F -> F * | a | b

Augmented Grammar
 E' -> E
 E -> E + T
 E -> T
 T -> T F
 T -> F
 F -> F *
 F -> a
 F -> b

Terminals   : ['+', '*', 'a', 'b']
Nonterminals: ["E'", 'E', 'T', 'F']
Symbols     : ["E'", 'E', 'T', 'F', '+', '*', 'a', 'b']

First
 E' = { a ,  b }
 E = { a ,  b }
 T = { a ,  b }
 F = { a ,  b }

Follow
 E' = { $ }
 E = { $ ,  + }
 T = { $ ,  + ,  a ,  b }
 F = { $ ,  + ,  a ,  b ,  * }

Items
I0:
 E' -> . E
 E -> . E + T
 E -> . T
 T -> . T F
 T -> . F
 F -> . F *
 F -> . a
 F -> . b
I1:
 E' -> E .
 E -> E . + T
I2:
 E -> T .
 T -> T . F
 F -> . F *
 F -> . a
 F -> . b
I3:
 T -> F .
 F -> F . *
I4:
 F -> a .
I5:
 F -> b .
I6:
 E -> E + . T
 T -> . T F
 T -> . F
 F -> . F *
 F -> . a
 F -> . b
I7:
 T -> T F .
 F -> F . *
I8:
 F -> F * .
I9:
 E -> E + T .
 T -> T . F
 F -> . F *
 F -> . a
 F -> . b

Parsing Table
+--------+--------+--------+--------+--------+--------+--------+--------+--------+
| State  |    +   |    *   |    a   |    b   |    $   |    E   |    T   |    F   |
+--------+--------+--------+--------+--------+--------+--------+--------+--------+
|   0    |        |        |   s4   |   s5   |        |    1   |    2   |    3   |
|   1    |   s6   |        |        |        |   acc  |        |        |        |
|   2    |   r2   |        |   s4   |   s5   |   r2   |        |        |    7   |
|   3    |   r4   |   s8   |   r4   |   r4   |   r4   |        |        |        |
|   4    |   r6   |   r6   |   r6   |   r6   |   r6   |        |        |        |
|   5    |   r7   |   r7   |   r7   |   r7   |   r7   |        |        |        |
|   6    |        |        |   s4   |   s5   |        |        |    9   |    3   |
|   7    |   r3   |   s8   |   r3   |   r3   |   r3   |        |        |        |
|   8    |   r5   |   r5   |   r5   |   r5   |   r5   |        |        |        |
|   9    |   r1   |        |   s4   |   s5   |   r1   |        |        |    7   |
+--------+--------+--------+--------+--------+--------+--------+--------+--------+


Enter Input String(Whitespaces is required in between lexemes): a + b * a

+--------+----------------------------+----------------------------+----------------------------+
|  Step  |           Stack            |           Input            |           Action           |
+--------+----------------------------+----------------------------+----------------------------+
|   1    | 0                          |                     a+b*a$ |              s4            |
|   2    | 0a4                        |                      +b*a$ |              r6            |
|   3    | 0F3                        |                      +b*a$ |              r4            |
|   4    | 0T2                        |                      +b*a$ |              r2            |
|   5    | 0E1                        |                      +b*a$ |              s6            |
|   6    | 0E1+6                      |                       b*a$ |              s5            |
|   7    | 0E1+6b5                    |                        *a$ |              r7            |
|   8    | 0E1+6F3                    |                        *a$ |              s8            |
|   9    | 0E1+6F3*8                  |                         a$ |              r5            |
|   10   | 0E1+6F3                    |                         a$ |              r4            |
|   11   | 0E1+6T9                    |                         a$ |              s4            |
|   12   | 0E1+6T9a4                  |                          $ |              r6            |
|   13   | 0E1+6T9F7                  |                          $ |              r3            |
|   14   | 0E1+6T9                    |                          $ |              r1            |
|   15   | 0E1                        |                          $ |           Accepted         |
+--------+----------------------------+----------------------------+----------------------------+
```
