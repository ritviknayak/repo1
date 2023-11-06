import math

list1 = [432, 331, 192, 108, 180, 50, 231, 188, 105, 51, 364, 168, 344, 195, 297, 342, 292, 198, 448, 62, 236, 342, 63]

m = 41
list2 = []

for i in range(len(list1)):
    inverse = pow(list1[i],-1,41)
    list2.append(inverse)

s = ""
for i in range(len(list2)):
    if 1 <= list2[i] <= 26:
        s += chr(ord('A') + list2[i] - 1)
    elif 27 <= list2[i] <= 36:
        s += chr(ord('0') + (list2[i] - 27))
    elif list2[i] == 37:
        s += '_'

print("Decrypted Message:", "picoCTF{" + s + "}")
