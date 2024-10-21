x = int(input())

while x >= 10:
    x = x // 10

print("EVEN") if x % 2 == 0 else print("ODD")