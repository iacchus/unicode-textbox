#!/usr/bin/env python3

import sys, os

#top_left_char = horizontal_char = top_right_char = vertical_char =\
#        bottom_left_char = bottom_right_char = '+'

# https://en.wikipedia.org/wiki/Box-drawing_character
CHARS = { 'hz': '\u2500',
          've': '\u2502',
          'tl': '\u250c',
          'tr': '\u2510',
          'bl': '\u2514',
          'br': '\u2518' }

NEWLINE = '\n'

PAD_SIZE = 1
# def last_line_size(text_str):
#     return len(text_str.splitlines()[-1].expandtabs())

linelist = list(sys.stdin)
LINES = [line.expandtabs().strip('\n') for line in linelist]

TEXT_WIDTH = max(map(len, LINES))
#no_of_lines = len(lines)

PAD_CHAR = '\u0020' * PAD_SIZE  # space char

PROCESS_LINES_ARGS = (TEXT_WIDTH, PAD_SIZE, PAD_CHAR, CHARS['ve'])

#text = str()
#output = list()
HZ_LINE_WIDTH = TEXT_WIDTH + (PAD_SIZE * 2)
TOP_LINE = (CHARS['tl'] + CHARS['hz']*HZ_LINE_WIDTH + CHARS['tr'])

BOTTOM_LINE = (CHARS['bl'] + CHARS['hz']*HZ_LINE_WIDTH + CHARS['br'])


def process_line(line, text_width, pad_size, pad_char, ve_char):

    padding = pad_char * pad_size
    extra_padding = pad_char * (text_width - len(line))

    return ve_char + padding + line + extra_padding + padding + ve_char

text_list = [process_line(line, *PROCESS_LINES_ARGS) for line in LINES]
TEXT = str('\n').join(text_list)
box_parts = [TOP_LINE, TEXT, BOTTOM_LINE]
box = str('\n').join(box_parts)
#for line_num, line in enumerate(LINES):

    # first box line
    #if line_num ==  0:
    #    output.append(TOP_LINE)

    #text = process_line(line, *PROCESS_LINES_ARGS)
    #output.append(text)

    #if line_num + 1 == no_of_lines:
    #    output.append(BOTTOM_LINE)


#text = "\n".join(output)
# print(text, end="\n"*2)
print(box, end="\n"*2)

