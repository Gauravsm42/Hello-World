import random
# The random module contains functions for generating random numbers,
# picking random elements from lists, tuples, or strings, and more.

feet_in_mile = 5280
meter_in_km = 1000

def get_file_ext(filename):
    return filename[filename.index(".") + 1:]

def roll_dice(num):
    return random.randint(1, num)
