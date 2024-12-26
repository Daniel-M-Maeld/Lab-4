import copy
MAX_CELLS = 9

items = {
    1: {'points': 25, 'size': 3, "name": 'r'},
    2: {'points': 15, 'size': 2, "name": 'p'},
    3: {'points': 15, 'size': 2, "name": 'a'},
    4: {'points': 20, 'size': 2, "name": 'm'},
    5: {'points': 5, 'size': 1, "name": 'i'},
    6: {'points': 15, 'size': 1, "name": 'k'},
    7: {'points': 20, 'size': 3, "name": 'x'},
    8: {'points': 25, 'size': 1, "name": 't'},
    9: {'points': 15, 'size': 1, "name": 'f'},
    10: {'points': 10, 'size': 1, "name": 'd'},
    11: {'points': 20, 'size': 2, "name": 's'},
    12: {'points': 20, 'size': 2, "name": 'c'},
}


def table_memo(items, max_cells):
    bag = [ [ [ 0 for _ in range(9)] for _ in range(max_cells)] for _ in range(len(items))]
    table = [ [ 0 for _ in range(max_cells)] for _ in range(len(items))]
    for row, value in enumerate(items.values()):
        size = value['size']
        points = value['points']
        name = value["name"]
        for limit_size in range(1, max_cells+1):
            col = limit_size - 1   
            
            if row == 0:
                
                if size > limit_size:
                    table[row][col] = 0 
                else:
                    table[row][col] = points
                    for i in range(size):
                        bag[row][col][i] = name
            else:
                prev_price = table[row-1][col]
                prev_bag = bag[row-1][col]
                if size > limit_size:
                    table[row][col] = prev_price
                    bag[row][col] = prev_bag
                else:
                    
                    if col-size < 0:
                        used = 0 
                    else:
                        used = table[row-1][col-size]
                    if prev_price >= points + used:
                        res = prev_price
                        new_bag = prev_bag
                    else:
                        if col-size < 0:
                            new_bag = [0,0,0,0,0,0,0,0,0]
                        else:
                            new_bag = copy.deepcopy(bag[row-1][col-size])
                            
                        x = new_bag.index(0)
                        for i in range(x, x+size):
                            new_bag[i] = name
                        res = points + used

                    table[row][col] = res
                    bag[row][col] = new_bag


    print(table[len(items)-1][MAX_CELLS-1])
    print('[',bag[len(items)-1][MAX_CELLS-1][0],']','[',bag[len(items)-1][MAX_CELLS-1][1],']','[',bag[len(items)-1][MAX_CELLS-1][2],']')
    print('[',bag[len(items)-1][MAX_CELLS-1][3],']','[',bag[len(items)-1][MAX_CELLS-1][4],']','[',bag[len(items)-1][MAX_CELLS-1][5],']')
    print('[',bag[len(items)-1][MAX_CELLS-1][6],']','[',bag[len(items)-1][MAX_CELLS-1][7],']','[',bag[len(items)-1][MAX_CELLS-1][8],']')
table_memo(items, MAX_CELLS)