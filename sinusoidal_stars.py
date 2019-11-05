width = int(input("Genişlik değerini girin : "))
height = int(input("Yükseklik değerini girin : "))

pos = 0
direction = -1

for i in range(height):
    if (i + width) % width == 0:
        direction *= -1
    
    pos += direction
    
    for j in range(width):
        if (j + 1) % (pos + 1) == 0:
            print("*", end="")
            break
            
        print(" ", end="")
            
    print("")
