import sys

def record_gap(str, gaps=[]):
    if len(str) >= 0:
        try:
            one = str.index('1',0)
        except Exception as exception:
            # print(exception.__class__.__name__)
            return gaps
        if one < len(str):
            gaps.append(one)
            str = str[one+1::]
            # print("sliced string:",str)
            record_gap(str,gaps)
        return gaps

def binary_gap(n,gaps = []):
    if n <= 0:
        return 0
    if n > 2147483647:
        return 0

    else:
        gaps = []
        mother_str = bin(n).replace('0b','').__str__()

        try:
            first_one = mother_str.index('1',0)
        except Exception as exception:
            print(exception.__class__.__name__)

        child_str = mother_str[first_one+1::]
        record_gap(child_str,gaps)

        if len(gaps) >0:
            return max(gaps)
        else:
            return 0


if __name__ == '__main__':
    # a test case
    print(binary_gap(25))