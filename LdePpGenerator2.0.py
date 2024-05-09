import datetime
from counting_annual_values import count_annual_values
from inputing_values import input_start_date, input_initial_values, ask_for_answer
from checking_values import check_all_values
from returning_messages import create_error_message, create_annual_value_message
from creating_dicts import new_start_values, create_dict, create_initial_dict
from checking_str_length import length_of_str
from saving_to_files import create_output_folder, create_text_and_save
from printing_logo import print_logo

template = "templates/LdePpMsgTmp.txt"
inputs = "inputs/InsertData.txt"


def proces_input(template, inputs):
    with open(inputs) as o:
        lines = o.readlines()
        print("Do you want to count annual values?")
        do_you_want_to_count_annual_values = ask_for_answer()
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
            print("Do you want to input initial values(distance, engine_hours)?")
            do_you_want_to_input_initial_values = ask_for_answer()
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

            print("Do you want to save to files?")
            do_you_want_to_save_to_files = ask_for_answer()
            if do_you_want_to_save_to_files:
                output_path = create_output_folder()
                for info_dict in dict_to_be_saved_list:
                    create_text_and_save(info_dict, template, output_path)
        else:
            print("Saving to files.")
            output_path = create_output_folder()
            for info_dict in dict_to_be_saved_list:
                create_text_and_save(info_dict, template, output_path)


print_logo()
proces_input(template, inputs)
