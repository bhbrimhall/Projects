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

def area_titles_to_dict(dirname):
    """
    This function locates a CSV file called `area-titles.csv` in
    the specified directory, and transforms it into a dictionary
    """
    file = open(dirname + "/area-titles.csv") # open the file
    areas = {}                                                                     # initialize the dict
    file.readline()                                                                 # skip the first line

    for line in file:
        line = line.split(",", 1)                                       # split the area code from the county and state
        if line[0][1:6].isdigit():                                                  # check if the area code doesn't have a letter in it
            if line[0][3:6] != "000":                                               # check if the last 3 characters of the area code isn't "000"
                areas[line[0][1:6]] = line[1].replace('"', "").strip()  # add to the dict

    return areas