low = 0
hight = 999
counter = 0
while counter < 10:
    x = input()
    x =int(x)
    i = (low+hight)/2
    if i == x:
        print("correct")
        break
    elif i < x:
        low = i +1
        print("lower")
        counter+1
    elif i > x:
        hight = i-1
        print("higher")
        counter+1