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


def grep(args):
    """print lines that match patterns"""

    not_contain = False
    pattern = ""

    if args[0] == "-v":
        not_contain = True
        args.pop(0)

    pattern = args[0]
    args.pop(0)

    for file in args:
        file = open(file)
        for line in file:
            if len(args) > 1:
                if pattern in line and not_contain == False:
                    print(str(file.name) + ": " + line, end="")
                elif pattern not in line and not_contain == True:
                    print(str(file.name) + ": " + line, end="")
            else:
                if pattern in line and not_contain == False:
                    print(line, end="")
                elif pattern not in line and not_contain == True:
                    print(line, end="")
        file.close()



