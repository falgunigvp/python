def print_list_r(lst, index=0):

    if index == len(lst):
        return 1
    
    print(lst[index])
    
 
    print_list_r(lst, index + 1)


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print_list_r(my_list)
