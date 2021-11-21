def count_substring(string, sub_string):
    sliding_window_size = len(sub_string)
    counter = 0
    if len(sub_string) > len(string):
        return 0  # if sub_string is greter it isn't contained within

    # otherwise for every match increment counter
    for i in range(len(string) - sliding_window_size + 1):
        if string[i] == sub_string[0]:
            if string[i:i + sliding_window_size] == sub_string:
                counter = counter+1
                #++counter #why doesn't it work
    return counter


# typical sliding window problem
# return int type
if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)