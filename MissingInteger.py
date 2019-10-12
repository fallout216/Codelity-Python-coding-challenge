
def solution(A):
    # write your code in Python 3.6

    A = sorted(A)
    A = list(dict.fromkeys(A))

    print("A:",A)

    if A[len(A) - 1] < 0:
        return 1

    if A[len(A) - 1] == (A[0] + len(A) - 1):
        return A[len(A) - 1] + 1

    if len(A) == 1:
        return A[0] + 1

    lo = 0
    high = len(A) - 1
    ptr = (high - lo) // 2 + lo

    return bin_search_missing(high, lo, ptr, A)
    pass

def bin_search_missing(high, lo, ptr, A):
    # if A[ptr] != A[ptr-1] + 1:
    #    return A[ptr-1] + 1

    if ptr == lo:
        return A[ptr] + 1
    if A[ptr] == A[lo] + (ptr - lo):
        lo = ptr
        ptr = (high - lo) // 2 + lo
        return bin_search_missing(high, lo, ptr, A)
    if A[high] == A[ptr] + (high - ptr):
        high = ptr
        ptr = (high - lo) // 2 + lo
        return bin_search_missing(high, lo, ptr, A)

if __name__ == '__main__':
    # a test case
    print(solution([-5,-1,-4,-2,-3]))