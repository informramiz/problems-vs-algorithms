## Square Root Problem

### Reasoning
Square root of a number is: a value that can be multiplied by itself to give the given number. Square root of 0 is 0 and 1 is 1. For other numbers, sqrt(n) will always be between [2, n/2] so do a simple binary 
search to find the square root. 

### Time Efficiency 
As binary search is log(n) so my solution using binary search will cost **log(n)** as required.

### Space Efficiency
My solution don't store anything other than 3 variables so space efficiency is **O(1)**