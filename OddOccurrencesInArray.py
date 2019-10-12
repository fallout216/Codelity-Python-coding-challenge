import numpy as np

def return_odd_element(input=[]):
    arr = np.array(input)
    if len(arr) == 0:
        return None
    else:
        # print('the new array is', arr)
        target = arr[0]
        paired = np.where(arr == target)
        if len(paired[0]) % 2 is not 0:
            return target
        else:
            new_array = np.delete(arr,paired[0])
            return return_odd_element(new_array)

if __name__=='__main__':
    # a test case
    print(return_odd_element([9, -1, 9, 9, 9, 2, 2, 3, -1]))