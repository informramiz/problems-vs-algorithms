## Problem 3: Rearrange Array Elements

### Reasoning
To maximize both numbers we need to make sure their most significant number is largest possible, then their next significant number and so on. To do that I first sorted the array using heap sort (because O(nlog(n))) and then alternatively pick numbers for each number in way that the largest possible numbers are most significant, the next largest are next significant and so on.

### Time Efficiency
I have used heap sort which has a run time of O(nlog(n), then I traverse the array 2 times, one to pick first number, second to pick 2nd number, each with run time O(n). so total
O(nlog(n)) + O(n) + O(n) = O(nlog(n))

### Space Efficiency
As other than storing 3 variables I don't store anything and heap sort is in-place algorithm so my space efficiency is **O(1)**