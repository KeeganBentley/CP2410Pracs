
def unique_list(list_of_nums):
    unique_num_list = []
    for num in list_of_nums:
        if num not in unique_num_list:
            unique_num_list.append(num)
            print(unique_num_list)
        else:
            return False
    return True


