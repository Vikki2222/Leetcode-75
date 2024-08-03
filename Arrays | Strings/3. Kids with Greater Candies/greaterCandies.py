from typing import List

def greaterCandies(candies: List[int], extraCandies: int) -> List[bool]:
    # NOTE: I tried finding the max values and the comparison in the traditional way but it was taking too long to run.
    # NOTE: So, I used the max function to find the max value in the list and then compared the values in the list with the max value in a single line.
    maxCandy = max(candies)
    return [candy + extraCandies >= maxCandy for candy in candies]