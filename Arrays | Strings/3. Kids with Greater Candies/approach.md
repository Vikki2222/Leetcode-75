# Problem Definition

**Difficulty:** `Easy`

There are n kids with candies. You are given an integer array candies, where each candies[i] represents the number of candies the ith kid has, and an integer extraCandies, denoting the number of extra candies that you have.

Return a boolean array result of length n, where result[i] is true if, after giving the ith kid all the extraCandies, they will have the greatest number of candies among all the kids, or false otherwise.

Note that multiple kids can have the greatest number of candies.

 

Example 1:

```
Input: candies = [2,3,5,1,3], extraCandies = 3
Output: [true,true,true,false,true] 
Explanation: If you give all extraCandies to:
- Kid 1, they will have 2 + 3 = 5 candies, which is the greatest among the kids.
- Kid 2, they will have 3 + 3 = 6 candies, which is the greatest among the kids.
- Kid 3, they will have 5 + 3 = 8 candies, which is the greatest among the kids.
- Kid 4, they will have 1 + 3 = 4 candies, which is not the greatest among the kids.
- Kid 5, they will have 3 + 3 = 6 candies, which is the greatest among the kids.
```

Example 2:

```
Input: candies = [4,2,1,1,2], extraCandies = 1
Output: [true,false,false,false,false] 
Explanation: There is only 1 extra candy.
Kid 1 will always have the greatest number of candies, even if a different kid is given the extra candy.
```

Example 3:

```
Input: candies = [12,1,12], extraCandies = 10
Output: [true,false,true]
```

# Approach

Since we need to find if after adding the extra candies the number of candies of the current kid is greater than or equal to the highest number of candies among the kids, we need to find the maximum number of candies

Now, we need to iterate through the candies array and check if after adding extra candies they are greater than or equal to the max.

# Psuedo Code

```
maxCandy = MAX(candies)

result = []

FOR candy in candies
    IF candy + extraCandies >= maxCandy then
        result.append(TRUE)
    ELSE
        result.append(FALSE)

return result
```

# Code

**Time Complexity:** O(N)

**Space Complexity:** O(N)