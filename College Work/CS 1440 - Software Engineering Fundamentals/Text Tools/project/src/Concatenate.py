#              Copyright © 2023 DuckieCorp. All Rights Reserved.
#
#                       __      Redistribution and use of this code, with or
#                     /` ,\__   without modification, are permitted provided
#                    |    ).-'  that the following conditions are met:
#                   / .--'
#                  / /          0. Redistributions of this code must retain
#    ,      _.==''`  \             the above copyright notice, this list of
#  .'(  _.='         |             conditions and the following disclaimer.
# {   ``  _.='       |          1. The name of the author may not be used to
#  {    \`     ;    /              endorse or promote products derived from
#   `.   `'=..'  .='               this software without specific prior written
#     `=._    .='                  permission.
#  jgs  '-`\\`__                2. Neither the name of the University nor the
#           `-._{                  names of its contributors may be used to
#                                  endorse or promote products derived from
#                                  this software without specific prior written
#                                  permission.


def cat(args):
    """concatenate files and print on the standard output"""

    for file in args:
        f = open(file)
        for line in f:
            print(line, end='')

        f.close()


def tac(args):
    """concatenate and print files in reverse"""

    for file in args:
        f = open(file)
        lines = []
        for line in f:
            lines.append(line)
        lines = reversed(lines)
        for line in lines:
            print(line, end='')
        f.close()

