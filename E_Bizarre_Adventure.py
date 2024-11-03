def max_area_of_ones(t, test_cases):
    results = []
    for s in test_cases:
        n = len(s)
        height = [0] * n
        max_area = 0
        
        for k in range(n):
            for j in range(n):
                if s[(j - k) % n] == '1':
                    height[j] += 1
                else:
                    height[j] = 0
            
            max_area = max(max_area, largest_rectangle_area(height))
        
        results.append(max_area)
    
    return results

def largest_rectangle_area(heights):
    heights.append(0)  
    stack = []
    max_area = 0
    
    for i in range(len(heights)):
        while stack and heights[stack[-1]] > heights[i]:
            h = heights[stack.pop()]
            w = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, h * w)
        stack.append(i)
    
    return max_area


t = int(input())
test_cases = [input().strip() for _ in range(t)]

results = max_area_of_ones(t, test_cases)

for result in results:
    print(result)
