def length_of_str(value):
    return len(str(value))


def counting_mx_len_for_annual_values_table(curr_value_str_len, mx_value_str_len):
    if curr_value_str_len > mx_value_str_len:
        mx_value_str_len = curr_value_str_len
    return mx_value_str_len

