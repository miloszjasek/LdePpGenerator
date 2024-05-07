import datetime


def check_all_values(prev_info_dict, curr_info_dict):
    temp_dict = dict()
    is_error = False
    keys_to_check = {"total_distance", "total_engine_hours", "total_fuel_consumption"}
    prev_value = prev_info_dict["date"]
    curr_value = curr_info_dict["date"]
    if prev_value > curr_value:
        is_error = True
        temp_dict["date"] = [prev_value, curr_value]
    for key in keys_to_check:
        prev_value = int(prev_info_dict[key])
        curr_value = int(curr_info_dict[key])
        if not check_value(prev_value, curr_value):
            is_error = True
            temp_dict[key] = [prev_value, curr_value]

    return is_error, temp_dict


def check_value(prev_value, curr_value):
    if prev_value > curr_value:
        return False
    return True