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
from industry_data import IndustryData


class TestIndustryData(unittest.TestCase):
    def test_default_values(self):
        """
        Ensure the attributes of the Report object are named correctly
        and have the expected default values
        """
        dat = IndustryData()

        self.assertEqual(0, dat.num_areas)
        self.assertEqual(0, dat.total_annual_wages)
        self.assertEqual(["", 0], dat.max_annual_wages)
        self.assertEqual(0, dat.total_estabs)
        self.assertEqual(["", 0], dat.max_estabs)
        self.assertEqual(0, dat.total_emplvl)
        self.assertEqual(["", 0], dat.max_emplvl)

    def test_add_record(self):
        dat = IndustryData()
        areas = {
                "02016": "TEST AREA A",
                "31079": "TEST AREA B",
                }

        record0 = '"02016","2","611","75","0","2022","A","",2,1,59925,0,0,1257,65373,"",17.34,0.03,0.02,0.00,0.00,0.79,0.79,"N",0,0.0,0,0,0,0,0,0,0,0,0,0,0,0'.split(",")
        dat.add_record(record0, areas)
        self.assertEqual(1, dat.num_areas)
        self.assertEqual(59925, dat.total_annual_wages)
        self.assertEqual(["TEST AREA A", 59925], dat.max_annual_wages)
        self.assertEqual(2, dat.total_estabs)
        self.assertEqual(["TEST AREA A", 2], dat.max_estabs)
        self.assertEqual(1, dat.total_emplvl)
        self.assertEqual(["TEST AREA A", 1], dat.max_emplvl)

        record1 = '"31079","1","102","72","0","2022","A","",22,605,47017021,0,0,1494,77682,"",2.02,0.93,1.07,0.00,0.00,1.16,1.16,"",0,0.0,-41,-6.3,-712727,-1.5,0,0.0,0,0.0,73,5.1,3787,5.1'.split(",")
        dat.add_record(record1, areas)
        self.assertEqual(2, dat.num_areas)
        self.assertEqual(47076946, dat.total_annual_wages)
        self.assertEqual(["TEST AREA B", 47017021], dat.max_annual_wages)
        self.assertEqual(24, dat.total_estabs)
        self.assertEqual(["TEST AREA B", 22], dat.max_estabs)
        self.assertEqual(606, dat.total_emplvl)
        self.assertEqual(["TEST AREA B", 605], dat.max_emplvl)
