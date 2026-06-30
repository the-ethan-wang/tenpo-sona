# random tetris info problem

Given an array of intergers `a` of length `n`, output the shortest sequence of instructions required to position a 1x1 square into the column of the valley enclosing the deepest hole. Two positions `i` and `j` where 1<=`i`<=`j`<=`n` are defined as within the same valley if there exists at most 1 index `p` where `i`<=`p`<=`j` such that the sequence `a_i`, `a_{i+1}`, ..., `a_{p}` is nonincreasing and the sequence `a_p`, `a_{p+1}`, ..., `a_j` is nondecreasing. If many holes are the deepest, any will do. If many such sequences exist, any will do. The 1x1 square starts at position `k` (1 <= `k` <= n). It is given that 1 <= `n` <= 1e6 and -1e8 <= `a_i` <= 1e8 for all 1 <= `i` <= `n`.

Note: the block must remain within the bound 1 <= position <= n throughout the sequence

Valid instructions:
- < - move the block 1 unit left
- > - move the block 1 unit right
- !< - move the block to index 1
- !> - move the block to index n

Input:
```
n k
a_1, a_2, a_3, ..., a_n
```

Output: output the sequence separated by newlines.

## Sample cases

Input
```
5 3
-9 7 1 0 1
```

Output
```
!<
```

Explanation  
!< moves the block to index 1, which is in the same valley as the deepest hole (at index 1)

