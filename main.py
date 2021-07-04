from Restoring import Restoring_division
from gates import dec_bin

num1 = int(input("Enter Dividend : "))
num2 = int(input("Enter Divisor : "))

dividend = dec_bin(num1,False)
divisor = dec_bin(num2,False)

qoutient , remainder = Restoring_division(dividend, divisor)

print("Qoutient : ", qoutient)
print("Remainder : ",remainder)







