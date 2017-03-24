
# [Register Machines] Godel's Numberings program decoder

Register Machines came in  the mid '50s as an alternative model of computation to Turing Machines.
They operate on natural numbers, stored in (finitely many) register R0 ... Rn.
A program takes the form of a finite list of instructions `<label>: <body>` where each body can be one of the following:
1. Rn+ => Li: add 1 to the content of Rn and jump to instruction Li;
2. Rn- => Li, Lj: if the content of Rn is > 0, subtract 1 and jump to Li, else jump to Lj (branch instruction);
3. HALT: stop the execution. 
Via Godel's numberings, it is possible to encode each instruction in a number and the so-obtained list of numbers
in a single one, representing the given program.

This script is meant to be a support tool for the Register Machines section in the Models Of Computation module 
@Imperial College London, Computing.
Simply run `python decode.py <program encoding>` to obtain the full program expansion.

## Example

The natural number 2<sup>46</sup> x 20483 can represent the encoding of a program.
Calling `decode.py` on the encoding gives back the following:
```
L0: R0- => L2, L1
L1: HALT
L2: R0- => L0, L1
L3: R0+ => L0
```

