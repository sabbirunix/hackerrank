if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    # split is used just to take the values from a single line seperated by sapce
    # this map just retuns the entered values as a map object; no further change

    as_list = list(arr)  # casting the `map object` ~ie: the values to list
    as_list.sort()  # to sort the list ; changed the original list as sorted one
    print(as_list)

    # now how do i select the 2nd largest element from a sorted list

    # huh ?
    # maybe use a reverse loop the check against the largest value and go backwards to check for the value less than it and then return once we found it

    # can i construct a backward for loop in python ??
    for num in as_list:
        if ((as_list[-1] - num != 0)):  # if number is not equal to largest number
            print()

    # do the whle loop thing # clears the midn
    # second_elem = 0  #or any arbitrary value here # second_elem = as_list[-2] #
    i = -1
    while i > -(len(as_list)):  # while -i > Neg.list_length
        if (as_list[i] < as_list[-1]):
            second_elem = as_list[i]
            break
        else:
            i = i - 1
    print("Second largest element is: " + str(second_elem))

    # using raw loop ##using two temp to save value

    # time complexity of __O(N)__
