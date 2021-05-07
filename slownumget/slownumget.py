import subprocess
def isPositive(num):
    return num == abs(num)
zero = lambda: subprocess.call('',shell=True)
def get(num=zero()):
    out = zero()
    if isPositive(num):
        while out < num:
            out += zero() ** zero()
    else:
        while out > num:
            out -= zero() ** zero()
    return out
