# Software Development Plan

## Phase 0: Requirements Analysis

**Instructions:**
Plan, document, and write a python program that can read data from the Bureau of Labor Statistics' Quarterly Census of
Employment and Wages and output statistics using the data. This program can filter its output so it only looks at data
with specific characteristics. As the programmer, I need to write/complete functions that gather the data and filter it.

We want this program to run fast and effectively. We also want to make sure that the program's output is neat and easy
to read. We also want this program to handle files with care; we shouldn't use the eval() function.

I know that I have the knowledge to complete this project, however, I am aware that in order to make this program as efficient
as possible, I may need to do some research. I am not very familiar with dictionaries, but I'm confident that I will
be able to understand them easily.

This program will always take one input: a directory. Depending on what this directory is, the filter will be different.
The output of this program will be  text. It will look like a form.

## Phase 1: Design

### Functions of *area_titles.py* 
#### area_titles_to_dict(dirname)
*   What it does: This function locates a CSV file called `area-titles.csv` in
    the specified directory, and transforms it into a dictionary. This function
    will skip over area codes that contain a letter or end with three zeros.
*  If a faulty directory name is inputtedc, the program should crash because
it can't find the file.


        def area_titles_to_dict(dirname):
            file = open(dirname/area-titles.csv)
            areas = new dictionary
            skip the first line
            for every line in file:
                line = line.split(",", 1)
                if !line[0].replace("#", "").isdigit or line[0][3:5] != "000": 
                    #if the area code doesn't contain a letter or its last 3 digits are zeros:
                    areas[line[0][1:5]] = state
            report areas 

### Functions of *util.py*
#### record_matches_fips(record, areas)
*   What it does: This function is a predicate that takes a QCEW record and dictionary of FIPS areas and
    decides whether the record contains information about a FIPS area in
    the dictionary


        def record_matches_fips(record, areas):
            get fips from the record, if in areas.keys:
                return True
            else
                return False

#### get_fips(record)
*   What it does: Extracts a FIPS area code from a QCEW record

        def get_fips(record):
            return record.split(",")[0].replace('"', "")

#### record_is_all_industries(record)
*   What it does: Predicate that takes a QCEW record and decides whether the record
    contains information about all industries under all types of
    ownership throughout the entire economy

        def record_is_all_industries(record):
            if record.split(",")[1] == 0 and [2] == 10
                return True
            else return False

#### record_is_software_industry(record)
*   What it does: Predicate that takes a QCEW record and decides whether the record
    contains information about privately owned software publishing firms

        def record_is_software_industry(record):
            if record.split(",")[1] == 5 and [2] == 513210
                return True
            else return False

#### get_estabs(record)
*   What it does: Extracts the annual average of quarterly establishment counts for a
    given year from a QCEW record

        def get_estabs(record):
            return record.split(",")[13]

#### get_emplvl(record)
*   What it does: Extracts the annual average of monthly employment levels for a given
    year from a QCEW record

        def get_emplvl(record):
            return record.split(",")[8]

#### get_wages(record)
*   What it does: Extracts the sum of the four quarterly total wage levels for a given
    year from a QCEW record

        def get_wages(record):
            return record.split(",")[15]

### Functions of *industry_data.py*
#### __init__(self)
*   What it does: Initializes the statistic variables that the IndustryData Class
edits. These include: `num_areas`, `total_annual_wages`, `max_annual_wages`, `total_estabs`, `max_mestabs`,
`total_emplvl`, and `max_emplvl`.

        __init__(self):
            self.num_areas = 0
            self.total_annual_wages = 0
            self.max_annual_wages = ["",""]
            self.total_estabs = 0
            self.max_estabs = ["",""]
            self.total_emplvl = 0
            self.max_emplvl = ["",""]

#### add_record(self, record, areas)
*   What it does: Adds a record's data to the summary statistics. This method does not need to validate it its input;
the record must be validated before this method is called.

    Parameters:
     - record: A record containing employment and wage data.
     - areas: A dictionary mapping FIPS area codes to human-friendly area titles.

    This method updates the following summary statistics:
     - Adds one to the total number of areas processed.
     - Calculates and accumulates the total annual wages.
     - Keeps track of the area with the maximum annual wages.
     - Calculates and accumulates the total number of establishments.
     - Keeps track of the area with the maximum number of establishments.
     - Calculates and accumulates the total employment level.
     - Keeps track of the area with the maximum employment level.


        def add_record(self, record, areas):
            self.num_areas += 1
            self.total_annual_wages += get_wages(record)
            if getwages(record) is bigger than the original max
                self.max_annual_wages = [getfips(record), getwages(record)]
            self.total_estabs += getestabs(record)
            if getestabs(record) is bigger than original maximum estabs:
                self.max_estabs = [getfips(record), getestabs(record)
            self.total_emplvl += get_emplvl(record)
            if get_emplvl(record) is bigger than the original max emplvl:
                self.max_emplvl = [getfips(record), getemplvl(record)
    
### "Functions" of *big_data.py*
This is the file that is ran from the command line. It doesn't necessarily need
"functions". It just needs to do a couple things:
*   Validate the user input
*   Create the area code dictionary
*   Fill in the report using information from `2022.annual.singlefile.csv`
*   Print it

If faulty arguments are given, the program should either crash because it can't
find a file or it should print a usage message and exit.


        if len of sys.argv is 1:
            print a usage message
            exit()
        areas = area_titles_to_dict(sys.argv[1])
        
        rpt = Report(2022)

        file = open(sys.argv[1] + "/2022.annual.singlefile.csv")
        file.readline()
        for line in file:
            if line matches fips:
                if record is all industries:
                    rpt.all.add_record(line, areas)
                elif record is software industry
                    rpt.soft.add_record(line, areas)

        print(rpt)

## Phase 2: Implementation

When coding `area_titles_to_dict`, I needed to change the max split to 2 and the line[0][1:5] to line[0][1:6].

When coding the get_*blah*(record) functions in util.py, the index values needed to change.

When looking at the unit tests, I noticed that the test record the program was passing in
wasn't a string, it was a list of strings. Now I have to go back and change my other functions to deal with this properly.

When coding add_record(self, record, areas) in `industry_data.py`, I added an if statement that checks if the max lists are empty.

## Phase 3: Testing and Debugging

To run some test cases, I duplicated the 2022.annual.singlefile.csv into the different data directories and used the 
steps in README.md to get specific information. Here's a list of all the commands I ran to test each of these
new cropped data files.

        bhbri@The_Beast MINGW64 ~/OneDrive/Desktop/cs1440assn/cs1440-assn3 (master)
        $ python3.11 src/big_data.py data/DC_all_industries/

        bhbri@The_Beast MINGW64 ~/OneDrive/Desktop/cs1440assn/cs1440-assn3 (master)
        $ python3.11 src/big_data.py data/DC_complete/

        bhbri@The_Beast MINGW64 ~/OneDrive/Desktop/cs1440assn/cs1440-assn3 (master)
        $ python3.11 src/big_data.py data/DC_sofware_industry/

        bhbri@The_Beast MINGW64 ~/OneDrive/Desktop/cs1440assn/cs1440-assn3 (master)
        $ python3.11 src/big_data.py data/IN_all_industries/

        bhbri@The_Beast MINGW64 ~/OneDrive/Desktop/cs1440assn/cs1440-assn3 (master)
        $ python3.11 src/big_data.py data/IN_software_industry/

        bhbri@The_Beast MINGW64 ~/OneDrive/Desktop/cs1440assn/cs1440-assn3 (master)
        $ python3.11 src/big_data.py data/NH+RI_complete/

        bhbri@The_Beast MINGW64 ~/OneDrive/Desktop/cs1440assn/cs1440-assn3 (master)
        $ python3.11 src/big_data.py data/NH+RI_reversed/

        bhbri@The_Beast MINGW64 ~/OneDrive/Desktop/cs1440assn/cs1440-assn3 (master)
        $ python3.11 src/big_data.py data/USA_full/

        bhbri@The_Beast MINGW64 ~/OneDrive/Desktop/cs1440assn/cs1440-assn3 (master)
        $ python3.11 src/big_data.py data/UT_complete/

        bhbri@The_Beast MINGW64 ~/OneDrive/Desktop/cs1440assn/cs1440-assn3 (master)
        $ python3.11 src/big_data.py data/UT_reversed/

I was very suprised to see that when I ran these test cases, they all worked perfectly the first time. Each command's
output matched exactly what was given in the `output.txt` files. 

I also ran the unit tests and the benchmark tests in PyCharm. I used the unit tests in `run_tests.py` as I implemented my code in phase 2,
and that helped a lot. I found bugs that I wouldn't be able to fix if it wasn't for the tests. For instance, I realized
that the record needs to be passed into functions as a list, not a string. I also learned that the max lists in
`industry_data.py` needed to have a string in the first index and an integer in the second. The unit tests also
helped me notice that my `get_*something*(record)` functions in `util.py` were getting the wrong values. 

After I had my program outputting the right stuff when I ran `big_data.py`, I ran the benchmark test in PyCharm. It passed!

## Phase 4: Deployment

Everything is lookin good! I pushed my final commit to gitlab with the right tags.


## Phase 5: Maintenance

I am satisfied with the code I have written for this assignment. I believe that I can easily be followed. That my just
be my bias, but it is what think. If a bug was reported, I think I could fix it in under an hour.

I think I did a better job documenting this assignment than my previous one. I when through the
workflow step by step. I will admit that I did rush it a little and it definetly could be improved,
but it was better than last time. I think it will be able to understand it still in the future.

I think it will be moderately difficult to add a feature in a years time. This is because I am still confused
about how the `report.py` works. This is the only reason. I will also most likely have to look up the QCEW
cheat sheet again.

I believe that my program will still work if an upgrade happens to my computer, os, or my python version.