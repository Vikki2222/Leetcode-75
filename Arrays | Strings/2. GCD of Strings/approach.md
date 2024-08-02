# Problem Definition

For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

 

Example 1:

```
Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"
Example 2:
```

```
Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"
Example 3:
```

```
Input: str1 = "LEET", str2 = "CODE"
Output: ""
```

# Approach

If str1 + str2 not same as str2 + str1 we can say that these strings don't have a GCD. Let's take an example:

```
str1 = 'ABCDEF'
str2 = 'ABC'
str1 and str2 don't have a GCD

ABCDEFABC != ABCABCDEF
```

We can take this mathematically by taking the lengths of both strings. If you notice the len(GCD) of the strings is equal to `GCD(len(str1), len(str2))`. Let's take an example:

```
str1 = 'ABABAB'
str2 = 'AB'
GCD = 'AB'

GCD(6, 2) = 2 which is length of GCD of the strings.
```

> NOTE:
> You can either use the math library to calculate GCD or you can whip up your own function that calculates the GCD.

# Pseudo Code

### My Approach

I identified the gcd of lengths part but didn't figure out the other part

```
IF str1[0] not equal to str2[0] then return ''

IF str1 equal to str2 then return str1

gcdLen = 0
n = length(str1)
m = length(str2)
i = 0

WHILE i < n and i < m
    IF str1[i] equal to str2[i] then
        IF n mod (i+1) equal to 0 and m mod (i+1) equal to 0 then
            gcdLen = i + 1
    ELSE
        return ''
    i = i + 1

gcd = str1[: gcdLen]
length = n IF n > m ELSE m
num = length // gcdLen
IF n > m and num * gcd != str1 then
    return ''
ELSE IF m > n and num * gcd != str2 then
    return ''

return gcd
```

### Optimal Approach

```
GCD(x, y)
    WHILE x > 0 and y > 0
        IF x > y then x = x % y
        IF y > x then y = y % x
    return x IF y == 0 ELSE y

IF str1 + str2 == str2 + str1 then 
    return ''

gcdLen = GCD(length(str1), length(st2))
return str1[: gcdLen]
```


# Code

**Time Complexity:** O(M + N)

**Space Complexity:** O(M + N)

