bdim = 8
bletter = ["a","b","c","d","e","f","g","h"]

# for num in reversed(range(bdim)):
#     for l in bletter:
#         print(l + str(num+1) , end=' ')
#     print()
    
def black_or_white(n):
    for num in reversed(range(bdim)):
        for l in bletter:
            if l + str(num+1) == str(n):
                color = int((bletter.index(l) + num + 1) % 2)                
                val = l + str(num+1)
                                
                if(color==0):
                    return val,"white"
                else:
                    return val,"black"

print(black_or_white("e3"))
print(black_or_white("g6"))