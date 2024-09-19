import datetime


def input_start_date():
    print("Please type in start date(YYYY-MM-DD).")
    date_str = input()
    temp_list = date_str.split("-")
    start_time = datetime.date(int(temp_list[0]), int(temp_list[1]), int(temp_list[2]))
    return start_time


def input_initial_values():
    initial_distance = input_initial_value("distance")
    initial_engine_hours = input_initial_value("engine hours")
    return initial_distance, initial_engine_hours


def input_initial_value(value_name):
    print(f"input initial {value_name}")
    value = input()
    return int(value)


def ask_for_answer(question):
    print(question)
    print("If yes type in \"y\", else type in \"n\".")
    answer = input()
    while answer != "y" and answer != "n":
        print("Please type in proper answer.")
        answer = input()
    if answer == "y":
        return True
    else:
        return False


def ask_for_number(number_set):
    answer = input()
    while answer not in number_set:
        print("Please type in proper answer.")
        answer = input()
    return int(answer)
