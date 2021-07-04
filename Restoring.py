from gates import dec_bin, Adder, complement_2, Shift_left

def Restoring_division(dividend,divisor):
    divisor_complement = complement_2(divisor)
    n = len(dividend)
    Q = dividend
    A = [0 for i in range(n+1)]

    M = divisor
    li = A + Q
    for i in range(n):
        li = Shift_left(li)
 
        A = li[:len(A)]
        Q = li[len(A):]
        restore = A
        A = Adder(A,divisor_complement)

        if A[0] == 0:
            Q[-1] = 1
        elif A[0] == 1:
            A = restore
            Q[-1] = 0
        
        li = A + Q

    return (Q,A)