import time

array = []

print("Ingrese longitud del array")

size = int(input())


for i in range (size):
    array.append(i)
    print(i)
    time.sleep(0.5) #in seconds


print(array)

array.sort()

find = 0

while(find != -1):
    print("Seleccione numero a buscar")

    find = int(input())

    if(find == -1):
        break

    if (find < size ):
        print ("Found")
    else:
        print("Not Found")


print("End of game -Tx for playing")