import datetime
from counting_annual_values import count_annual_values_new
from imputing_values import input_start_date, input_initial_values, ask_for_answer
from checking_values import check_all_values
from returning_messages import create_error_message


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


def proces_input():
    outputPath = createOutputFolder()
    with open(inputs) as o:
        lines = o.readlines()
        print("Do you want to count annual values?")
        do_you_want_to_count_annual_values = ask_for_answer()
        counter = 1
        curr_dict = create_dict(lines[1])
        return_values_list = []
        dict_to_be_saved_list = [curr_dict]
        if do_you_want_to_count_annual_values:
            start_date = input_start_date
            print("Do you want to input initial values(distance, engine_hours)?")
            do_you_want_to_input_initial_values = ask_for_answer()
            initial_distance, initial_engine_hours = input_initial_values()
            prev_dict = {
                "date": start_date,
                "total_distance": initial_distance,
                "total_engine_hours": initial_engine_hours,
                "total_fuel_consumption": 0
            }
            is_error, error_dict = check_all_values(prev_dict, curr_dict)
            if is_error:
                error_message = create_error_message(error_dict, counter)
                return_values_list.append(error_message)
            else:
                return_values_list.append(count_annual_values(prev_dict, curr_dict))
            counter += 1




        for line in lines[2:]:
            curr_info_dict = create_dict(line)
            if do_you_want_to_count_annual_values:
            #function required







        if answer:
            start_date = input_start_date_new()
            print("Do you want to input initial values (distance, engine_hours)?")
            answer = ask_for_answer()
            if answer:
                start_distance, start_engine_hours = input_initial_values()
            else:
                start_distance, start_engine_hours = 0, 0
            prev_info_dict = {
                "date": start_date,
                "total_distance": start_distance,
                "total_engine_hours": start_engine_hours,
                "total_fuel_consumption": 0
            }
            curr_info_dict = create_dict(lines[1])
            is_error, error_dict = check_all_values(prev_info_dict, curr_info_dict)
            new_start_date, new_start_distance, new_start_engine_hours, new_start_fuel = new_start_values(
                curr_info_dict)
            counter = 1
            if not is_error:
                yearly_km, yearly_engine_hours, average_fuel_consumption_per_100_km = count_annual_values(start_date,
                                                                                                          curr_info_dict[
                                                                                                              "date"],
                                                                                                          curr_info_dict[
                                                                                                              "total_distance"],
                                                                                                          start_distance,
                                                                                                          curr_info_dict[
                                                                                                              "total_engine_hours"],
                                                                                                          start_engine_hours,
                                                                                                          curr_info_dict[
                                                                                                              "total_fuel_consumption"],
                                                                                                          0)
                print(str(counter) + "." + date_to_str(curr_info_dict["date"]) + " annual distance(km): " + str(
                    yearly_km) + " | annual engine hours: " + str(
                    yearly_engine_hours) + " | average fuel consumption per 100 km: " + str(
                    average_fuel_consumption_per_100_km))
                prev_info_dict = curr_info_dict
            else:
                print(create_error_message(error_dict, counter))
            counter += 1
            for line in lines[2:]:
                curr_info_dict = create_dict(line)
                is_error, error_dict = check_all_values(prev_info_dict, curr_info_dict)
                if not is_error:
                    yearly_km, yearly_engine_hours, average_fuel_consumption_per_100_km = count_annual_values(
                        new_start_date, curr_info_dict["date"], curr_info_dict["total_distance"], new_start_distance,
                        curr_info_dict["total_engine_hours"], new_start_engine_hours,
                        curr_info_dict["total_fuel_consumption"], new_start_fuel)
                    print(str(counter) + "." + date_to_str(curr_info_dict["date"]) + " annual distance(km): " + str(
                        yearly_km) + " | annual engine hours: " + str(
                        yearly_engine_hours) + " | average fuel consumption per 100 km: " + str(
                        average_fuel_consumption_per_100_km))
                    prev_info_dict = curr_info_dict
                else:
                    print(create_error_message(error_dict, counter))
                counter += 1
        print("Do you want to save to files?")
        answer = ask_for_answer()
        if answer:
            for line in lines[1:]:
                # tmp, info_dict["chassis_series"], info_dict["chassis_number"], date = save_into_file_new(line)
                line = line.replace("\n", "")
                inTab = line.split(",")
                # print(inTab)
                tmp = readFile(tempalte)
                tmp = replaceValue(tmp, "CHASSIS_SERIES", inTab[0])
                tmp = replaceValue(tmp, "CHASSIS_NUMBER", inTab[1])
                tmp = replaceDate(tmp, "MSG_DATE", inTab[2])
                tmp = replaceValue(tmp, "TOTAL_DISTANCE", inTab[3])
                tmp = replaceValue(tmp, "TOTAL_ENGINE", inTab[4])
                tmp = replaceValue(tmp, "TOTAL_FUEL", inTab[5])
                date = inTab[2].replace("-", "_")
                saveOutputFile(tmp, outputPath, inTab[0], inTab[1], date)

print(count_differences_in_total_value(100,10))