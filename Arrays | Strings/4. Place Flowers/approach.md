# Problem Definition

**Difficulty:** `Easy`

You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

 

Example 1:

```
Input: flowerbed = [1,0,0,0,1], n = 1
Output: true
```

Example 2:

```
Input: flowerbed = [1,0,0,0,1], n = 2
Output: false
```

A lot of edge cases, honestly this is a easy question but a pain in the a**.

# Approach

The approach is simple, i.e if the previous and ahead spaces are not planted then we can plant in the current space.

There can be a edge case when the first element and last element are involved since they don't have previous and next respectively.

My approach to that was to have a bunch of if-else statements which made the code longer but I found a simpler code. I'm going to write the pseudo code for both below.

# Pseudo Code

### My Approach

```
IF length(flowerbed) == 1 then
    IF n == 0 then return True
    ELSE IF flowerbed[0] == 0 and n == 1 then return True
    ELSE return False

    count = 0
    length = length(flowerbed)

    IF flowerbed[0] == 0 and flowerbed[1] == 0 then
        flowerbed[0] = 1
        count += 1
    
    IF flowerbed[length-1] == 0 and flowerbed[length-2] == 0 then
        flowerbed[length-1] = 1
        count += 1
    
    i = 1
    WHILE i < length-1 
        IF flowerbed[i] == 0 then
            IF flowerbed[i+1] == 0 and flowerbed[i-1] == 0 then
                flowerbed[i] = 1
                count += 1
        i += 1
    
    return count >= n
```

### Optimal Approach

```
count = 0
flowerbed = [0] + flowerbed + [0] 

FOR i in range(1, length(flowerbed) - 1)
    IF flowerbed[i] == 0 and flowerbed[i-1] == 0 and flowerbed[i+1] == 0 then 
        flowerbed[i] = 1
        count += 1

return count >= n
```

# Code

**Time Complexity:** O(N)

**Space Complexity:** O(1)