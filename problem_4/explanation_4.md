## Problem 4: Dutch National Flag Problem

### Reasoning
The idea is that If we put 0s and 2s in correct positions the 1s will be automatically put in correct positions so we keep track of next index for 0 (index\_index\_0), and next index for 2 (next\_index\_2) and these indexes are only incremented when either a zero is encountered and put in right position or a 2. 

Meanwhile front\_index keep tracks of the next number to be checked to see if it is in correct position or not. If it is 0 then it should go to next\_index\_0 and if it is 2 then it should go to next\_index\_2, if it is 1 then it is in the right position. This way when front\_index reaches the next\_index\_2 the array will be sorted.

### Time Efficiency
The whole process happens in a single traversal of array so time efficiency is **O(n)**.


### Space Efficiency
As other than storing 3 variables I don't store anything and heap sort is in-place algorithm so my space efficiency is **O(1)**
