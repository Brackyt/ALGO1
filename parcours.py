def parcours(house_list):
    """
    Bubble sort
    """
    for i in range(0, len(house_list) - 1):
        swap_test = False
        for j in range(0, len(house_list) - i - 1):
            if house_list[j] > house_list[j + 1]:
                house_list[j], house_list[j + 1] = house_list[j + 1], house_list[j]
            swap_test = True
        if swap_test == False:
            break
    return house_list