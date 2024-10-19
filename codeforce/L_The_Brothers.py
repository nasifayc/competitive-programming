def str_inputs(): return input().strip().split()

f1,s1 = str_inputs()
f2,s2 = str_inputs()

print("ARE Brothers") if s1 == s2 else print("NOT")