# Uses python3
import sys

def get_change(m):
    coins = [10, 5, 1]
    c = 0
    while m > 0:
        if m >= coins[0]:
            m = m - coins[0]
        elif m >= coins[1]:
            m = m - coins[1]
        else:
            m = m - coins[2]
        c += 1
    return c

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
