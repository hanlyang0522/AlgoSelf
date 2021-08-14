import sys

n_size = int(sys.stdin.readline())

A = [[0] for i in range(n_size)]

for i in range(n_size):
    tmp_list = list(map(int, sys.stdin.readline().split()))
    A[i] = tmp_list

# print(A)

# start
x, y = n_size//2, n_size//2
# print(x, y, A[y][x])

# sand, dir, step
sand_out = 0
dir = ['l', 'd', 'r', 'u']
dir_idx = 0
step_size = 1

# sand_dispose(y, x)
list_lr = [[-1, 1], [-1, 0], [-2, 0], [-1, -1], [0, -2], [1, -1], [2, 0], [1, 0], [1, 1]]
list_ud = [[-1, -1], [0, -2], [0, -1], [1, -1], [2, 0], [1, 1], [0, 1], [0, 2], [-1, 1]]
list_perc = [1, 2, 10, 5, 10, 2, 7, 1]

while not(x==0 and y==0):
    for step in range(step_size):
        sand_tmp = 0
        sand_fall = 0

        if dir[dir_idx] == 'l':
            x = x-1

            for fall_idx in range(9):
                a, b = list_lr[fall_idx]

                sand_fall = round(A[y][x]*list_perc[fall_idx]/100)
                
                if y+a < 0 or y+a >= n_size or x+b < 0 or x+b >= n_size:
                    sand_out += sand_fall
                    continue
                else:
                    A[y+a][x+b] = sand_fall
            
            if x-1 < 0:
                sand_out += sand_fall


        elif dir[dir_idx] == 'd':
            y = y+1
    
        elif dir[dir_idx] == 'r':
            x = x+1
    
        elif dir[dir_idx] == 'u':
            y = y+1
    










print(sand_out)
