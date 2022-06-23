def checkSquare(num):
    if num == 1:
        return True
    elif num == 2:
        return False
    else:
        for i in range(2, num//2, 1):
            if i**2 == num:
                return True

print(checkSquare(16))
print(checkSquare(3))

def checkSquare2(num):
    result = False
    if num == 1:
        result = True
        return result
    elif num == 2:
        result = False
        return result
    else:
        l = 2
        r = num
        while l < r:
            m = l + (l - r)//2
            if m*m > num:
                r = m -1
            elif m*m < num:
                l = m + 1
            else:
                return True
        return False

from datetime import datetime

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
        'num': A.tolist(),
        'bs': bs,
        'bs_time': bs_time,
        'linear': linear,
        'linear_time': linear_time
    })
    return df

import numpy as np
A = [3, 30, 300, 3000, 30000, 300000]
result = compareTime(A)