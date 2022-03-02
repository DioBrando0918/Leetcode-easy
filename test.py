# a = [1, 3, 2, 2, 4]
#
# print(len((set(a))))

lst = [0, 1, 2, 2, 3, 0, 4, 2]
length = len(lst)
x = 0
while x < length:
    if lst[x] == 2:
        lst.remove(2)
        length -= 1
        x -= 1
    x += 1

print(lst)
