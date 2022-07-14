x = [[5, 9, 7, 17, 13, 0], [8, 10, 16, 35, 7, 5], [10, 17, 5]]
y = [[3, 2, 5], [16, 9, 7, 15, 0, 17, 20], [17, 1], [107, 57, 21]]
   

def sort_multi_array(x):
    num = []
    res = []
    num_len = 0

    for a in x:
        for s in a:
            num.append(s)
        
    data = sorted(num)
    for a in x:
        res.append([])
        for s in a:
            num_len = num_len+1
            res[x.index(a)].append(data[num_len-1])
    
    return res

print(sort_multi_array(x))
print(sort_multi_array(y))