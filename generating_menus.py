import os
from inputing_values import ask_for_number


def generate_input_folder_list():
    current_directory = os.path.dirname(os.path.abspath(__file__))
    folder_path = os.path.join(current_directory, 'inputs')
    return os.listdir(folder_path), folder_path


def create_str_input_folder_list(input_folder_list):
    str_list = ""
    num_set = set()
    for number, name in enumerate(input_folder_list):
        str_list += str(number) + ". " + str(name) + "\n"
        num_set.add(str(number))
    return str_list, num_set


def generate_input_menu():
    input_folder_list, folder_path = generate_input_folder_list()
    str_list, num_set = create_str_input_folder_list(input_folder_list)
    more_than_one_file = len(input_folder_list) > 1
    if more_than_one_file:
        menu_message = "Please type in the number corresponding to the file you want to process." + "\n" + str_list
        print(menu_message)
        number = ask_for_number(num_set)
        file_name = input_folder_list[number]
        file_path = os.path.join(folder_path, file_name)
    else:
        menu_message = "Found one file, proceeding to process it"
        print(menu_message)
        file_name = input_folder_list[0]
        file_path = os.path.join(folder_path, file_name)
    return file_path

