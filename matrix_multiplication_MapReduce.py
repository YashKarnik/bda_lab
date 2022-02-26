A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]

i = len(A)
j = len(A[0])
k = len(B[0])

# Mapper

A_dict = {}

print('A:')
for x in range(k):
    for y in range(i):
        for z in range(j):
            S = '(({},{}),({},{},{}))'.format(y+1, x+1, 'A', z+1, A[y][z])
            print(S)
            A_dict[(y+1, x+1)] = A_dict.get((y+1, x+1), []) + \
                [('A', z+1, A[y][z])]

# print(A_dict)


B_dict = {}
print('B')
for x in range(i):
    for y in range(j):
        for z in range(k):
            S = '(({},{}),({},{},{}))'.format(x+1, z+1, 'B', y+1, B[y][z])
            print(S)
            B_dict[(x+1, z+1)] = B_dict.get((x+1, z+1), []) + \
                [('B', y+1, B[y][z])]
# print(B_dict)


# Reduce
res = [[0]*i for _ in range(k)]
print('\nReduce')
for i in A_dict.keys():
    print('{}=> A_LIST={}'.format(i, A_dict[i]))
    print('{}=> B_LIST={}'.format(i, B_dict[i]), end=' => ')
    x = A_dict[i][0][-1]*B_dict[i][0][-1] + A_dict[i][1][-1]*B_dict[i][1][-1]
    print(x)
    row, col = i
    res[row-1][col-1] = x
print(res)
