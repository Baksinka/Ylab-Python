from itertools import permutations


coord = [[0, 2], [2, 5], [5, 2], [6, 6], [8, 3]]

amount = len(coord)
maxel = coord[0][0]
minel = coord[0][0]
for i in range(amount):
    for j in range(2):
        if coord[i][j] < minel:
            minel = coord[i][j]
        if coord[i][j] > maxel:
            maxel = coord[i][j]
summ_min = amount * (2 * (maxel - minel) ** 2) ** 0.5
edges_min = []
elem_min = []
routes = permutations([i for i in range(1, amount)])
for elem in routes:
    edges = []
    elem_list = list(elem)
    elem_list.insert(0, 0)
    elem_list.insert(amount, 0)
    for i in range(amount):
        edges.append(((coord[elem_list[i]][0] - coord[elem_list[i + 1]][0]) **
                      2 + (coord[elem_list[i]][1] -
                           coord[elem_list[i + 1]][1]) ** 2) ** 0.5)
    summ = sum(edges)
    if summ < summ_min:
        summ_min = summ
        edges_min = edges
        elem_min = elem_list

print(tuple(coord[0]), end='')
summ_edges = 0
for i in range(amount):
    summ_edges += edges_min[i]
    print(' ->', tuple(coord[elem_min[i + 1]]), [summ_edges], end='')
print(' =', summ_min)
