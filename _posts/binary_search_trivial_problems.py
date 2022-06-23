def checkSquare(num):
    if num == 1:
        return True
    else:
        for i in range(2, num//2, 1):
            if i**2 == num:
                return True
    return False
    
def checkSquare2(num):
    if num == 1:
        return True
    l = 0
    r = num // 2
    while l <= r:
        m = l + (r - l)//2
        if m*m > num:
            r = m -1
        elif m*m < num:
            l = m + 1
        else:
            return True
    return False
# print(checkSquare2(3))

from datetime import datetime
import pandas as pd
def compareTime(A):
    bs, bs_time, linear, linear_time = [], [], [], []
    for i in A:
        t0 = datetime.now()
        bs.append(checkSquare2(i))
        bs_time.append((datetime.now() - t0).microseconds)

        t1 = datetime.now()
        linear.append(checkSquare(i))
        linear_time.append((datetime.now() - t1).microseconds)
    df = pd.DataFrame({
        'num': A,
        'bs': bs,
        'bs_time': bs_time,
        'linear': linear,
        'linear_time': linear_time
    })
    return df

A = [3, 30, 300, 3000, 30000, 300000, 3000000]
result = compareTime(A)
print(result)