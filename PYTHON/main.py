import renderMenu
import time

array = []

print("Ingrese longitud del array")

size = int(input())


for i in range (size):
    array.append(i)
    print(i)
    time.sleep(0.5) #in seconds


print(array)


find = 0

while(True):
    print("Seleccione numero a buscar")

    find = int(input())

    if(find == -1):
        break

    if (find in array ):
        print ("Found")
    else:
        print("Not Found")


print("End of game -Tx for playing")

