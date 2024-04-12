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


def cut(args):
    """remove sections from each line of files"""
    keep = [1]
    if args[0] == "-f":
        keep = []
        args.pop(0)
        number_to_remove = ""

        for c in args[0]:

            if c != ",":
                number_to_remove += c
            else:
                keep.append(int(number_to_remove))
                number_to_remove = ""

        keep.append(int(number_to_remove))
        args.pop(0)


    for file in args:
        file = open(file)
        for line in file:
            output = ""
            what_to_print = ""
            comma_count = 0
            for c in line:
                if c != ",":
                    output += c

                else:
                    comma_count += 1
                    if comma_count in keep:
                        what_to_print += output

                    output = ","


            comma_count += 1
            if comma_count in keep:
                what_to_print += output.strip("\n")
            if what_to_print[0] == ",":
                print(what_to_print[1:])
            else:
                print(what_to_print)

        file.close()


def paste(args):
    """merge lines of files"""

    files = []
    iteration = 0

    for file in args:
        file = open(file)
        files.append([])

        for line in file:
            files[iteration].append(line)

        file.close()
        iteration += 1

    iteration = 0


    while True:
        keep_going = False
        what_to_print = ""
        for file in files:
            if iteration < len(file):
                keep_going = True
                if file == files[len(files)-1]:
                    what_to_print += file[iteration].strip("\n")
                else:
                    what_to_print += file[iteration].strip("\n") + ","


            else:
                if file != files[len(files)-1]:
                    what_to_print += ","



        if keep_going == False:
            break

        iteration += 1
        print(what_to_print)










