from __init__ import *

def gen_pallettes(color_list, dict_lab):
    dict_color = {}
    for i in color_list:
        split_list = i.split(':')
        split_colors = split_list[1].split('-')
        dict_color[split_list[0].capitalize()] = split_colors

    if len(dict_color) != len(dict_lab):
        print(f'**Error: Your color lebels are NOT complete, please check input command')
        exit()
    else:
        color_val = [val for key, val in dict_color.items()]
        lab_val = [val for key, val in dict_lab.items()]
        color_num = [len(num) for num in color_val]
        lab_num = [len(num) for num in lab_val]
        if color_num != lab_num:
            print(f'**Error: Your color lebels are NOT complete, please check input command')
            exit()
        else:
            pass

    return(dict_color)

def gen_onehot(df, label):
    new_df = pd.DataFrame.from_dict(df)
    val = [val for key, val in label.items()]
    for i in val:
        sort_list = sorted(i)
        o = 0
        for j in sort_list:
            new_df = new_df.replace(j,o)
            o += 1
        o = 0

    arr = new_df.to_numpy()
    print('>> Replace labels with one-hot <<')
    print(new_df)
    print("-------------------------------------------------------------------------------------------------------------------------------------")
    return(arr)


def capital_fromUp(string):
    new_str = [*string]
    capi = []
    for i in range(len(new_str)):
        if i == 0:
            capi.append(new_str[i])
        else:
            capi.append(new_str[i].lower())
    capi = ''.join(capi)
    return(capi)

def change_decim_021(intiger):
    if intiger != 0:
        percent = int(round(intiger, 2) * 100)
        string_num = str(percent)
        last2_str = string_num[-2]
        if last2_str == '0':
            return(int(intiger))
        else:
            return(round(intiger, 1))
    else:
        return(int(intiger))

def divide_decim(intiger, divide):
    if intiger != 0 and divide == 2:
        percent = int(round(intiger, 2) * 100)
        string_num = str(percent)
        if int(string_num) % 2 == 0:
            return(True)
        else:
            return(False)
    else:
        return(True)
