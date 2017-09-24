#!/usr/bin/env python
"""
    wunderground_avg.py -- Calculate city's average, max, min temperature and standard deviation
    Author: Qi Meng Qi.meng810@gmail.com
    Last modified: 09.21.2017
"""

import sys                            # import the 'system' library

SKIP_LINE = 1  # Mark number of lines to skip in reading file

try:
    city_arg = ''.join(sys.argv[1:])   # Take the argument from Command Line, and remove space
except IndexError:
    exit('error: invalid input')


def validate_input():
    """ Validate the city input """

    city_input = str(city_arg.lower())
    if city_input == 'chicago':
        city = 'Chicago'
    elif city_input == 'honolulu':
        city = 'Honolulu'
    elif city_input == 'losangeles':
        city = 'Los Angeles'
    elif city_input == 'newyork':
        city = 'New York'
    else:
        print('Please enter a valid city')
        exit(0)
    return city

def acquire_data(city):
    """ Based on the city input, acqure data from corresponding csv file,
    and create the city temperature data list """

    city_name = city.replace(' ','').lower()
    file_name = 'weather_' + city_name + '.csv'
    file = open('C:/Andrew/Python/python_data/ALL_DATA/python_data/'  + file_name  )
    file_lines_list = file.readlines()  # Create a list of lines in the file
    #print(file_lines_list)
    valid_lines = file_lines_list[SKIP_LINE:]   # Skip the first row
    #print(valid_lines)
    valid_list = []
    for line in valid_lines:
        line_list = line.split(',')
        element = line_list[2]          # Use the 3rd column, which is the Mean Temperature
        float_element = float(element)  # change str to float variable
        valid_list.append(float_element)
    return valid_list

def calculate_avg_min_max(valid_list):
    """ Calulate the average, min and max temperature from valid_list """
    temp_average = sum(valid_list)/len(valid_list)
    temp_max =int(max(valid_list))       # Change float to int
    temp_min = int(min(valid_list))      # Change float to int
    total = len(valid_list)


    cal = 0
    cal_sum = 0

    for tem in valid_list:
        cal = (tem - temp_average) ** 2
        cal_sum = cal + cal_sum
    var = cal_sum/total            #Calculating the variance
    std_dev = var ** (0.5)

    return temp_average, temp_max, temp_min, std_dev

def report_temps(city, temp_average, temp_max, temp_min, std_dev):
    """ Based on the calculation results, create format to generate report """
    format1 = 'Summary of daily temperature data for {} in year 2016:'.format(city)
    format2 = 'Average temp: {}'.format(temp_average)
    format3 = 'Max temp: {}'.format(temp_max)
    format4 = 'Min temp: {}'.format(temp_min)
    format5 = 'Standard deviation: {}'.format(std_dev)
    print(format1)
    print(format2)
    print(format3)
    print(format4)
    print(format5)

def main():
    city = validate_input()
    valid_list = acquire_data(city)
    temp_average, temp_max, temp_min, std_dev = calculate_avg_min_max(valid_list)

    report_temps(city, temp_average, temp_max, temp_min, std_dev)


if __name__ == '__main__':

    main()
    exit(0)   # exit, signaling no error
