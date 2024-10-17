def int_inputs(): return map(int, input().strip().split())
x,y = int_inputs()

num1 = x % 10
num2 = y % 10

print(num1+num2)