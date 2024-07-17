#name = input("Enter your name:")
# f-string 3.6+
#print(f"Hello {name}")

#-import math

#print(f"The of PI is approximately {math.pi:.3f}")

#yes_votes = 41_323_655
#no_votes = 51_598_123
#print(f"{no_votes / (no_votes + yes_votes):2.4f}")

#num1 = 2
#num2 = 12
#num3 = 145
# 002
# 012
# 145
#print(f"{num1:03d}")
#print(f"{num2:03d}")
#print(f"{num3:03d}")

import datetime

today = datetime.datetime.today()
print(f"{today:%b %d , %Y}")