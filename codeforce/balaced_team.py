def max_balanced_team_size(n, skills):
    
    skills.sort()
    
    max_size = 0
    left = 0
    
    for right in range(n):
        
        while skills[right] - skills[left] > 5:
            left += 1
        
        
        max_size = max(max_size, right - left + 1)
    
    return max_size


n = int(input())
skills = list(map(int, input().split()))


print(max_balanced_team_size(n, skills))
