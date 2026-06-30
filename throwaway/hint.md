# Hint

It is important that a solution program is aware that just because many indexes may be the lowest, but some may be more accessible than others. A breaking case for a "naive" program may be

```
5 5
1 0 1 0 1
```

wherein the naive program stores the lowest index only (as "2")

then calculates the minimum number of instructions to be 2 (!< >)

Thus ignores the fact that cell at index 4 is also a minimum, there exists a sequence of instructions (<) that reaches a minimum valley in just one instruction. Thus, the naive program fails.