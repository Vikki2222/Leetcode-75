def mergeAlternative(word1: str, word2: str) -> str:
    n = len(word1)
    m = len(word2)
    i = 0
    merged = ''
    
    while i < n and i < m:
        merged += word1[i] + word2[i]
        i += 1
        
    if n > m:
        merged += word1[i: ]
    else:
        merged += word2[i: ]
    
    return merged