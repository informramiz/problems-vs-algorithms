## Problem 5: Autocomplete with Tries

### Reasoning
Given a node we have to find all the children of this nodes that are complete words and return them. So I go through each children of the node while keep tracking of the word made till this depth, check if any children is a complete word and if it is I add it to the words list. I do this recursively for child node to check their children and then their child and so on.

### Time Effficiency
Let's say M is the maximum length suffix (max depth of trie) and N is the maximum number of child nodes any node has then M will define the maximum depth of our recursion call tree and N will define the maximum width of any call so total run time is **O(M x N)**

### Space Efficiency
Let's say M is maximum depth of the Node so M is the depth of the call stack and in each call we store at max (let's say) N words then the total space cost is **O(M x N)**