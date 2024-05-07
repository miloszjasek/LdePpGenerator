from operating_on_dates import date_to_str
str(counter) + "." + date_to_str(curr_info_dict["date"]) + " annual distance(km): " + str(yearly_km) + " | annual engine hours: " + str(yearly_engine_hours) + " | average fuel consumption per 100 km: " + str(average_fuel_consumption_per_100_km)


def create_error_message(error_dict, counter):
    temp_str = str(counter) + ".Inconsistent input data in "
    for key in error_dict:
        temp_tuple = error_dict[key]
        prev_value = temp_tuple[0]
        curr_value = temp_tuple[1]
        temp_str += key + " : " + str(prev_value) + " > " + str(curr_value) + " "
    return temp_str


def create_annual_value_message(values_list):
    temp_str = str(counter) + ". "
    for value in values_list:
