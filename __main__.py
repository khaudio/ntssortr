#!/usr/bin/env python

import datetime
import sys
import json


def open_file_as_text(filename: str):
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            yield line


def timestamp_to_datetime(timestamp: str):
    if not timestamp:
        return
    return datetime.datetime.strptime(
            timestamp.replace('\u202f', ' '),
            '%m/%d/%Y %I:%M %p'
        )


def process_csv_as_text(filepath):
    timestamp, buff = '', ''
    for index, line in enumerate(open_file_as_text(filepath)):
        if '\u202f' in line:
            yield index - 1, timestamp_to_datetime(timestamp), buff
            timestamp = line.split(',')[0]
            buff = line.lstrip(timestamp).lstrip(',')
        else:
            buff += line
    yield index - 1, timestamp_to_datetime(timestamp), buff

def main():
    processor = process_csv_as_text(sys.argv[1])
    _ = next(processor) # Skip column labels
    data = dict()
    for index, timestamp, message in processor:
        data[index] = [timestamp.strftime('%Y-%m-%d %H:%M'), message]
        print(index, timestamp, message)
    json.dump(data, open('data.json', 'w'), indent=4)


if __name__ == '__main__':
    main()

