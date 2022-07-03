arr1 = [8, 3, 15, 6, 4, 2]
arr2 = []
for el in range(len(arr1)):
    if arr1[el] % 2 == 0:
        arr2.append(el)
print(arr2)