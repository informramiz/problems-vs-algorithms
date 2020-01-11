## Problem 7: HTTPRouter using a Trie

### Reasoning
All the required logic is already given in the problem itself and all I did was follow it so there is nothing special that I have done that require any reasoning.

### Time Efficiency
#### RouteTrie
- **insert:** Usually it is O(lgn) but in RouteTrie it is different because each child is based on a word and not a character. Let's say m is the maximum length of any path then it is `O(mlog(n))` because for each children we are comparing the path value.
- **find:** The logic for find is same as insert so same run time, `O(mlog(n))`.

#### Router
- **split_path:** This is a O(n) as it uses built-in split and then filter and both are O(n).
- **Insert:** It involves spliting the path into parts (O(n)) then inserting the handler into the Trie (O(Mlog(n)). So total = `O(n) + O(mlog(n)) => O(mlog(n))`
- **Lookup:** The logic of look_up method is same as insert so same run time, `O(mlog(n))`.


### Space Efficiency
The space required is the one used by `RouteTrie`. If `W` is width of the Trie and `H` is height of the Trie then space used is `O(W*H)`.  