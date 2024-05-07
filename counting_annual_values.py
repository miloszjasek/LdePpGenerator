import datetime


def count_annual_values(prev_dict, curr_dict):
    amount_of_days = count_days(prev_dict["date"], curr_dict["date"])
    diff_km = count_differences_in_total_value(prev_dict["total_distance"], curr_dict["total_distance"])
    yearly_km = count_yearly_values_for_km_and_engine_hours(amount_of_days, diff_km)
    diff_engine_hours = count_differences_in_total_value(prev_dict["total_engine_hours"], curr_dict["total_engine_hours"])
    yearly_engine_hours = count_yearly_values_for_km_and_engine_hours(amount_of_days, diff_engine_hours)
    diff_fuel = count_differences_in_total_value(prev_dict["total_fuel_consumption"], curr_dict["total_fuel_consumption"])
    average_fuel_consumption_per_100_km = count_average_fuel_consumption_per_100_km(diff_fuel, diff_km)
    return [int(yearly_km), int(yearly_engine_hours), round(average_fuel_consumption_per_100_km, 1), curr_dict["date"]]


def count_yearly_values_for_km_and_engine_hours(amount_of_days, value_difference):
    value_per_day = value_difference / amount_of_days
    yearly_value = value_per_day * 365
    return yearly_value


def count_average_fuel_consumption_per_100_km(fuel_consumption_difference, distance_difference):
    average_fuel_consumption_per_100_km = fuel_consumption_difference / distance_difference * 100
    return average_fuel_consumption_per_100_km


def count_differences_in_total_value(prev_total_value, curr_total_value):
    return int(curr_total_value) - int(prev_total_value)


def count_days(first_date, second_date):
    days_between = second_date - first_date
    return days_between.days
