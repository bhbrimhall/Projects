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
from area_titles import area_titles_to_dict


class TestAreaTitles(unittest.TestCase):
    def setUp(self):
        self.areas = area_titles_to_dict("tests")

    def test_dictionary_length(self):
        """The areas dictionary contains 3,463 pairs"""
        self.assertEqual(len(self.areas), 3463)

    def test_no_statewide_areas(self):
        """The areas dictionary contains no keys ending in 000"""
        for key in self.areas:
            self.assertFalse(key.endswith('000'))

    def test_no_alphabetic_areas(self):
        """
        The areas dictionary contains no keys with alphabetic characters

        For all keys, .isdigit() returns True
        """
        for key in self.areas:
            self.assertTrue(key.isdigit())

    def test_keylen_is_5(self):
        """The areas dictionary contains no keys != len() of 5"""
        for key in self.areas:
            self.assertEqual(len(key), 5)

    def test_no_newlines(self):
        """The areas dictionary contains no newlines at the end of values"""
        for key in self.areas:
            self.assertFalse(self.areas[key].endswith("\n"))

    def test_50_states(self):
        """The areas dictionary contains FIPS codes representing all 50 states"""
        self.assertIn("01001", self.areas)  # Autauga County, Alabama
        self.assertIn("02010", self.areas)  # Aleutian Islands Census Area, Alaska
        self.assertIn("04001", self.areas)  # Apache County, Arizona
        self.assertIn("05001", self.areas)  # Arkansas County, Arkansas
        self.assertIn("06001", self.areas)  # Alameda County, California
        self.assertIn("08001", self.areas)  # Adams County, Colorado
        self.assertIn("09001", self.areas)  # Fairfield County, Connecticut
        self.assertIn("10001", self.areas)  # Kent County, Delaware
        self.assertIn("12001", self.areas)  # Alachua County, Florida
        self.assertIn("13001", self.areas)  # Appling County, Georgia
        self.assertIn("15001", self.areas)  # Hawaii County, Hawaii
        self.assertIn("16001", self.areas)  # Ada County, Idaho
        self.assertIn("17001", self.areas)  # Adams County, Illinois
        self.assertIn("18001", self.areas)  # Adams County, Indiana
        self.assertIn("19001", self.areas)  # Adair County, Iowa
        self.assertIn("20001", self.areas)  # Allen County, Kansas
        self.assertIn("21001", self.areas)  # Adair County, Kentucky
        self.assertIn("22001", self.areas)  # Acadia Parish, Louisiana
        self.assertIn("23001", self.areas)  # Androscoggin County, Maine
        self.assertIn("24001", self.areas)  # Allegany County, Maryland
        self.assertIn("25001", self.areas)  # Barnstable County, Massachusetts
        self.assertIn("26001", self.areas)  # Alcona County, Michigan
        self.assertIn("27001", self.areas)  # Aitkin County, Minnesota
        self.assertIn("28001", self.areas)  # Adams County, Mississippi
        self.assertIn("29001", self.areas)  # Adair County, Missouri
        self.assertIn("30001", self.areas)  # Beaverhead County, Montana
        self.assertIn("31001", self.areas)  # Adams County, Nebraska
        self.assertIn("32001", self.areas)  # Churchill County, Nevada
        self.assertIn("33001", self.areas)  # Belknap County, New Hampshire
        self.assertIn("34001", self.areas)  # Atlantic County, New Jersey
        self.assertIn("35001", self.areas)  # Bernalillo County, New Mexico
        self.assertIn("36001", self.areas)  # Albany County, New York
        self.assertIn("37001", self.areas)  # Alamance County, North Carolina
        self.assertIn("38001", self.areas)  # Adams County, North Dakota
        self.assertIn("39001", self.areas)  # Adams County, Ohio
        self.assertIn("40001", self.areas)  # Adair County, Oklahoma
        self.assertIn("41001", self.areas)  # Baker County, Oregon
        self.assertIn("42001", self.areas)  # Adams County, Pennsylvania
        self.assertIn("44001", self.areas)  # Bristol County, Rhode Island
        self.assertIn("45001", self.areas)  # Abbeville County, South Carolina
        self.assertIn("46003", self.areas)  # Aurora County, South Dakota
        self.assertIn("47001", self.areas)  # Anderson County, Tennessee
        self.assertIn("48001", self.areas)  # Anderson County, Texas
        self.assertIn("49001", self.areas)  # Beaver County, Utah
        self.assertIn("50001", self.areas)  # Addison County, Vermont
        self.assertIn("51001", self.areas)  # Accomack County, Virginia
        self.assertIn("53001", self.areas)  # Adams County, Washington
        self.assertIn("54001", self.areas)  # Barbour County, West Virginia
        self.assertIn("55001", self.areas)  # Adams County, Wisconsin
        self.assertIn("56001", self.areas)  # Albany County, Wyoming

    def test_territories(self):
        """
        The areas dictionary contains FIPS codes representing
        *   The District of Columbia
        *   Puerto Rico
        *   Virgin Islands
        """
        self.assertIn("11001", self.areas)  # District of Columbia
        self.assertIn("72001", self.areas)  # Adjuntas Municipio, Puerto Rico
        self.assertIn("78010", self.areas)  # St. Croix, Virgin Islands

    def test_overseas_locations(self):
        '''The areas dictionary contains FIPS codes representing "Overseas Locations"'''
        self.assertIn("01996", self.areas)  # Overseas Locations -- Alabama
        self.assertIn("02996", self.areas)  # Overseas Locations -- Alaska
        self.assertIn("04996", self.areas)  # Overseas Locations -- Arizona
        self.assertIn("05996", self.areas)  # Overseas Locations -- Arkansas
        self.assertIn("06996", self.areas)  # Overseas Locations -- California
        self.assertIn("08996", self.areas)  # Overseas Locations -- Colorado
        self.assertIn("09996", self.areas)  # Overseas Locations -- Connecticut
        self.assertIn("10996", self.areas)  # Overseas Locations -- Delaware
        self.assertIn("11996", self.areas)  # Overseas Locations -- D. C.
        self.assertIn("12996", self.areas)  # Overseas Locations -- Florida
        self.assertIn("13996", self.areas)  # Overseas Locations -- Georgia
        self.assertIn("15996", self.areas)  # Overseas Locations -- Hawaii
        self.assertIn("16996", self.areas)  # Overseas Locations -- Idaho
        self.assertIn("17996", self.areas)  # Overseas Locations -- Illinois
        self.assertIn("18996", self.areas)  # Overseas Locations -- Indiana
        self.assertIn("19996", self.areas)  # Overseas Locations -- Iowa
        self.assertIn("20996", self.areas)  # Overseas Locations -- Kansas
        self.assertIn("21996", self.areas)  # Overseas Locations -- Kentucky
        self.assertIn("22996", self.areas)  # Overseas Locations -- Louisiana
        self.assertIn("23996", self.areas)  # Overseas Locations -- Maine
        self.assertIn("24996", self.areas)  # Overseas Locations -- Maryland
        self.assertIn("25996", self.areas)  # Overseas Locations -- Massachusetts
        self.assertIn("26996", self.areas)  # Overseas Locations -- Michigan
        self.assertIn("27996", self.areas)  # Overseas Locations -- Minnesota
        self.assertIn("28996", self.areas)  # Overseas Locations -- Mississippi
        self.assertIn("29996", self.areas)  # Overseas Locations -- Missouri
        self.assertIn("30996", self.areas)  # Overseas Locations -- Montana
        self.assertIn("31996", self.areas)  # Overseas Locations -- Nebraska
        self.assertIn("32996", self.areas)  # Overseas Locations -- Nevada
        self.assertIn("33996", self.areas)  # Overseas Locations -- New Hampshire
        self.assertIn("34996", self.areas)  # Overseas Locations -- New Jersey
        self.assertIn("35996", self.areas)  # Overseas Locations -- New Mexico
        self.assertIn("36996", self.areas)  # Overseas Locations -- New York
        self.assertIn("37996", self.areas)  # Overseas Locations -- North Carolina
        self.assertIn("38996", self.areas)  # Overseas Locations -- North Dakota
        self.assertIn("39996", self.areas)  # Overseas Locations -- Ohio
        self.assertIn("40996", self.areas)  # Overseas Locations -- Oklahoma
        self.assertIn("41996", self.areas)  # Overseas Locations -- Oregon
        self.assertIn("42996", self.areas)  # Overseas Locations -- Pennsylvania
        self.assertIn("44996", self.areas)  # Overseas Locations -- Rhode Island
        self.assertIn("45996", self.areas)  # Overseas Locations -- South Carolina
        self.assertIn("46996", self.areas)  # Overseas Locations -- South Dakota
        self.assertIn("47996", self.areas)  # Overseas Locations -- Tennessee
        self.assertIn("48996", self.areas)  # Overseas Locations -- Texas
        self.assertIn("49996", self.areas)  # Overseas Locations -- Utah
        self.assertIn("50996", self.areas)  # Overseas Locations -- Vermont
        self.assertIn("51996", self.areas)  # Overseas Locations -- Virginia
        self.assertIn("53996", self.areas)  # Overseas Locations -- Washington
        self.assertIn("54996", self.areas)  # Overseas Locations -- West Virginia
        self.assertIn("55996", self.areas)  # Overseas Locations -- Wisconsin
        self.assertIn("56996", self.areas)  # Overseas Locations -- Wyoming
        self.assertIn("72996", self.areas)  # Overseas Locations -- Puerto Rico
        self.assertIn("78996", self.areas)  # Overseas Locations -- Virgin Islands

    def test_multicounty_not_statewide(self):
        '''The areas dictionary contains FIPS codes representing "Multicounty, Not Statewide"'''
        self.assertIn("01997", self.areas)  # Multicounty, Not Statewide -- Alabama
        self.assertIn("02997", self.areas)  # Multicounty, Not Statewide -- Alaska
        self.assertIn("04997", self.areas)  # Multicounty, Not Statewide -- Arizona
        self.assertIn("05997", self.areas)  # Multicounty, Not Statewide -- Arkansas
        self.assertIn("06997", self.areas)  # Multicounty, Not Statewide -- California
        self.assertIn("08997", self.areas)  # Multicounty, Not Statewide -- Colorado
        self.assertIn("09997", self.areas)  # Multicounty, Not Statewide -- Connecticut
        self.assertIn("10997", self.areas)  # Multicounty, Not Statewide -- Delaware
        self.assertIn("12997", self.areas)  # Multicounty, Not Statewide -- Florida
        self.assertIn("13997", self.areas)  # Multicounty, Not Statewide -- Georgia
        self.assertIn("15997", self.areas)  # Multicounty, Not Statewide -- Hawaii
        self.assertIn("16997", self.areas)  # Multicounty, Not Statewide -- Idaho
        self.assertIn("17997", self.areas)  # Multicounty, Not Statewide -- Illinois
        self.assertIn("18997", self.areas)  # Multicounty, Not Statewide -- Indiana
        self.assertIn("19997", self.areas)  # Multicounty, Not Statewide -- Iowa
        self.assertIn("20997", self.areas)  # Multicounty, Not Statewide -- Kansas
        self.assertIn("21997", self.areas)  # Multicounty, Not Statewide -- Kentucky
        self.assertIn("22997", self.areas)  # Multicounty, Not Statewide -- Louisiana
        self.assertIn("23997", self.areas)  # Multicounty, Not Statewide -- Maine
        self.assertIn("24997", self.areas)  # Multicounty, Not Statewide -- Maryland
        self.assertIn("26997", self.areas)  # Multicounty, Not Statewide -- Michigan
        self.assertIn("27997", self.areas)  # Multicounty, Not Statewide -- Minnesota
        self.assertIn("28997", self.areas)  # Multicounty, Not Statewide -- Mississippi
        self.assertIn("29997", self.areas)  # Multicounty, Not Statewide -- Missouri
        self.assertIn("30997", self.areas)  # Multicounty, Not Statewide -- Montana
        self.assertIn("31997", self.areas)  # Multicounty, Not Statewide -- Nebraska
        self.assertIn("32997", self.areas)  # Multicounty, Not Statewide -- Nevada
        self.assertIn("34997", self.areas)  # Multicounty, Not Statewide -- New Jersey
        self.assertIn("35997", self.areas)  # Multicounty, Not Statewide -- New Mexico
        self.assertIn("36997", self.areas)  # Multicounty, Not Statewide -- New York
        self.assertIn("39997", self.areas)  # Multicounty, Not Statewide -- Ohio
        self.assertIn("40997", self.areas)  # Multicounty, Not Statewide -- Oklahoma
        self.assertIn("41997", self.areas)  # Multicounty, Not Statewide -- Oregon
        self.assertIn("47997", self.areas)  # Multicounty, Not Statewide -- Tennessee
        self.assertIn("48997", self.areas)  # Multicounty, Not Statewide -- Texas
        self.assertIn("49997", self.areas)  # Multicounty, Not Statewide -- Utah
        self.assertIn("50997", self.areas)  # Multicounty, Not Statewide -- Vermont
        self.assertIn("51997", self.areas)  # Multicounty, Not Statewide -- Virginia
        self.assertIn("53997", self.areas)  # Multicounty, Not Statewide -- Washington
        self.assertIn("55997", self.areas)  # Multicounty, Not Statewide -- Wisconsin
        self.assertIn("56997", self.areas)  # Multicounty, Not Statewide -- Wyoming
        self.assertIn("72997", self.areas)  # Multicounty, Not Statewide -- Puerto Rico
        self.assertIn("78997", self.areas)  # Multicounty, Not Statewide -- Virgin Islands

    def test_out_of_state(self):
        '''The areas dictionary contains FIPS codes representing "Out-of-State"'''
        self.assertIn("01998", self.areas)  # Out-of-State, Alabama
        self.assertIn("02998", self.areas)  # Out-of-State, Alaska
        self.assertIn("04998", self.areas)  # Out-of-State, Arizona
        self.assertIn("05998", self.areas)  # Out-of-State, Arkansas
        self.assertIn("06998", self.areas)  # Out-of-State, California
        self.assertIn("08998", self.areas)  # Out-of-State, Colorado
        self.assertIn("09998", self.areas)  # Out-of-State, Connecticut
        self.assertIn("10998", self.areas)  # Out-of-State, Delaware
        self.assertIn("11998", self.areas)  # Out-of-State, District of Columbia
        self.assertIn("12998", self.areas)  # Out-of-State, Florida
        self.assertIn("13998", self.areas)  # Out-of-State, Georgia
        self.assertIn("15998", self.areas)  # Out-of-State, Hawaii
        self.assertIn("16998", self.areas)  # Out-of-State, Idaho
        self.assertIn("17998", self.areas)  # Out-of-State, Illinois
        self.assertIn("18998", self.areas)  # Out-of-State, Indiana
        self.assertIn("19998", self.areas)  # Out-of-State, Iowa
        self.assertIn("20998", self.areas)  # Out-of-State, Kansas
        self.assertIn("21998", self.areas)  # Out-of-State, Kentucky
        self.assertIn("22998", self.areas)  # Out-of-State, Louisiana
        self.assertIn("23998", self.areas)  # Out-of-State, Maine
        self.assertIn("24998", self.areas)  # Out-of-State, Maryland
        self.assertIn("25998", self.areas)  # Out-of-State, Massachusetts
        self.assertIn("26998", self.areas)  # Out-of-State, Michigan
        self.assertIn("27998", self.areas)  # Out-of-State, Minnesota
        self.assertIn("28998", self.areas)  # Out-of-State, Mississippi
        self.assertIn("29998", self.areas)  # Out-of-State, Missouri
        self.assertIn("30998", self.areas)  # Out-of-State, Montana
        self.assertIn("31998", self.areas)  # Out-of-State, Nebraska
        self.assertIn("32998", self.areas)  # Out-of-State, Nevada
        self.assertIn("33998", self.areas)  # Out-of-State, New Hampshire
        self.assertIn("34998", self.areas)  # Out-of-State, New Jersey
        self.assertIn("35998", self.areas)  # Out-of-State, New Mexico
        self.assertIn("36998", self.areas)  # Out-of-State, New York
        self.assertIn("37998", self.areas)  # Out-of-State, North Carolina
        self.assertIn("38998", self.areas)  # Out-of-State, North Dakota
        self.assertIn("39998", self.areas)  # Out-of-State, Ohio
        self.assertIn("40998", self.areas)  # Out-of-State, Oklahoma
        self.assertIn("41998", self.areas)  # Out-of-State, Oregon
        self.assertIn("42998", self.areas)  # Out-of-State, Pennsylvania
        self.assertIn("44998", self.areas)  # Out-of-State, Rhode Island
        self.assertIn("45998", self.areas)  # Out-of-State, South Carolina
        self.assertIn("46998", self.areas)  # Out-of-State, South Dakota
        self.assertIn("47998", self.areas)  # Out-of-State, Tennessee
        self.assertIn("48998", self.areas)  # Out-of-State, Texas
        self.assertIn("49998", self.areas)  # Out-of-State, Utah
        self.assertIn("50998", self.areas)  # Out-of-State, Vermont
        self.assertIn("51998", self.areas)  # Out-of-State, Virginia
        self.assertIn("53998", self.areas)  # Out-of-State, Washington
        self.assertIn("54998", self.areas)  # Out-of-State, West Virginia
        self.assertIn("55998", self.areas)  # Out-of-State, Wisconsin
        self.assertIn("56998", self.areas)  # Out-of-State, Wyoming
        self.assertIn("72998", self.areas)  # Out-of-State, Puerto Rico
        self.assertIn("78998", self.areas)  # Out-of-State, Virgin Islands

    def test_unknown_or_undefined(self):
        """The areas dictionary contains FIPS codes representing "Unknown Or Undefined" areas"""
        self.assertIn("01999", self.areas)  # Unknown Or Undefined, Alabama
        self.assertIn("02999", self.areas)  # Unknown Or Undefined, Alaska
        self.assertIn("04999", self.areas)  # Unknown Or Undefined, Arizona
        self.assertIn("05999", self.areas)  # Unknown Or Undefined, Arkansas
        self.assertIn("06999", self.areas)  # Unknown Or Undefined, California
        self.assertIn("08999", self.areas)  # Unknown Or Undefined, Colorado
        self.assertIn("09999", self.areas)  # Unknown Or Undefined, Connecticut
        self.assertIn("10999", self.areas)  # Unknown Or Undefined, Delaware
        self.assertIn("12999", self.areas)  # Unknown Or Undefined, Florida
        self.assertIn("13999", self.areas)  # Unknown Or Undefined, Georgia
        self.assertIn("15999", self.areas)  # Unknown Or Undefined, Hawaii
        self.assertIn("16999", self.areas)  # Unknown Or Undefined, Idaho
        self.assertIn("17999", self.areas)  # Unknown Or Undefined, Illinois
        self.assertIn("18999", self.areas)  # Unknown Or Undefined, Indiana
        self.assertIn("19999", self.areas)  # Unknown Or Undefined, Iowa
        self.assertIn("20999", self.areas)  # Unknown Or Undefined, Kansas
        self.assertIn("21999", self.areas)  # Unknown Or Undefined, Kentucky
        self.assertIn("22999", self.areas)  # Unknown Or Undefined, Louisiana
        self.assertIn("23999", self.areas)  # Unknown Or Undefined, Maine
        self.assertIn("24999", self.areas)  # Unknown Or Undefined, Maryland
        self.assertIn("25999", self.areas)  # Unknown Or Undefined, Massachusetts
        self.assertIn("26999", self.areas)  # Unknown Or Undefined, Michigan
        self.assertIn("27999", self.areas)  # Unknown Or Undefined, Minnesota
        self.assertIn("28999", self.areas)  # Unknown Or Undefined, Mississippi
        self.assertIn("29999", self.areas)  # Unknown Or Undefined, Missouri
        self.assertIn("30999", self.areas)  # Unknown Or Undefined, Montana
        self.assertIn("31999", self.areas)  # Unknown Or Undefined, Nebraska
        self.assertIn("32999", self.areas)  # Unknown Or Undefined, Nevada
        self.assertIn("33999", self.areas)  # Unknown Or Undefined, New Hampshire
        self.assertIn("34999", self.areas)  # Unknown Or Undefined, New Jersey
        self.assertIn("35999", self.areas)  # Unknown Or Undefined, New Mexico
        self.assertIn("36999", self.areas)  # Unknown Or Undefined, New York
        self.assertIn("37999", self.areas)  # Unknown Or Undefined, North Carolina
        self.assertIn("38999", self.areas)  # Unknown Or Undefined, North Dakota
        self.assertIn("39999", self.areas)  # Unknown Or Undefined, Ohio
        self.assertIn("40999", self.areas)  # Unknown Or Undefined, Oklahoma
        self.assertIn("41999", self.areas)  # Unknown Or Undefined, Oregon
        self.assertIn("42999", self.areas)  # Unknown Or Undefined, Pennsylvania
        self.assertIn("44999", self.areas)  # Unknown Or Undefined, Rhode Island
        self.assertIn("45999", self.areas)  # Unknown Or Undefined, South Carolina
        self.assertIn("46999", self.areas)  # Unknown Or Undefined, South Dakota
        self.assertIn("47999", self.areas)  # Unknown Or Undefined, Tennessee
        self.assertIn("48999", self.areas)  # Unknown Or Undefined, Texas
        self.assertIn("49999", self.areas)  # Unknown Or Undefined, Utah
        self.assertIn("50999", self.areas)  # Unknown Or Undefined, Vermont
        self.assertIn("51999", self.areas)  # Unknown Or Undefined, Virginia
        self.assertIn("53999", self.areas)  # Unknown Or Undefined, Washington
        self.assertIn("54999", self.areas)  # Unknown Or Undefined, West Virginia
        self.assertIn("55999", self.areas)  # Unknown Or Undefined, Wisconsin
        self.assertIn("56999", self.areas)  # Unknown Or Undefined, Wyoming
        self.assertIn("72999", self.areas)  # Unknown Or Undefined, Puerto Rico
        self.assertIn("78999", self.areas)  # Unknown Or Undefined, Virgin Islands

    def test_no_forbidden_codes(self):
        """
        The areas dictionary must NOT contain FIPS codes representing
        Nationwide, Statewide, Metropolitan Statistical Areas, Combined
        Statistical Areas, Micropolitan Statistical Areas, or Consolidated
        Metropolitan Statistical Areas
        """
        self.assertNotIn("21000", self.areas)  # Kentucky -- Statewide
        self.assertNotIn("USMSA", self.areas)  # U.S. Metropolitan Statistical Areas (combined)
        self.assertNotIn("C3310", self.areas)  # Miami-Fort Lauderdale-Miami Beach, FL MSA
        self.assertNotIn("CS176", self.areas)  # Chicago-Naperville-Michigan City, IL-IN-WI CSA
        self.assertNotIn("C3350", self.areas)  # Minot, ND MicroSA
        self.assertNotIn("M2760", self.areas)  # Fort Wayne, In MSA
        self.assertNotIn("CMS77", self.areas)  # Philadelphia-Wilmington-Atlantic City, Pa-NJ-De-Md CMSA
