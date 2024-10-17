
def int_inputs(): return map(int, input().strip().split())

x, y = int_inputs()
print("Yes") if x >= y else print("No")