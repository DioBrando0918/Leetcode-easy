# def fact(n):
#     if n == 0 or n == 1:
#         return 1  # 會return 1 給line18 就會變成n*1而不是繼續遞迴
#     # return 2 的話會變成48
#     # return 3的話會變成72
#
#     else:
#         return fact(n - 1)
#
#
# print(fact(4))  # 24

# print(7//2)
# ans = ['a', 'm', 'a', 'n', 'a', 'p', 'l', 'a', 'n', 'a', 'c', 'a', 'n', 'a', 'l', 'p', 'a', 'n', 'a', 'm', 'a']
# ans = "".join(ans)
# print(ans)
#
# A, B = 10, 20
# print(A ^ B)
# print(4 ^ 8)
#
# lst = [[i] for i in range(5)]
# print(lst)
# print(chr(89))
# print(700//26)
# print(chr(90))
# map = {}
# map.clear()
# print(map)
#
# map1 = {1:2,3:4,5:2}
# print(set(map1))
# map1[1] = 3
# print(map1.__contains__(4))
# print(map1)
#
# print(4 in map1.values())

map1 = {'b': 'b', 'a': 'a', 'd': 'b', 'c': 'a'}
mapval = [map1[k] for k in map1]
print(mapval)
print(set(mapval))
print(len(mapval))
print(len(set(mapval)))

