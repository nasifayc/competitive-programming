#brute force - Time and Space O(2 ^ (n+m))

def bruteForce(r,c,rows,cols):
    if r == rows or c == cols:
        return 0
    if r == rows - 1 and c == cols-1:
        return 1
    return (bruteForce(r+1,c,rows,cols) + bruteForce(r+1,c,rows,cols))

#Memoization - Time and Space O(n*m)

def memo(r,c,rows,cols, cache):
    if r == rows or c == cols:
        return 0
    if cache[r][c] > 0:
        return cache[r][c]
    if r == rows - 1 and c == cols-1:
        return 1
    cache[r][c] = memo(r+1,c,rows,cols,cache) + memo(r,c+1,rows,cols,cache)
    
    return cache[r][c]
    
    
    