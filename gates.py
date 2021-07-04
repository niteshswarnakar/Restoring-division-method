inputs = [0,1]

#and gate

def AND(a,b):
    if (a not in inputs) or (b not in inputs):
        print("invalid input")
    elif a == 1 and b == 1:
        return 1
    else :
        return 0

def OR(a,b):
    if (a not in inputs) or (b not in inputs):
        print("invalid input")
    elif a == 0 and b == 0:
        return 0
    else:
        return 1

def XOR(a,b):
    if (a not in inputs) or (b not in inputs):
        print("invalid input")
    elif a != b:
        return 1
    else:
        return 0

def NOT(a):
    b = not a
    return b


#other useful functions
def split_word(word):
    return [letter for letter in word]

def join_list(li):
    a = ""
    for i in range(len(li)):
        a = a+str(li[i])
    return a

def Sum(a,b,c = 0):
    return XOR(c,XOR(a,b))

def Carry(a,b, c = 0):
    return OR(AND(a,b),AND(c,XOR(a,b)))

def Diff(a,b,bin = 0):
    return XOR(XOR(a,b),bin)

def Borrow(a,b, bin = 0):
    return OR(AND(not XOR(a,b),bin),AND(not a, b))

def Adder(a,b):
    max_length = len(a) if a > b else len(b)
    local_sum = []
    
    local_carry = []
    carry = 0
    for m,n in zip(a[::-1],b[::-1]):
        local_sum.append(Sum(m,n,carry))
        carry = Carry(m,n,carry)
    
    # if carry == 1:
    #     local_sum.append(carry)
    #     carry = 0
        
    local_sum.reverse()
    return local_sum


def Subtractor(a,b):
    max_length = len(a) if a > b else len(b)
    local_diff = []
    borrow = 0
    for m,n in zip(a[::-1],b[::-1]):
        local_diff.append(Diff(m,n,borrow))
        borrow = Borrow(m,n,borrow)
    
    local_diff.reverse()

    return (local_diff,borrow)

def Subtractor_by_complement(a, b, borrow=0, cin=0):
    diff = []
    b_comp = complement_2(b)[:]
    for i in range(len(a)-1, -1, -1):
        # Logical implementation of the difference function of the full adder
        # A xor B xor C
        diff.insert(0, Sum(a[i],b_comp[i],cin))
        cin = OR(OR(AND(a[i],b_comp[i]), AND(b_comp[i], cin)), AND(a[i], cin))

    return diff

def complement_2(b):
    a = []
    i = len(b)-1
    while b[i] != 1:
        a.append(b[i])
        i-=1
    a.append(b[i])
    i-=1
    while i>=0:
        a.append(XOR(1,b[i]))
        i-=1
    a.reverse()
    return a

def dec_bin(num,sign):
    num1 = num
    num = abs(num)

    b = []
    while num!=0:
        re = num%2
        b.append(re)
        num = num //2
    b.append(0)
    # if sign == True:
    #     b.append(0)
    b.reverse()
    if num1 < 0:
        b = complement_2(b)

    return b

def Shift_left(li):
    size = len(li)-1
    i = 0
    while i<size:
        li[i] = li[i+1]
        i += 1
    return li


if __name__ == "__main__":
    print(Subtractor([0,1,1,0],[1,0,1,0]))
        











