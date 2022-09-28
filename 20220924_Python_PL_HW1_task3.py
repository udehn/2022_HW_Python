
import random

def get_count_dict(arr):
    count_dict = {}
    for number in arr:
        count_dict[number] = 0
    for number in arr:
        count_dict[number] = count_dict[number] + 1
    return count_dict

def get_revert_dict(old_dict, min_value, max_value):
    reversed_dict = dict([(i, []) for i in range(min_value, max_value + 1)])
    for key, value in old_dict.items():
        reversed_dict[value].append(key)
    return reversed_dict

def get_min_and_max_values(old_dict):
    max_value = -100000
    min_value = 100000
    for value in old_dict.values():
        if max_value < value:
            max_value = value
        if min_value > value:
            min_value = value
    return min_value, max_value

def Solution(arr, k):
    count_dict = get_count_dict(arr)
    min_value, max_value = get_min_and_max_values(count_dict)
    revert_count_dict = get_revert_dict(count_dict, min_value, max_value)

    ans = []
    for i in range(max_value, min_value - 1, -1):
        if len(ans) <= k:
            ans.extend(revert_count_dict[i])
        else:
            break

    if k <= len(ans):
        print("Top", k, ":", ans[:k])
    else:
        print("k has exceeded the array size")

def random_init(len_arr=100000, element_size_lower_bound=-10000, element_size_upper_bound=10000):
    arr_random = []
    for i in range(len_arr):
        arr_random.append(random.randint(element_size_lower_bound, element_size_upper_bound))
    return arr_random

if __name__ == '__main__':
    # Random init array
    # len_arr = 1002
    # element_size_lower_bound = -89
    # element_size_upper_bound = 313
    # arr = random_init(len_arr, element_size_lower_bound, element_size_upper_bound)
    # print(arr)
    # print(len_arr)
    # print(element_size_upper_bound)
    # print(element_size_lower_bound)
    # k = 23

    # Input
    # arr_temp = input("Input: arr = ")
    # arr = [int(n) for n in arr_temp.split()]
    # k = int(input("k = "))

    # sample 1
    arr = [1, 1, 1, 2, 2, 3]
    k = 2

    # sample 2
    # arr = [1]
    # k = 1

    print("array is:", arr)
    print("k is:", k)

    Solution(arr, k)



