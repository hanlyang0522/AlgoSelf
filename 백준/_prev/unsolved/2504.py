import sys

input = sys.stdin.readline()
p_list = list(input)[0:-1]
p_len = len(input) - 1
print(p_list, p_len)

sum = 0
while p_len > 0:
    for i in range(len(p_list)):
        if p_list[i] == '':
            continue

        elif p_list[i] == '(' and p_list[i+1] == ')':
            p_list[i] = '2'
            p_list[i+1] = ''
            p_len = p_len - 2
            

        elif p_list[i] == '[' and p_list[i+1] == ']':
            p_list[i] = '3'
            p_list[i+1] = ''
            p_len = p_len - 2

        elif p_list[i].isdigit() and p_list[i+1].isdigit():
            p_list[i] = str(int(p_list[i]) + int(p_list[i+1]))
            p_list[i+1] = ''
            p_len = p_len - 2

        elif p_list[i] == '(' and p_list[i+1].isdigit() and p_list[i+2] == ')':
            p_list[i] = str(2 * int(p_list[i+1]))
            p_list[i+1], p_list[i+2] = '', ''
            p_len = p_len - 2
        
        elif p_list[i] == '[' and p_list[i+1].isdigit() and p_list[i+2] == ']':
            p_list[i] = str(3 * int(p_list[i+1]))
            p_list[i+1], p_list[i+2] = '', ''
            p_len = p_len - 2
        
    while '' in p_list:
        p_list.remove('')

print(p_list[0])