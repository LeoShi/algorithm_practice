def sub_sequent_with_nlogn(a):
    """
    Problem: http://weibo.com/1915548291/A7ArDvUzY
    """
    negative_len = len(filter(lambda item: item < 0, a))
    first_part, second_part = a[:negative_len], a[negative_len:]
    first_positive_index, first_negative_index = -1, -1

    for first_index in range(0, len(first_part)):
        if a[first_index] > 0:
            first_positive_index = first_index
            break
    for second_index in range(negative_len, len(a)):
        if a[second_index] < 0:
            first_negative_index = second_index
            break

    if first_positive_index >= 0 and first_negative_index >= 0:
        temp = a[first_positive_index]
        a[first_positive_index] = a[first_negative_index] * -1
        a[first_negative_index] = temp * -1

    #recursive
    if len(first_part) > 1:
        a[:negative_len] = sub_sequent_with_nlogn(a[:negative_len])
    if len(second_part) > 1:
        a[negative_len:] = sub_sequent_with_nlogn(a[negative_len:])

    # fix symbol
    for first_index in range(0, len(first_part)):
        if a[first_index] > 0:
            a[first_index] *= -1
    for second_index in range(negative_len, len(a)):
        if a[second_index] < 0:
            a[second_index] *= -1
    return a

a = [-1, 1, -3, -2 ,2, 5, 7, 4, -6, 9]
print sub_sequent_with_nlogn(a)

#output: [-1, -3, -2, -6, 1, 2, 5, 7, 4, 9]
