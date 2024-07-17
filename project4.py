X = 5
if X > 0:
    print("x is positive")

if False:
    print("This statement is not RuntimeWarning")
    X = 1

    print(X)

#X = input("Enter an integer: ")
#X  = int(X)
#if X % 2 == 0:
#    print('X is even')
#else:
#    print('X is odd')
#    X = 1
#    print(X)

X = 7
Y = 3
if X < Y:
    print("x is less than y")
    X = Y
elif X > Y:
    print("x is greater than y")
else:
    print("x and y are equal")

score = input("Enter score: ")
score = float(score)
if score >= 9.0:
    print("A")
elif score >= 0.8:
    print("B")
elif score >= 0.7:
    print("C")
elif score >= 0.6:
    print("D")
else:
    print("F")