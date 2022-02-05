def convert_list_in_str(list_in: list) -> str:
    index = 0
    for i in list_in:
        if i[-1].isdigit() == True:
            if len(i) == 1 or (len(i) == 2 and i[0].isdigit() == False):
                list_in.remove(i)
                i = list(i)
                i.insert(-1, '0')
                i = ''.join(i)
                list_in.insert(index, '"' + i + '"')
            else:
                list_in.remove(i)
                list_in.insert(index, '"' + i + '"')

        index +=1

    str_out = ' '.join(list_in)
    return str_out

my_list = ['в', '6', 'часов', '17', 'минут', 'температура', 'воздуха', 'была','+5', 'градусов']
result = convert_list_in_str(my_list)
print(result)