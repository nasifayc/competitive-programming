n = int(input())

y,m, = 0,0

while n >= 365:
    n -= 365
    y += 1

while n >= 30:
    n -= 30
    m += 1

print(f'{y} years')
print(f'{m} months')
print(f'{n} days')
