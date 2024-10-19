def int_inputs(): return map(int, input().strip().split())

x, y = int_inputs()

print("Multiples") if (x % y) == 0 or (y % x ) == 0 else print("No Multiples")
