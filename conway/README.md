# Conway's game of life

## Links

carykh video "The Conway Multiverse" https://www.youtube.com/watch?v=QK_KZv-YyOc

Zipf's law https://en.wikipedia.org/wiki/Zipf%27s_law

The Zipf Mystery https://www.youtube.com/watch?v=fCn8zs912OE

Processing 4 https://processing.org/

cellular automata that mirrors B37/S1234 "mice in corridors" devinacker.github.io/celldemo rule 18 (sierpinski triangle if started from 1 cell)

## Notes

Rulestrings in the notation B{α}/S{β}

alpha is a set of numbers which can include 0-8 inclusive, number of adj living cells to a dead cell that allows a birth

beta is similar, but its the number of adj living cells which allow a preexisting living cell to continue living

thus, rulestring can be stored as an 18 bit bitmask (and thus unique 2^18 rulestrings)

Cary only analyses connected rulestrings (continuous, thus at most 1 switch)

also, non-square tilemaps could be interesting e.g. hexagon or triangle maps and the set could be 0-6 or 0-3 depending on the tiles and tessellation

further explore B36/S23 "HighLife" and B3678/S34678 "Day and Night"

B345678/S2345678 is so funny

## Cool/program

implement

B3/S12345 and B3/1234 for cool maze

B34/S23 (A World on Fire)

data analysis for "Life Without Death" B3/S0123456789 - Famous Ladder

growth analysis

---

Bo Burnham - A World on fire https://www.youtube.com/watch?v=1ws33f6qys4