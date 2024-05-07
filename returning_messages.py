from operating_on_dates import date_to_str


def create_error_message(error_dict, counter):
    temp_str = str(counter) + ".Inconsistent input data in "
    for key in error_dict:
        temp_tuple = error_dict[key]
        prev_value = temp_tuple[0]
        curr_value = temp_tuple[1]
        temp_str += key + " : " + str(prev_value) + " > " + str(curr_value) + " "
    return temp_str


def create_annual_value_message(message_list, len_tup, mx_distance_str_len, mx_engine_hours_str_len):
    temp_str = str(message_list[0]) + ". " + date_to_str(message_list[4]) + " |"
    mx_len_tup = (mx_distance_str_len, mx_engine_hours_str_len)
    temp_list = [" annual distance(km): ", " | annual engine hours(h): ", " | average fuel consumption per 100 km: "]
    for i in range(1, 4):

        if i != 3:
            temp_str += temp_list[i - 1] + str(message_list[i]) + " " * (mx_len_tup[i - 1] - len_tup[i - 1])
        else:
            temp_str += temp_list[i - 1] + str(message_list[i])
    return temp_str
