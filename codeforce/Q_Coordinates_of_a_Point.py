def int_inputs(): return map(float, input().strip().split())

x,y = int_inputs()



if x == 0 and y == 0:
    print("Origem")
elif x > 0 and y > 0:
    print("Q1")

elif x < 0 and y > 0:
    print("Q2")

elif x < 0 and y < 0:
    print("Q3")

elif x > 0 and y < 0:
    print("Q4")
elif  y != 0:
    print("Eixo Y")
elif x != 0 :
    print("Eixo X")
