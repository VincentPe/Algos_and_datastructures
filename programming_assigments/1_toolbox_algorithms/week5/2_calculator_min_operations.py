# Uses python3
import sys

def optimal_sequence(n):
    sequence = []
    while n >= 1:
        sequence.append(n)
        if n % 3 == 0:
            n = n // 3
        elif n % 2 == 0:
            n = n // 2
        else:
            n = n - 1
    return reversed(sequence)


def bottom_up_primcalc(n):
    if n < 2:
        return [n]
    sequence = [[0,0],[1,1]]
    for i in range(2, n+1):
        one = sequence[i-1][0] + 1
        if i % 2 == 0:
            two = sequence[i//2][0] + 1
        else:
            two = n+1
        if i % 3 == 0:
            three = sequence[i//3][0] + 1
        else:
            three = n+1
        
        if (one <= two) & (one <= three):
            sequence.append([one, i-1])
        elif two <= three:
            sequence.append([two, i//2])
        else:
            sequence.append([three, i//3])
    output = [n]
    while n > 1:
        output.append(sequence[n][1])
        n = sequence[n][1]
    return output


#bottom_up_primcalc(96234)
    

#bottom_up_primcalc(1)


input = sys.stdin.read()
n = int(input)
sequence = list(bottom_up_primcalc(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
