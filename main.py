import random as rnd

arr_num ='0123456789'
arr_en = 'abcdefghijklmnopqrstuvwxyz'
arr_EN = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' 
arr_symb = '!@#$%_?/'

is_pincode = False
is_num = True
is_latter = True
is_symb = False
pwd_lenght = 8 # Dlina parola

arr_all = ''
if is_pincode:
    arr_all = arr_num
if is_latter:
    arr_all = arr_en + arr_EN
if is_num:
    arr_all += arr_num
if is_latter:
    arr_all = arr_symb + arr_all + arr_num

def sample(arr, count):
    tmp_sample = [None] * count
    for i in range(count):
        random_index = rnd.randint(0, len(arr)-1)
        random_element = arr[random_index]
        tmp_sample.append(random_element)
    return tmp_sample 
   
#arr_all = rnd.sample(arr_all, len(arr_all))

arr_pwd = rnd.sample(arr_all, pwd_lenght)

print(''.join(arr_pwd))