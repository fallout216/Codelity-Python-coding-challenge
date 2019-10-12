def solution(X, Y, D):
    if Y <= X:
        return 0

    if X+D >= Y:
        return 1

    high = Y
    lo = 0
    ptr = high // 2 + lo

    # implement the binary search
    return binary_search(high,lo,ptr,X,Y,D)

def binary_search(high,lo,ptr,X,Y,D):
    if ptr*D+X >= Y and (ptr-1)*D+X < Y:
        return ptr
    if ptr*D+X > Y:
        high = ptr
        ptr = (high - lo) // 2 + lo
        return binary_search(high,lo,ptr,X,Y,D)
    if ptr*D+X < Y:
        lo = ptr
        ptr = (high - lo) // 2 + lo
        return binary_search(high, lo, ptr, X, Y, D)

if __name__ == '__main__':
    # a test case
    print(solution(54, 210, 1000))