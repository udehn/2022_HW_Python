
def find_triplets(arr):
    ans = []
    for i in range(len(arr) - 2):
        for j in range(i + 1, len(arr) - 1):
            if abs(arr[i] - arr[j]) > a:
                continue
            for k in range(j + 1, len(arr)):
                if abs(arr[j] - arr[k]) > b or abs(arr[i] - arr[k]) > c:
                    continue
                else:
                    ans.append((arr[i], arr[j], arr[k]))
    return ans

if __name__ == '__main__':

    # Input
    # arr_temp = input("Input: arr = ")
    # a = int(input("a = "))
    # b = int(input("b = "))
    # c = int(input("c = "))
    # arr = [int(n) for n in arr_temp.split()]

    # sample 1
    arr = [3, 0, 1, 1, 9, 7]
    a = 7
    b = 2
    c = 3

    # sample 2
    # arr = [1, 1, 2, 2, 3]
    # a = 0
    # b = 0
    # c = 1

    ans = find_triplets(arr)
    if ans == []:
        print("No triplets")
    else:
        print(ans)
