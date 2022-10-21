my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
res_list_1 = []
for el in range(1, len(my_list)):
    if my_list[el] > my_list[el - 1]:
        res_list_1.append(my_list[el])

print(res_list_1)

res_list_2 = [my_list[el] for el in range(
    1, len(my_list)) if my_list[el] > my_list[el - 1]]

print(res_list_2)
