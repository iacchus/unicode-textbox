#!/usr/bin/env python3

import sys, os

top_left_char = horizontal_char = top_right_char = vertical_char =\
        bottom_left_char = bottom_right_char = '+'

NEWLINE = '\n'

def last_line_size(text_str):
    return len(text_str.splitlines()[-1].expandtabs())

linelist = list(sys.stdin)

#def textbox(inner_size, text):


# gets the biggest line
biggest_line_size = 0
for line in linelist:
    line_lenght = len(line.expandtabs().strip(NEWLINE))
    if line_lenght > biggest_line_size:
        biggest_line_size = line_lenght

no_of_lines = len(linelist)

padsize = 1
padding = ' ' * padsize # space char

text = str()

box_cols = 1 + padsize + biggest_line_size + padsize + 1

for line_num, line in enumerate(linelist):

    # first box line
    if line_num ==  0:
        text += top_left_char
        text += horizontal_char * (1+biggest_line_size+1)  # padding
        text += top_right_char
        text += NEWLINE

    if line.strip(' ') != '':
        text += vertical_char
        text += padding
        #text += line.strip(' ')
        text += line.strip(NEWLINE).expandtabs()
        text += padding
        extra_pad = ' ' *  (biggest_line_size - last_line_size(text))
        #print(last_line_size(text))
        text += extra_pad
        text += vertical_char
        text += NEWLINE

    if line_num +1 == no_of_lines:
        text += bottom_left_char
        text += horizontal_char * (1+biggest_line_size+1)  # padding
        text += bottom_right_char
        text += NEWLINE

#divider = spacing + ('─' * int(biggest_line_size)) # unicode 0x2500
#text += divider

print(text, end="\n"*2)

