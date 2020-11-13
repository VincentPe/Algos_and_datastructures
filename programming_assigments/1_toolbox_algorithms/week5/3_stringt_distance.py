# Uses python3
def edit_distance(a, b):
    len_a = len(a)
    len_b = len(b)
    
    matrix = []
    matrix.append([x for x in range(len_a+1)])
    for i in range(1, len_b+1):
        matrix.append([i if x == 0 else 0 for x in range(len_a+1)])
        
    for j in range(1, len_b+1):
        for i in range(1, len_a+1):
        
            insertion = matrix[j][i-1] + 1
            deletion = matrix[j-1][i] + 1
            match = matrix[j-1][i-1] 
            mismatch = matrix[j-1][i-1] + 1
            
            #print(' Insertion: {} \n Deletion: {} \n Match: {} \n Mismatch: {}'.format(insertion, deletion, match, mismatch))
            #print(' a: {} \n b: {}'.format(a[i-1], b[j-1]))
            
            if a[i-1] == b[j-1]:
                matrix[j][i] = min(insertion, deletion, match)
            else:
                matrix[j][i] = min(insertion, deletion, mismatch)

    return matrix[j][i]



#a = 'distance'
#b = 'editing'
#edit_distance(a, b)
#
#a = 'short'
#b = 'ports'
#edit_distance(a, b)



        


if __name__ == "__main__":
    print(edit_distance(input(), input()))
