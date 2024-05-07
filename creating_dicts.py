import datetime


def new_start_values(curr_info_dict):
    new_start_dict = dict()
    new_start_dict["date"] = curr_info_dict["date"]
    new_start_dict["total_distance"] = curr_info_dict["total_distance"]
    new_start_dict["total_engine_hours"] = curr_info_dict["total_engine_hours"]
    new_start_dict["total_fuel_consumption"] = curr_info_dict["total_fuel_consumption"]
    return new_start_dict


def create_dict(line):
    temp_list = line.split(",")
    temp_date = temp_list[2].split("-")
    temp_list[2] = datetime.date(int(temp_date[0]), int(temp_date[1]), int(temp_date[2]))
    info_dict = {
        "chassis_series": temp_list[0],
        "chassis_number": temp_list[1],
        "date": temp_list[2],
        "total_distance": temp_list[3],
        "total_engine_hours": temp_list[4],
        "total_fuel_consumption": temp_list[5]
    }
    return info_dict


def create_initial_dict(start_date, initial_distance, initial_engine_hours):
    initial_dict = {
        "date": start_date,
        "total_distance": initial_distance,
        "total_engine_hours": initial_engine_hours,
        "total_fuel_consumption": 0
    }
    return initial_dict
