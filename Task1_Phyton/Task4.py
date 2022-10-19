def get_pair_for_target(list: list, target: int):
    return_list_of_pairs = []
    for i in range(len(list)):
        for j in range(i, len(list)):
            if((list[i], list[j]) not in return_list_of_pairs):
                if(list[i] + list[j] == target):     
                    return_list_of_pairs.append((list[i], list[j]))
    return return_list_of_pairs