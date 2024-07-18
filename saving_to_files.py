from operating_on_dates import date_to_str
import os
import datetime


def copy_from_file(file_name):
    txt_file = open(file_name, "r")
    data = txt_file.read()
    txt_file.close()
    return data


def replace_value(message, name_to_replace, value):
    message = message.replace(name_to_replace, value)
    return message


def replace_date(message, name_to_replace, date):
    date += "T05:00:00.000Z"
    message = replace_value(message, name_to_replace, date)
    return message


def create_text_and_save(info_dict, template, output_path):
    date = date_to_str(info_dict["date"])
    chassis_series = str(info_dict["chassis_series"])
    chassis_number = str(info_dict["chassis_number"])
    message = copy_from_file(template)
    message = replace_value(message, "CHASSIS_SERIES", chassis_series)
    message = replace_value(message, "CHASSIS_NUMBER", chassis_number)
    message = replace_value(message, "TOTAL_DISTANCE", info_dict["total_distance"])
    message = replace_value(message, "TOTAL_ENGINE", info_dict["total_engine_hours"])
    message = replace_value(message, "TOTAL_FUEL", info_dict["total_fuel_consumption"].strip("\n"))
    message = replace_date(message, "MSG_DATE", date)
    save_to_file(message, output_path, chassis_series, chassis_number, date)


def create_output_folder():
    current_time = datetime.datetime.now()
    folder_name = str(datetime.datetime.now())[:19].replace(" ", "__").replace(":", "_")
    folder_path = "outputs/" + folder_name
    print("Output files located in folder : " + folder_path)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    return folder_path


def save_to_file(message, output_path, chassis_series, chassis_number, date):
    file_name = output_path + "/" + chassis_series + chassis_number + "_" + date + ".txt"
    with open(file_name, "w") as file:
        file.write(message)
