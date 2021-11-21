if __name__ == '__main__':
    outer_list = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        inner_list_temp = [name, score]
        outer_list.append(inner_list_temp)
        # outer_list.append( [input(), float(input())] )   #last_4_line_in_one

    # make score list
    score_list = []
    for _ in outer_list:
        score_list.append(_[1])

    # using 2 pointer for min & min_2 // greedy method ? //
    # corner case: fails when min/max appear before min_2/max_2 in list
    mini = score_list[0]
    second_min = mini
    maxi = score_list[0]
    second_max = maxi
    for _ in score_list:
        if _ < mini:
            second_min = mini
            mini = _
        elif _ < second_min:  # for handling the corner case // must needed
            second_min = _

        # if _ > maxi:
        #     second_max = maxi
        #     maxi = _
        # elif _ > second_max: # handling corner case
        #     second_max = _
    # print("Minimum value: " +str(mini))
    # print("Second last :" +str(second_min))
    # print("Max value: " +str(maxi))
    # print("Runner Up: " +str(second_max))

    # Extracting the names of min_2 score holders
    name_temp = []
    for _ in outer_list:
        if _[1] == second_min:
            name_temp.append(_[0])

    # printing names on separate line
    for _ in sorted(name_temp):
        print(_)

    '''   
    #solve using diff & late_diff method
    #corner_case: fails when min_2 is negative 
    #Find min_2 from score list
    late_diff = max(score_list)
    for item in score_list:
        diff = item - min(score_list)
        if diff > 0 and diff < late_diff:
            late_diff = diff
            second_min = item
    '''

    '''
    #solve using diff & late_diff method
    #corner_case: fails when min_2 is negative 
    # Finding min_2 from outer & score list /// needs score list 
    late_diff = max(score_list)
    for inner_list in outer_list: #returns in inner list in each call
        diff = inner_list[1] - min(score_list)
        if diff>0 and diff<late_diff:
            late_diff = diff
            min_second = inner_list[1]
    '''