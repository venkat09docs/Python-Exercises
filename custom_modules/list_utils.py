""" list_utils_02.py is a sample Python module that exposes list utility functions """

__usage_counter = 0
def sum_elements(user_list):
    global __usage_counter
    __usage_counter += 1
    element_sum = 0
    for el in user_list:
        element_sum += el
    return element_sum

def double_each_element(user_list):
    global __usage_counter
    __usage_counter += 1
    return [element * 2 for element in user_list]

def get_usage_counter():
    global __usage_counter
    return __usage_counter

if __name__ == '__main__' :
    __entry_list = [1, 2, 3, 4, 5]
    __summed = sum_elements(__entry_list)

    if __summed == 15:
        print("Sum is Okay")
    else:
        print("Sum is not Okay")

    doubled = double_each_element(__entry_list)
    entry_list = doubled
    doubled = double_each_element(entry_list)
    if doubled == [2, 4, 6, 8, 10]:
        print("Doubled is Okay")
    else:
        print("Doubled is not Okay")

    print("The Counter Value - " + str(__usage_counter))