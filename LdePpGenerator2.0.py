from counting_annual_values import count_annual_values
from inputing_values import input_start_date, input_initial_values, ask_for_answer
from checking_values import check_all_values
from returning_messages import create_error_message, create_annual_value_message
from creating_dicts import new_start_values, create_dict, create_initial_dict
from checking_str_length import length_of_str, counting_mx_len_for_annual_values_table
from saving_to_files import create_output_folder, create_text_and_save, saving_to_files
from printing_logo import print_logo
from generating_menus import generate_input_menu

template = "templates/LdePpMsgTmp.txt"


def process_input_with_annual_values(curr_dict, dict_to_be_saved_list, lines):
    return_values_list = []
    len_list = []
    mx_distance_str_len = 0
    mx_engine_hours_str_len = 0
    counter = 1
    new_start_dict = new_start_values(curr_dict)
    start_date = input_start_date()
    do_you_want_to_input_initial_values = ask_for_answer("Do you want to input initial values(distance, engine_hours)?")
    if do_you_want_to_input_initial_values:
        initial_distance, initial_engine_hours = input_initial_values()
    else:
        initial_distance, initial_engine_hours = 0, 0
    prev_dict = create_initial_dict(start_date, initial_distance, initial_engine_hours)
    is_error, error_dict = check_all_values(prev_dict, curr_dict)
    if is_error:
        error_message = create_error_message(error_dict, counter)
        return_values_list.append((is_error, error_message))
        len_list.append(0)
    else:
        # no error
        annual_values_list = count_annual_values(prev_dict, curr_dict)
        curr_distance_str_len = length_of_str(annual_values_list[0])
        mx_distance_str_len = counting_mx_len_for_annual_values_table(curr_distance_str_len, mx_distance_str_len)
        curr_engine_hours_str_len = length_of_str(annual_values_list[1])
        mx_engine_hours_str_len = counting_mx_len_for_annual_values_table(curr_engine_hours_str_len, mx_engine_hours_str_len)
        len_list.append((curr_distance_str_len, curr_engine_hours_str_len))
        return_values_list.append((is_error, [counter] + annual_values_list))
        prev_dict = curr_dict
    counter += 1

    for line in lines[2:]:
        curr_dict = create_dict(line)
        dict_to_be_saved_list.append(curr_dict)
        is_error, error_dict = check_all_values(prev_dict, curr_dict)
        if is_error:
            error_message = create_error_message(error_dict, counter)
            return_values_list.append((is_error, error_message))
            len_list.append(0)
        else:
            annual_values_list = count_annual_values(new_start_dict, curr_dict)
            curr_distance_str_len = length_of_str(annual_values_list[0])
            mx_distance_str_len = counting_mx_len_for_annual_values_table(curr_distance_str_len, mx_distance_str_len)
            curr_engine_hours_str_len = length_of_str(annual_values_list[1])
            mx_engine_hours_str_len = counting_mx_len_for_annual_values_table(curr_engine_hours_str_len, mx_engine_hours_str_len)
            len_list.append((curr_distance_str_len, curr_engine_hours_str_len))
            return_values_list.append((is_error, [counter] + annual_values_list))
            prev_dict = curr_dict
            counter += 1
    for i in range(len(return_values_list)):
        is_error, message = return_values_list[i]
        len_tup = len_list[i]
        if is_error:
            print(message)
        else:
            print(create_annual_value_message(message, len_tup, mx_distance_str_len, mx_engine_hours_str_len))


def process_input_without_annual_values(dict_to_be_saved_list, lines):
    for line in lines[2:]:
        curr_dict = create_dict(line)
        dict_to_be_saved_list.append(curr_dict)
    return dict_to_be_saved_list


def process_input_general(template_1, inputs_1):
    with open(inputs_1) as o:
        lines = o.readlines()
    curr_dict = create_dict(lines[1])
    dict_to_be_saved_list = [curr_dict]
    do_you_want_to_count_annual_values = ask_for_answer("Do you want to count annual values?")
    if do_you_want_to_count_annual_values:
        process_input_with_annual_values(curr_dict, dict_to_be_saved_list, lines)
        do_you_want_to_save_to_files = ask_for_answer("Do you want to save to files?")
        if do_you_want_to_save_to_files:
            saving_to_files(dict_to_be_saved_list, template_1)
    else:
        # not counting annual values
        dict_to_be_saved_list = process_input_without_annual_values(dict_to_be_saved_list, lines)
        saving_to_files(dict_to_be_saved_list, template_1)


def process_input(template_1, inputs_1):
    with open(inputs_1) as o:
        lines = o.readlines()
        do_you_want_to_count_annual_values = ask_for_answer("Do you want to count annual values?")
        curr_dict = create_dict(lines[1])
        dict_to_be_saved_list = [curr_dict]

        if do_you_want_to_count_annual_values:
            return_values_list = []
            len_list = []
            mx_distance_str_len = 0
            mx_engine_hours_str_len = 0
            counter = 1
            new_start_dict = new_start_values(curr_dict)
            start_date = input_start_date()
            do_you_want_to_input_initial_values = ask_for_answer(
                "Do you want to input initial values(distance, engine_hours)?")
            if do_you_want_to_input_initial_values:
                initial_distance, initial_engine_hours = input_initial_values()
            else:
                initial_distance, initial_engine_hours = 0, 0
            prev_dict = create_initial_dict(start_date, initial_distance, initial_engine_hours)
            is_error, error_dict = check_all_values(prev_dict, curr_dict)
            if is_error:
                error_message = create_error_message(error_dict, counter)
                return_values_list.append((is_error, error_message))
                len_list.append(0)
            else:
                annual_values_list = count_annual_values(prev_dict, curr_dict)
                curr_distance_str_len = length_of_str(annual_values_list[0])
                if curr_distance_str_len > mx_distance_str_len:
                    mx_distance_str_len = curr_distance_str_len
                curr_engine_hours_str_len = length_of_str(annual_values_list[1])
                if curr_engine_hours_str_len > mx_engine_hours_str_len:
                    mx_engine_hours_str_len = curr_engine_hours_str_len
                len_list.append((curr_distance_str_len, curr_engine_hours_str_len))
                return_values_list.append((is_error, [counter] + annual_values_list))
                prev_dict = curr_dict
            counter += 1

        for line in lines[2:]:
            curr_dict = create_dict(line)
            dict_to_be_saved_list.append(curr_dict)

            if do_you_want_to_count_annual_values:
                is_error, error_dict = check_all_values(prev_dict, curr_dict)
                if is_error:
                    error_message = create_error_message(error_dict, counter)
                    return_values_list.append((is_error, error_message))
                    len_list.append(0)
                else:
                    annual_values_list = count_annual_values(new_start_dict, curr_dict)
                    curr_distance_str_len = length_of_str(annual_values_list[0])
                    if curr_distance_str_len > mx_distance_str_len:
                        mx_distance_str_len = curr_distance_str_len
                    curr_engine_hours_str_len = length_of_str(annual_values_list[1])
                    if curr_engine_hours_str_len > mx_engine_hours_str_len:
                        mx_engine_hours_str_len = curr_engine_hours_str_len
                len_list.append((curr_distance_str_len, curr_engine_hours_str_len))
                return_values_list.append((is_error, [counter] + annual_values_list))
                prev_dict = curr_dict
                counter += 1

        if do_you_want_to_count_annual_values:

            for i in range(len(return_values_list)):
                is_error, message = return_values_list[i]
                len_tup = len_list[i]
                if is_error:
                    print(message)
                else:
                    print(create_annual_value_message(message, len_tup, mx_distance_str_len, mx_engine_hours_str_len))
            # already in new functions
            do_you_want_to_save_to_files = ask_for_answer("Do you want to save to files?")
            if do_you_want_to_save_to_files:
                output_path = create_output_folder()
                for info_dict in dict_to_be_saved_list:
                    create_text_and_save(info_dict, template_1, output_path)
        else:
            print("Saving to files.")
            output_path = create_output_folder()
            for info_dict in dict_to_be_saved_list:
                create_text_and_save(info_dict, template_1, output_path)


print_logo()
inputs = generate_input_menu()
process_input_general(template, inputs)
answer = ask_for_answer("Do you want to process more files?")
while answer:
    print_logo()
    inputs = generate_input_menu()
    process_input_general(template, inputs)
    answer = ask_for_answer("Do you want to process more files?")
