#! /usr/bin/python3

import datetime as dt
import os

SUBTITLE_COLOR_YELLOW = '#ffff00'
OUTPUT_DIRECTORY = 'output'
RESOURCES_DIRECTORY = 'resources'


def __get_subtitles_from_file(file_path: str, file_encoding: str) -> list:
    with open(file_path, 'r', encoding=file_encoding) as original_srt_file:
        subtitles = list(original_srt_file.read().split('\n\n'))

    return subtitles


def __list_srt_files():
    subtitle_files = list()
    for file_name in os.listdir(RESOURCES_DIRECTORY):
        if file_name.endswith('srt'):
            subtitle_files.append(file_name)

    return subtitle_files


def __show_error_open_file(list_files: list):
    list_files.insert(0, 'Color Subtitles could not open some files using encoding UTF-8 and Windows 1252.')
    for error_message in list_files:
        print(error_message)


def main():
    start_time = dt.datetime.now()
    try:
        subtitle_files = __list_srt_files()
        file_error_list = list()
        print(f'There is {len(subtitle_files)} file(s) to process...')
        print()
        for file_number, file_name in enumerate(subtitle_files):
            print(f'Processing file {file_number + 1} from {len(subtitle_files)}. File name: {file_name}')
            full_file_name = RESOURCES_DIRECTORY + '/' + file_name
            try:
                subtitle = __get_subtitles_from_file(full_file_name, 'UTF8')
            except UnicodeDecodeError:
                try:
                    subtitle = __get_subtitles_from_file(full_file_name, 'windows 1252')
                except UnicodeDecodeError:
                    file_error_list.add(file_name)

            __generate_colored_subtitles(file_name, subtitle)
    finally:
        end_time = dt.datetime.now()

    if file_error_list:
        __show_error_open_file(file_error_list)

    print(f'Processed in: {(end_time - start_time)}')


def __generate_colored_subtitles(file_name, subtitle):
    with open(OUTPUT_DIRECTORY + '/' + file_name, 'w+') as new_srt_file:
        for subtitle_line in subtitle:
            line = list(subtitle_line.splitlines())
            for i in range(0, len(line)):
                if i < 2:
                    new_srt_file.write(line[i])
                else:
                    new_srt_file.write(f"<font color={SUBTITLE_COLOR_YELLOW}>")
                    new_srt_file.write(line[i])
                    new_srt_file.write("</font>")
                new_srt_file.write('\n')
            new_srt_file.write('\n')


if __name__ == '__main__':
    main()
