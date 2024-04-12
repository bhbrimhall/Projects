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

import unittest
import tests.test_area_titles
import tests.test_report
import tests.test_industry_data
import tests.test_util


suite = unittest.TestSuite()
suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(tests.test_area_titles.TestAreaTitles))
suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(tests.test_report.TestReport))
suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(tests.test_industry_data.TestIndustryData))
suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(tests.test_util.TestUtil))

unittest.TextTestRunner(verbosity=2).run(suite)
