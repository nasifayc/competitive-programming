import math


def int_inputs(): return map(int, input().strip().split())
def custom_round(number):
    decimal_part = number - int(number)  
    if decimal_part >= 0.5:
        return math.ceil(number) 
    else:
        return math.floor(number)

x,y = int_inputs()

print(f"floor {x} / {y} = {math.floor(x/y)}")
print(f"ceil {x} / {y} = {math.ceil(x/y)}")


re = x / y
r = custom_round(re)
print(f"round {x} / {y} = {r}")