def can_reduce_to_k(n, k, a):
    total_sum = sum(a)
    
    if (total_sum - k) % (n - 1) != 0:
        return "NO"
    
    
    x_total = (total_sum - k) // (n - 1)
    
    
    if min(a) <= x_total <= max(a):
        return "YES"
    else:
        return "NO"

t = int(input())  
results = []
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    results.append(can_reduce_to_k(n, k, a))

print("\n".join(results))
