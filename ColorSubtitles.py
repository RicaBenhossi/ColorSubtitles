import datetime as dt


def get_subtitles_from_file(file_path: str, file_encoding: str) -> list:
    with open(file_path, 'r', encoding=file_encoding) as original_srt_file:
        subtitles = list(original_srt_file.read().split('\n\n'))

    return subtitles


file_name = 'Magnum.P.I.2018.S03E06.720p.HEVC.x265-MeGusta.srt'
file_path = 'resources/'
start_time = dt.datetime.now()

try:
    subtitle = get_subtitles_from_file(file_path + file_name, 'UTF8')
except UnicodeDecodeError:
    print('Could not open file using UTF-8 encoding. Trying with encoding windows 1252.')
    try:
        subtitle = get_subtitles_from_file(file_path + file_name, 'windows 1252')
    except UnicodeDecodeError:
        print('Error on openning file using windows 1252 encoding.')
        print('Check if the encoding of the file is UTF-8 or Windows 1252.')
        exit()

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

end_time = dt.datetime.now();
print(end_time - start_time)
