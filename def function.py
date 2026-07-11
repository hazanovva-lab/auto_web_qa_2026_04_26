# #def calc_sum(a: int, b: int) -> int
#
# #def name(a, b, c="some"):
# #    print (name)
#
# integer = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# # new_list = []
#
# # for num in integer:
# #     if num % 2 ==0:
# #         new_list.append(num)
# # print(new_list)
#
# list_comprehension = (num for num in integer if num % 2 ==0)
# target_num = next((num for num in list_comprehension if num == 3), None)
# print(target_num)
# # print(next(list_comprehension))


product = {"apple":10, "orange":4, "banana":15}
print(dict(sorted(product.items(), key=lambda x: x[1], reverse=True)))
