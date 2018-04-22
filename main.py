#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Hour Calculator

Quickly made hour calculator for 24h day clock to prevent the need of relying
on a website for simple time calculations. Does the work; enter timestamps,
shows results in a table of elapsed time and total hours.
"""

import datetime
import sys
import os

__title__ = "Hour Calculator"
__author__ = "Philip Andersen <philip.andersen@codeofmagi.net>"
__license__ = "MIT"
__version__ = "1.0"
__copyright__ = "Copyright 2018 (c) Philip Andersen"


def clear_screen():
    return os.system('cls' if os.name == 'nt' else 'clear')


def format_timedelta(time):
    minutes, seconds = divmod(time.seconds + time.days * 86400, 60)
    hours, minutes = divmod(minutes, 60)
    return '{:d}:{:02d}:{:02d}'.format(hours, minutes, seconds)


def get_interger(string):
    while True:
        try:
            return int(input(string))
        except ValueError:
            print('Not a valid number\n')
            continue
        break


def get_timestamps(times, time_format='%H:%M'):
    timestamps = {}
    for time in range(0, times):
        while True:
            try:
                print("\nTimestamp {} ({})".format(time+1, time_format))
                start = datetime.datetime.strptime(
                    input("- Start: "),
                    time_format
                )
                end = datetime.datetime.strptime(
                    input("- End:   "),
                    time_format
                )
                timestamps[time+1] = [start, end, end-start]
            except ValueError as time_error:
                print(time_error)
                continue
            break
    return timestamps


def get_total_hours(timestamps):
    return format_timedelta(
        sum([y[2] for x, y in timestamps.items()], datetime.timedelta())
    )


def print_table(timestamps, time_format='%H:%M'):
    clear_screen()
    print('='*40)
    print(' #    Start    End        Time elapsed')
    print('='*40)
    for x, y in timestamps.items():
        print(" {}    {}    {}      {}".format(
            x,
            y[0].strftime(time_format),
            y[1].strftime(time_format),
            y[2]
        ))
    print('='*40)
    print(' TOTAL HOURS:             {}\n'.format(get_total_hours(timestamps)))


def main():
    # Just added for time saving sake, not that pretty.
    if len(sys.argv) > 1:
        try:
            print_table(get_timestamps(int(sys.argv[1])))
        except:
            print('Not a valid number')
            print_table(get_timestamps(get_interger("How many days?: ")))
    else:
        print_table(get_timestamps(get_interger("How many days?: ")))


if __name__ == "__main__":
    main()
