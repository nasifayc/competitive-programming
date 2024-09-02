def find_working_buttons(s):
    working_buttons = set()
    i = 0
    while i < len(s):
        if i < len(s) - 1 and s[i] == s[i + 1]:  
            i += 2  
        else:
            working_buttons.add(s[i])  
            i += 1
    
    return ''.join(sorted(working_buttons))


t = int(input())  
for _ in range(t):
    s = input().strip()
    print(find_working_buttons(s))
