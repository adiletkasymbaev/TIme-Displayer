import sys
summa = sum
def func():
    global summa
    sums = []
    result = []
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))
    q = int(sys.stdin.readline())
    if len(a) % 2 == 0:
        mid = (len(a) // 2) - 1
    else:
        mid = ((len(a) + 1) // 2) - 1

    for j in range(q):
        sums = []
        x = list(sys.stdin.readline().split())
        if x[0] == '1':
            if len(a) % 2 == 0:
                a.insert(mid+1, int(x[1]))
            else:
                a.insert(mid, int(x[1]))
            if len(a) % 2 == 0:
                mid = (len(a) // 2) - 1
            else:
                mid = ((len(a) + 1) // 2) - 1
        elif x[0] == '2':
            a.remove(a[mid])
            if len(a) % 2 == 0:
                mid = ((len(a) + 1) // 2) - 1
            else:
                mid = ((len(a)) // 2) - 1
        elif x[0] == '3':
            l = int(x[1]) - 1
            r = int(x[2]) - 1
            for i in range(l, r+1):
                sums.append(a[i])
                sum = summa(sums)
            result.append(str(sum))
    print(' '.join(result))
func()

# https://testing.kg/media/uploads/2024/09/12/2_JExI2Hi.pdf
# Задача Е
