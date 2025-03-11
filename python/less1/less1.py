import time
from datetime import datetime

str = input()
stack = []
arr = list(str)
try:
    startTime  = datetime.now()
    for i in arr:
        if i == "(":
            stack.append(i)
        if i == ")":
            if stack[0] == "(":
                stack.pop()
    if len(stack) == 0:
        print("Послідовність правильна")
        finalTime = datetime.now()
except:
    print("Послідовність неправильна")
    finalTime = datetime.now()

print(finalTime)
print(startTime)
result = finalTime-startTime
print(result)