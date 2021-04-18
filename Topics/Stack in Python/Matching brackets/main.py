# put your python code here
given_string = str(input())
open_brackets_count = 0
close_brackets_count = 0
error_flag = False

for letter in given_string:
    if letter == '(':
        open_brackets_count += 1
    elif letter == ')':
        if open_brackets_count > close_brackets_count:
            close_brackets_count += 1
        else:
            error_flag = True
            break

if open_brackets_count != close_brackets_count:
    print('ERROR')
elif error_flag:
    print('ERROR')
else:
    print('OK')
