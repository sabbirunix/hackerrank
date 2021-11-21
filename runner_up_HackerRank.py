if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    sec_list = list(arr)
    print(sec_list)

    as_list = list(arr)  # casting the `map object` ~ie: the values to list
    as_list.sort()  # to sort the list ; changed the original list as sorted one
    print(as_list)

    # do the while loop thing # clears the mind
    i = -1
    while i > -(len(as_list)):  # while -i > Neg.list_length
        if (as_list[i] < as_list[-1]):
            second_elem = as_list[i]
            break
        else:
            i = i - 1
    print("Second largest element is: " + str(second_elem))

    # using for loop in reverse
    for num in reversed(as_list):
        if (num < as_list[-1]):
            second_elem = num
            break
    print("Second largest element is: " + str(second_elem))

# solve using the max method next #then you are done for sure
# probably -_O(2N)_- operation ## O(N) for max() ##O(N) for the loop
#     sec_list = list(arr)
#     print(sec_list)