#!/usr/bin/env python3    # make sure this is the very first line, flush left!
"""
    Aggregate_bitly.py
    --
    1. Find unique cities in the bitly data, sorted by name
    2. Create a dictory based on bitly country_code data, find top ten country_code value
    3. Find top 10 machine_name values from bity data
    Author: Qi Meng
    Last modified 09.23.2017
"""


FILE =  open('/Users/Andrew/Documents/python/python_data/python_data/bitly.tsv').readlines()[1:]
BITLY_DATA = FILE[1:]

# Create the data list, skipping the first row

""""
I created the column name index for reference

for count, line in enumerate(FILE[0].split(),1):
    print(count, line)

0 timestamp
1 user_agent
2 referring_url
3 short_url_cname
4 long_url
5 geo_city_name
6 country_code
7 geo_region
8 accept_language
9 timezone
10 lat
11 long

"""

# The program starts here


def city_sort():
    """ Create a set and sort the set based on city names """
    city_set = set()     # initiate a blank set
    for line in BITLY_DATA:
        city_name = line.rstrip('\n').split("\t")[5]
        city_set.add(city_name)   # add data into set
    city_name_sorted = sorted(city_set)
    print(city_name_sorted)
#city_sort()

def country_code_sort():
    """ Create a dictory based on the country_code,
     and find the top 10 city_code based on key values """


    country_code_dict = dict()  # initiate a blank dictionary
    for line in BITLY_DATA:
        country_code = line.rstrip('\n').split("\t")[6]
        if country_code not in country_code_dict:
            country_code_dict[country_code] = 0
        country_code_dict[country_code] = country_code_dict[country_code] + 1
    country_code_sorted = sorted(country_code_dict, key = country_code_dict.get)[0:9]
    print(country_code_sorted)

#country_code_sort()


def machine_name_sort():
    """ Create a dictroy based on machine_name,
    and find the top 10 machine_name based on key values """

    machine_name_dict = dict()   # initiate a blank dictionary
    for line in BITLY_DATA:
        long_url = line.rstrip('\n').split("\t")[4]
        machine_name = long_url.split('/')[2].replace('www.','')
        if machine_name not in machine_name_dict:
            machine_name_dict[machine_name] = 0
        machine_name_dict[machine_name] = machine_name_dict[machine_name] + 1
    machine_name_sorted = sorted(machine_name_dict, key = machine_name_dict.get)[0:9]
    print(machine_name_sorted)



def main():
    city_sort()
    country_code_sort()
    machine_name_sort()


if __name__ == '__main__':

    main()
    exit(0)   # exit, signaling no error
