#!/usr/bin/env python3

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
import time

from area_titles import area_titles_to_dict
from report import Report
from util import record_matches_fips, record_is_all_industries, record_is_software_industry


if len(sys.argv) != 2: #if incorrect args are given, exit
    print("Usage: src/big_data.py DATA_DIRECTORY")
    exit(1)

print("Reading the databases...", file=sys.stderr)
before = time.time()

areas = area_titles_to_dict(sys.argv[1]) #make areas dictionary

rpt = Report(2022) #create the report object

file = open(sys.argv[1] + "/2022.annual.singlefile.csv")
file.readline() #skip the first line
for line in file:
    line = line.split(",") # split the line in a list
    if record_matches_fips(line, areas): # if the record's fips code the area code dictionary
        if record_is_all_industries(line): #filter the industry
            rpt.all.add_record(line, areas)
        elif record_is_software_industry(line):
            rpt.soft.add_record(line, areas)




after = time.time()
print(f"Done in {after - before:.3f} seconds!", file=sys.stderr)

# Print the completed report
print(rpt)

