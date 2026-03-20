## 25.2 Gift Shop

Inputs parsed with standard string manipulation(split,etc.), break the problem down into a few parts

One tiny obstacle along the way was some mix-up between slicing the strings into how many pieces and a typo that led me to write n instead of len(n), making me think time complexity O(n^3) is already too much to handle...

---
## 25.3 Lobby

In this challenge I compared the chars directly as they are comparable, but then always I keep in mind they need to be converted in the end. Initially tried two pointer to solve but missing a lot of edge cases(and I still don't know if two pointer will work...), thank you brute-force! Caught my attention when debugging that it is very important to add the equal sign when comparing the digits, as it must updates to the frontest element!

---
## 25.4 Printing Department
Thought process:   
Process the input and put them into a list, would be of length L * height H, L is length of each string, H would be the length of the list, traverse through the list

Edge cases include:
1. the corner: all paper rolls there are automatically accessible
2. on edges: up/down/left/right-most

Very brute force. Edge cases literally contain the edges. Tried to optimize with the branching as there were quite a lot of repetitions with regard to counting paper rolls(but failed). Gon think about that later. Since strings are not mutable next time would consider already in P1 to put it in list.    
Definitely need to optimize the code in the future(now it looks quite ugly...). 


