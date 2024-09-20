

def element_sum(x:list):
    return x[0] + x[1]


def test_function_to_test():

    my_list= [1,2]
    assert element_sum(my_list) == 3

    my_list= [0]
    assert element_sum(my_list) == 0