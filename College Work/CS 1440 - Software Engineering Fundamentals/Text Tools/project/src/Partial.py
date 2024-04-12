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


def head(args):
    """output the first part of files"""

    num_of_lines = 10

    if args[0] == "-n":
        args.pop(0)
        num_of_lines = int(args[0])
        args.pop(0)

    for file in args:
        file = open(file)

        if len(args) > 1:
            print("==> " + file.name + " <==")

        iterator = 0
        for line in file:
            if iterator == num_of_lines:
                break
            print(line, end="")
            iterator += 1
        print()
        file.close()



def tail(args):
    """output the last part of files"""

    num_of_lines = 10

    if args[0] == "-n":
        args.pop(0)
        num_of_lines = int(args[0])
        args.pop(0)

    for file in args:
        file = open(file)

        if len(args) > 1:
            print("==> " + file.name + " <==")

        iteration = 0
        total_lines = len(file.readlines())
        file.seek(0)
        for line in file:
            if total_lines - iteration <= num_of_lines:
                print(line, end='')
            iteration += 1
        print()
        file.close()
