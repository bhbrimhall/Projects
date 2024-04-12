#!/usr/bin/env python

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


import sys

from Concatenate import cat, tac
from CutPaste import cut, paste
from Grep import grep
from Partial import head, tail
from Sorting import sort
from WordCount import wc
from Usage import usage


if len(sys.argv) < 2:
    usage()
    sys.exit(1)
else:

    sys.argv.pop(0)

    if sys.argv[0] == "cat":
        sys.argv.pop(0)
        if len(sys.argv) > 0:
            cat(sys.argv)
        else:
            usage("Too few arguments", "cat")

    elif sys.argv[0] == "tac":
        sys.argv.pop(0)
        if len(sys.argv) > 0:
            tac(sys.argv)
        else:
            usage("Too few arguments", "tac")

    elif sys.argv[0] == "wc":
        sys.argv.pop(0)
        if len(sys.argv) > 0:
            wc(sys.argv)
        else:
            usage("Too few arguments", "wc")

    elif sys.argv[0] == "grep":

        if len(sys.argv) > 1:
            if sys.argv[1] == "-v":
                sys.argv.pop(0)
                if len(sys.argv) > 2:
                    grep(sys.argv)
                else:
                    usage("Please provide a pattern and at least one filename", "grep")
            elif len(sys.argv) > 2:
                sys.argv.pop(0)
                grep(sys.argv)
            else:

                usage("Please provide a pattern and at least one filename", "grep")
        else:
            usage("Please provide a pattern and at least one filename", "grep")

    elif sys.argv[0] == "head":
        sys.argv.pop(0)
        if len(sys.argv) > 0:
            if sys.argv[0] == "-n":
                if len(sys.argv) > 2:
                    head(sys.argv)
                elif len(sys.argv) > 1:
                    if sys.argv[1].isdigit():
                        if int(sys.argv[1]) > -1:
                            usage("At least one filename is required", "head")
                        else:
                            usage("Number of lines is required", "head")
                    else:
                        usage("Number of lines is required", "head")
                else:
                    usage("Number of lines is required", "head")
            else:
                head(sys.argv)
        else:
            usage("Too few arguments", "head")

    elif sys.argv[0] == "tail":
        sys.argv.pop(0)
        if len(sys.argv) > 0:
            if sys.argv[0] == "-n":
                if len(sys.argv) > 2:
                    tail(sys.argv)
                elif len(sys.argv) > 1:
                    if sys.argv[1].isdigit():
                        if int(sys.argv[1]) > -1:
                            usage("At least one filename is required", "tail")
                        else:
                            usage("Number of lines is required", "tail")
                    else:
                        usage("Number of lines is required", "tail")
                else:
                    usage("Number of lines is required", "tail")
            else:
                tail(sys.argv)
        else:
            usage("Too few arguments", "tail")

    elif sys.argv[0] == "sort":
        sys.argv.pop(0)
        if len(sys.argv) > 0:
            sort(sys.argv)
        else:
            usage("Too few arguments", "sort")

    elif sys.argv[0] == "paste":
        sys.argv.pop(0)
        if len(sys.argv) > 0:
            paste(sys.argv)
        else:
            usage("Too few arguments", "paste")

    elif sys.argv[0] == "cut":
        sys.argv.pop(0)
        if len(sys.argv) > 0:
            if len(sys.argv) > 1:
                if sys.argv[0] == "-f":
                    iteration = 0
                    fail = False
                    for c in sys.argv[1]:
                        if not c.isdigit():
                            if c == ",":
                                try:
                                    if not sys.argv[1][iteration + 1].isdigit():
                                        fail = True
                                        break
                                except IndexError:
                                    fail = True
                                    break

                            else:
                                fail = True
                                break

                        iteration += 1
                    if fail == False:
                        if len(sys.argv) > 2:
                            cut(sys.argv)
                        else:
                            usage("At least one filename is required", "cut")
                    else:
                        usage("A comma-separated field specification is required", "cut")

            elif sys.argv[0] == "-f":
                usage("A comma-separated field specification is required", "cut")
            else:
                cut(sys.argv)
        else:
            usage("Too few arguments", "cut")

    else:
        usage()
