def int_inputs(): return map(int, input().strip().split())
a,b,c,d = int_inputs()

result = (a*b) - (c*d)

print(f"Difference = {result}")