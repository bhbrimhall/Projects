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


def wc(files):
    """print newline, word, and byte counts for each file"""

    total_lines = 0
    total_words = 0
    total_characters = 0

    for file in files:
        file = open(file)

        total_lines += len(file.readlines())
        file.seek(0)
        print(len(file.readlines()), end='\t')
        file.seek(0)

        total_words += len(file.read().split())
        file.seek(0)
        print(len(file.read().split()), end='\t')
        file.seek(0)

        total_characters += len(file.read())
        file.seek(0)
        print(len(file.read()), end='\t')
        print(file.name)
        file.close()

    if len(files) > 1:
        print(str(total_lines) + "\t" + str(total_words) + "\t" + str(total_characters) + "\ttotal")
