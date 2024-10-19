def int_inputs(): return map(int, input().strip().split())

x,y,z = int_inputs()

s = min(x,y,z)
l = max(x,y,z)

print(s,l)