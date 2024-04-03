Dor = 0
for i in range(1, 101):
    if i % 3 == 0:
        print("DOR", end=" ")
        Dor += 1
    elif i % 5 == 0:
        print("DOR", end=" ")
        Dor += 1 
    elif i % 10 == 0:
        print("DOR",end=" ")   
    else:
        print(i, end=" ")
    if i % 10 == 0:
        print ()     
        
print("\nTotal DOR yang muncul sebanyak =" ,Dor)
    