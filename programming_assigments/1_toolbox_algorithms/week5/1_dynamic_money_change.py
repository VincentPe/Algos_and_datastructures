# Uses python3
import sys

def get_change(m):
    if m < 3:
        return m
    if (m == 3) | (m == 4):
        return 1
    memory = [0, 1, 2, 1, 1]
    for i in range(5, m+1):
        one = memory[i-1] + 1
        two = memory[i-3] + 1
        three = memory[i-4] + 1
        memory.append(min(one, two, three))
    return memory[m]
 

## TO DO topdown rather than bottom up

#m = 1000
#coins = [1, 3, 4]
#
#get_change(m)



if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
