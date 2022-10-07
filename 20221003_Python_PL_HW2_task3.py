import copy

import numpy

def Solve(times_list, entrance, times_map, run_time, max_run_time):
    now_run_time = run_time
    next_times_list = copy.deepcopy(times_list)
    # flag = 0

    while times_list:
        if entrance == times_list[-1][0]:
            times_map[times_list[-1][1] - 1] = 1
            # if flag == 0:
            run_time = now_run_time + times_list[-1][2]
            #     flag = 1
            next_times_list.remove(times_list[-1])
            for value in times_list:
                if value[1] == entrance:
                    next_times_list.remove(value)
            times_map, run_time, max_run_time = Solve(next_times_list, times_list[-1][1], times_map, run_time, max_run_time)
            next_times_list = copy.deepcopy(times_list)
        times_list.pop()

    if max_run_time < run_time:
        max_run_time = run_time
    return times_map, run_time, max_run_time

if __name__ == "__main__":

    # sample 1
    times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
    N = 4
    X = 2

    # sample 2
    # times = [[1, 2, 1]]
    # N = 2
    # X = 2

    # times = [[2, 1, 1], [6, 7, 1], [1, 5, 3], [1, 8, 2], [2, 3, 1], [4, 6, 1], [3, 4, 1], [3, 9, 3]]
    # N = 9
    # X = 2

    answer_map = numpy.zeros(N)
    answer_map[X - 1] = 1

    m, t, max_t = Solve(times, X, answer_map, 0, 0)

    flag = 1
    for value in m:
        if value == 0:
            flag = -1
            break

    if flag == 1:
        print(max_t)
    else:
        print(flag)