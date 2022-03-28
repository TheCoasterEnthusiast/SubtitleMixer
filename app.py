"""
Current goals for SubtitleMixer:
1. Combine srt files
2. Adjust timings for subtitles
"""
import re

DEFAULT_FILE_NAME = 'combined_subtitles.srt'


def create_subtitle_list(lines: list) -> list[list]:
    subtitle_list = [[]]
    for line in lines:
        if line == '\n':
            subtitle_list.append([])
        else:
            subtitle_list[-1].append(line)
    return subtitle_list


def is_subtitle(line: str) -> bool:
    if re.search('[a-zA-Z]', line):
        return True
    return False


def read_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        return lines


def combine_subtitles(srt_name_1: str, srt_name_2: str):

    srt_1_lines = read_file(srt_name_1)
    srt_2_lines = read_file(srt_name_2)

    subtitle_list_1 = create_subtitle_list(srt_1_lines)
    subtitle_list_2 = create_subtitle_list(srt_2_lines)

    # searches for lines with text, and appends them to the first subtitle list
    for index, subtitle in enumerate(subtitle_list_2):
        for element in subtitle:
            if is_subtitle(element):
                subtitle_list_1[index].append(element)

    for subtitle in subtitle_list_1:
        subtitle.append('\n')

    with open(DEFAULT_FILE_NAME, 'w') as file:
        for subtitle in subtitle_list_1:
            file.writelines(subtitle)


def main():
    running = True

    while running:
        user_input = input("""Would you like to:
        1 - Combine subtitles
        2 - Adjust subtitle timings
        q - Quit
        """)

        if user_input == 'q':
            running = False


#main()
combine_subtitles("english.srt", "spanish.srt")
