#! /usr/bin/python3

import datetime as dt
import os


def get_subtitles_from_file(file_path: str, file_encoding: str) -> list:
    with open(file_path, 'r', encoding=file_encoding) as original_srt_file:
        subtitles = list(original_srt_file.read().split('\n\n'))

    return subtitles


def remove_not_srt_file(file_list: list):
    for file_name in file_list:
        if file_name[-3:] != 'srt':
            file_list.remove(file_name)

    return file_list


def show_error_open_file(list_files: list):
    if list_files:
        list_files.insert(0, 'Color Subtitles could not open some files using encoding UTF-8 and Windows 1252.')
    for error_message in list_files:
        print(error_message)


start_time = dt.datetime.now()
file_path = 'resources'
file_list = remove_not_srt_file(os.listdir(file_path))
file_error_list = list()
print(f'There is {len(file_list)} file(s) to process...')
print()
processed_file_count = 0
for file_name in file_list:
    processed_file_count += 1
    print(f'Processing file {processed_file_count} from {len(file_list)}. File name: {file_name}')
    full_file_name = file_path + '/' + file_name
    try:
        subtitle = get_subtitles_from_file(full_file_name, 'UTF8')
    except UnicodeDecodeError:
        try:
            subtitle = get_subtitles_from_file(full_file_name, 'windows 1252')
        except UnicodeDecodeError:
            file_error_list.add(file_name)

    with open(file_name, 'w+') as new_srt_file:
        for subtitle_line in subtitle:
            line = list(subtitle_line.splitlines())
            for i in range(0, len(line)):
                if i < 2:
                    new_srt_file.write(line[i])
                else:
                    new_srt_file.write("<font color=#ffff00>")
                    new_srt_file.write(line[i])
                    new_srt_file.write("</font>")
                new_srt_file.write('\n')
            new_srt_file.write('\n')
    processed_file_count += 1

end_time = dt.datetime.now()
show_error_open_file(file_error_list)
print(f'Processed in: {(end_time - start_time)}')
