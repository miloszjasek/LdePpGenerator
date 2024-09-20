from operating_on_dates import str_to_date


def reading_defaults(defaults_path):
    with open(defaults_path, "r") as df:
        defaults_list = df.readlines()
    initial_date = str_to_date(defaults_list[0])
    initial_distance, initial_engine_hours = int(defaults_list[1]), int(defaults_list[2])
    return initial_date, initial_distance, initial_engine_hours
