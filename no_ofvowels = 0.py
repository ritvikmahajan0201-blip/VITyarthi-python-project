def find_divisibles(myList, num):
    divisibles = []
    for i in myList:
        if i % num == 0:
            divisibles.append(i)
            
    return divisibles

myList = [8, 14, 21, 36, 43, 57, 63, 71, 83, 93]
num = 3
print(find_divisibles(myList, num))




