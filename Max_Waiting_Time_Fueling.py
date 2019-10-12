def solution(A,X,Y,Z):
    print("==========================")
    disp = [X, Y, Z]
    wait_time =[0,0,0]

    for i in range(len(A)):

        # the # of visited dispensers for car A[i]
        count = 0

        # update the priority based on which A[i] select the dispenser with the lowest waiting time
        priority = sorted(range(len(wait_time)), key=lambda k: wait_time[k])

        for j in priority:

            if A[i] <= disp[j]:
                print("car", i, "goes to dispenser", j)
                if i == len(A)-1:
                    return wait_time[j];
                else:
                    wait_time[j] += A[i]
                    disp[j] -= A[i]
                    break

            # no available dispenser that has fuel for A[i]
            else:
                count = count + 1
                if count == len(disp):
                    print("car ", i, "has visited all the three dispenser and none of them has sufficient fuel.")
                    return -1

print("[2,8,4,3,2], 7, 11, 3, waiting time: ", solution([2,8,4,3,2], 7, 11, 3))
print("[2,8,3,3,2], 7, 11, 3, waiting time: ", solution([2,8,3,3,2], 7, 11, 3))
print("[2,8,4,3,2,1,2], 7, 11, 3, waiting time: ", solution([2,8,4,3,2,1,2], 7, 11, 3))
print("[8,2,4,3,2,1,1], 7, 11, 3, waiting time: ", solution([8,2,4,3,2,1,1], 7, 11, 3))