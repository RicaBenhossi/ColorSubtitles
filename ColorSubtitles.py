# file = open("The.Rookie.srt", "r", encoding="windows 1252")
file = open("resources/The.Rookie.S03E02.1080p.HEVC.x265-MeGusta.srt", "r", encoding="windows 1252")
output = open("subtitle.srt", "w+")

for line in file:
    try:
        int(str(line[0]))
        output.write(line)
    except Exception:
        if line not in ('\n', '\r\n'):
            line_str = line
            output.write("<font color=#ffff00>")
            output.write(line_str)
            output.write("</font>")
        else:
            output.write(line)
