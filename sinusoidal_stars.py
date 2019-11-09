width = int(input("Genişlik değerini girin : "))
height = int(input("Yükseklik değerini girin : "))

pos = 1
direction = 1

for i in range(1, height + 1):  
    for j in range(1, width + 1):
        if j % pos == 0:
            print("*")
            
            print("j , width", j , width)
            if j % width == 0:
                direction *= -1
            
            pos += direction
            
            break
        else:
            print(" ", end="") 
