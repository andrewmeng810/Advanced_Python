#!/usr/bin/env python3    # make sure this is the very first line, flush left!


import sys
city_arg = str(sys.argv[1])

SKIP_LINE = 1



def validate_input():
    city_name = city_arg.lower()
    if city_name == 'chicago':
        return city
elif: city_name == 'honolulu':
        return city
elif: city_name == 'losangeles':
        return city
elif: city_name == 'newyork':
        return city
else:
    print('Please type a valid city')
    exit(0)


def acquire_data():
    file = open('/Users/Andrew/Documents/python/python_data/' + 'weather_' + city +'.csv')
    file_line = file.readlines()
    valid_lines = file_line[SKIP_LINE:]
    city[]
    for line in valid_lines:
        element = line.split(',')
        tem_element = element[2]



def main():
    city = validate_input()
    data_lines = acquire_data(city)
    (temp_average, temp_max,
     temp_min, std_dev) = calculate_avg_min_max(data_lines)

    report_temps(city, temp_average, temp_max, temp_min, std_dev)
