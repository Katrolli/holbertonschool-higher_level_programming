def uniq_add(my_list=[]):
    tmp = set(my_list)
    new_list = (list(tmp))
    sum = 0
    for i, nr in enumerate(new_list):
        sum += new_list[i]
    return sum
