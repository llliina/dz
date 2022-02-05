from random import uniform

def transfer_list_in_str(list_in: list) -> str:
    str_out = ''
    for i in list_in:
        remain = round((float(i) - int(i))* 100)
        if remain != 0:
            if remain % 10 == remain:
                i = str(int(i)) + ' руб ' + ' 0'+ str(remain) + " коп, "
            else:
                i = str(int(i)) + ' руб ' + str(remain) + " коп, "
        elif remain == 0:
            i = str(int(i)) + ' руб ' + '00' + ' коп, '
        str_out += i
    return str_out
my_list = [round(uniform(10, 100), 2) for _ in range(1,16)]
print(f'исходный список: {my_list}')
result_1 = transfer_list_in_str(my_list)
print(result_1)

def sort_prices(list_in: list) -> list:
    list_in.sort()
    return list_in


print(id(my_list))
result_2 = sort_prices(my_list)
print(id(my_list))
print(result_2)

def sort_price_adv(list_in: list) -> list:
    list_out = sorted(list_in, reverse=True)
    return list_out


result_3 = sort_price_adv(my_list)
print(result_3)

def check_five_max_elements(list_in: list) -> list:
    list_out = result_3[1: 6]
    return list_out

result_4 = check_five_max_elements(my_list)
print(result_4)
