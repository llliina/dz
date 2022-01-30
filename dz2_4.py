def convert_name(list_in: list) -> list:
    list_out = []
    for i in list_in:
        name = i.split()[-1]
        list_out.append("Привет, " + name.capitalize() + "!")
    return list_out

my_list = ["инженер коструткор Игорь", "главный бухгалтер мАРИНА", "токать высшего разряда нИКОЛАЙ", "директор аэлитаа"]
result = convert_name(my_list)
print(result)