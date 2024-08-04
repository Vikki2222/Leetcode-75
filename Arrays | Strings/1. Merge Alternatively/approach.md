# Problem Definition

**Difficulty:** `Easy`

You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.

 

Example 1:

```
Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r
```

Example 2:

```
Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"
Explanation: Notice that as word2 is longer, "rs" is appended to the end.
word1:  a   b 
word2:    p   q   r   s
merged: a p b q   r   s
```

```
Example 3:

Input: word1 = "abcd", word2 = "pq"
Output: "apbqcd"
Explanation: Notice that as word1 is longer, "cd" is appended to the end.
word1:  a   b   c   d
word2:    p   q 
merged: a p b q c   d
```

# Approach

It is a very simple problem, we need to iterate while concatenating each character alternatively from both strings until one of the strings or both are exhausted.

After this we can check the string which is longer and concatenate the remaining characters by using the index that came out of the above loop.


# Pseudo Code

```
N = word1 length
M = word2 length
i = 0
MERGED = ''

WHILE i < N and i < M 
    MERGED = MERGED + word1[i] + word2[i]
    INCREMENT i

IF N > M then
    MERGED = MERGED + word1[i to end]
ELSE 
    MERGED = MERGED + WPRD2[I TO end]

return MERGED
```

# Code

**Time Complexity**: O(N)

**Space Complexity**: O(N + M)
