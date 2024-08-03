# Problem Definition

Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

 

Example 1:

```
Input: s = "hello"
Output: "holle"
```

Example 2:

```
Input: s = "leetcode"
Output: "leotcede"
```

# Approach

We have to reverse just the vowels in the string, therefore we can use `2-pointer approach`.

We can have one pointer at the start and the other at the end of the array. The left pointer will increase and right pointer will decrease till both find a vowel. At this point we must swap them. 

Since srings are immutable we must first convert the string to a list of characters.

# Pseudo Code

### Brute Force

```
vowels = []

FOR ch in s
    IF ch is vowel then
        vowels.append(ch)

j = length(vowels) - 1
new = ""

FOR ch in s
    IF ch is vowel then
        new = new + vowels[j]
        j -= 1
    ELSE
        new = new + ch

return new
```

### Optimal

```
s = list(s)
left = 0
right = length(s) - 1

WHILE left < right
    IF s[left] is vowel and s[right] is vowel then
        SWAP(s[left], s[right])
        left += 1
        right -= 1
    IF s[left] is not vowel then
        left += 1
    IF s[right] is not vowel then
        right -= 1

return ''.join(s)
```

# Code

**Time Complexity:** O(N)

**Space Complexity:** O(N)