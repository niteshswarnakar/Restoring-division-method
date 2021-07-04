a = [i for i in range(5,20)]

def Shift_left(li):
    size = len(li)-1
    i = 0
    while i<size:
        li[i] = li[i+1]
        i += 1
    return li

print(a)

print(Shift_left(a))