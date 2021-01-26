import datetime as dt
import chardet


def get_file_encoding(src_file_path):
    """
    Get the encoding type of a file
    :param src_file_path: file path
    :return: str - file encoding type
    """

    with open(src_file_path) as src_file:
        return src_file.encoding


# file = open("The.Rookie.srt", "r", encoding="windows 1252")
file_name = 'the.neighborhood.s03e05.720p.web.h264-ggwp.srt'
file_path = 'resources/'
file_encoding = get_file_encoding(file_path+file_name)
# file_encoding = "UTF8"
# start_time = dt.datetime.now()

with open(file_path + file_name, "r", encoding=file_encoding) as original_srt_file:
    new_list = list(original_srt_file.read().split('\n\n'))

with open(file_name, "w+") as new_srt_file:
    for subtitle_line in new_list:
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
