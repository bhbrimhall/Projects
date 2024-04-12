# Software Development Plan

## Phase 0: Requirements Analysis

I need to program python functions that can serve as text-editing tools. I need to properly document my
progress while going through this process. I need to make my progress according to the order listed in the
Tech Tree. The functions that I will create will not edit text files directly. These functions will also take
 certain arguments that can modify what the function will output.

A good solution to the problem I've been handed would be dependable functions that perform perfectly and 
handles errors properly. I'm confident in my ability to think out how these functions will work, however I do see myself struggling with some syntax issues.

This program will use data from text files provided in the form of arguments for the function being called. These
files will be stored in the /data directory contained in the project directory (cs1440-assn2). These functions will output 
text onto the command line interface.

The algorithms used in each function will be unique, yet similar in some ways. They will all need to use the data provided 
in the text files (obviously). 
## Phase 1: Design

### <ins>cat()
Description:
* Print out the lines of files

Parameters:
* This function only takes filenames as arguments. However, it can take an infinite amount of files as arguments.

Documentation String:
* Concatenate files and print on the standard output

Pseudocode:

    for file in args:
        open the file
        then for each line in the file:
            print the line
  
<br></br>

### <ins>tac()
Description:
* Print the lines of a file or files in reverse order

Parameters:
* This function only takes filenames as arguments. However, it can take an infinite amount of files as arguments.

Documentation String:
* Concatenate and print files in reverse

Pseudocode:

    for file in args:
        open the file
        make an empty list
        for each line in the file:
            append line to the list
        list = reversed list
        for each thing in the list:
            print it

<br></br>

### <ins>wc()
Description:
* Print the amount of lines, words, and characters in a file. If more than one file is given to count, it displays a total 
of the values.

Parameters:
* This function only takes filenames as arguments. However, it can take an infinite amount of files as arguments.

Documentation String:
* Print newline, word, and byte counts for each file

Pseudocode:

    set total words/lines/characters to 0
    for file in files:
        open the file
        add the length of file.readlines() to the total and output it
        go back to the start of the file
        add the length of file.read.split() to the total and output it
        go back to the start of the file
        add the length of file.read() of the total and output it

    if given more than one file in the args:
        print the totals
        

<br></br>

### <ins>grep()
Description:
* Print lines from a file that contain or don't contain a certain character or characters. 

Parameters:
* This function takes a pattern, files, and optionally a "-v". The function is called like such:
  *     grep [-v] PATTERN FILES

Documentation String:
* Print lines that match patterns

Pseudocode:

    not_contain = false
    pattern = ""
    
    if -v:
        not_contain = true
        args.pop(0)
    
    pattern = args[0]
    args.pop(0)
    
    for each file in args:
        open file
        if more than one file:
            if pattern in line and not_contain = False, print the line along with the name of the file
            elif pattern not in line and not_contain = True, print the line along with the name of the file
        else:
            if pattern in line and not_contain = False, print the line
            elif pattern not in line and not_contain = True, print the line
        

<br></br>

### <ins>head()
Description:
* Print the first 10 lines from files unless specified otherwise. Users can use the argument "-n" 
to choose a different value other than 10.

Parameters:
* This function can take "-n" and "[positive int]" as optional arguments, then takes file names.

Documentation String:
* Output the first part of files

Pseudocode:

    numoflines = 10
    if -n
        args.pop(0)
        numoflines = args[0]
        args.pop(0)

    for each file in args
        open it
        if more than one file
            print ==> filename <==
        
        iterator = 0
        for line in file:
            if iterator == numoflines
                break   
            print(line)
            iterator+=1
       

<br></br>

### <ins>tail()
Description:
* Print the last 10 lines from files unless specified otherwise. Users can use the argument "-n" 
to choose a different value other than 10.

Parameters:
* This function can take "-n" and "[positive int]" as optional arguments, then takes file names.

Documentation String:
* Output the last part of files

Pseudocode:

    numoflines = 10
    if -n
        args.pop(0)
        numoflines = args[0]
        args.pop(0)

    for each file in args
        open it
        if more than one file
            print ==> filename <==
        
        iterator = 0
        totallinesinfile = length of file.readlines()
        file.seek(0)
        for line in file:
            if totallinesinfile - iteration <= numoflines
                print(line)
            iterator+=1
       

<br></br>

### <ins>sort()
Description:
* Print out the lines from files in lexical order. If more than one file is given, it compares the lines from all the files 
and sorts them.

Parameters:
* Takes names of files for arguments

Documentation String:
* sort lines of text files

Pseudocode:

    linestosort = []
    
    for each file in args:
        open it
        for each line in the file:
            append it to linestosort
        
    linestosort = sorted(linestosort)

    for each item in linestosort:
        print it
       

<br></br>

### <ins>paste()
Description:
* Print out lines from files on the same line with a comma between them. The first line from each 
file given will be printed on the same line with a comma between.

Parameters:
* Takes names of files for arguments

Documentation String:
* merge lines of files

Pseudocode:

    files = []
    iteration = 0

    for every file in args:
        open it
        append a list to files
        for every line in the file:
            append it to the newly created list in files
        iteration += 1

    iteration = 0
    
    while True:
        keep_going? = False
        whattoprint = ""
        for each list in files:
            if the iteration is less than the length of the list:
                keep_going = True   
                if the list is the last one in files:
                    add list[iteration] to whattoprint (no comma)
                else:
                    add list[iteration] to whattoprint (with comma)
            else (if iteration is larger than the length of the list:
                if the list isn't the last on in files:
                    add a comma to whattoprint
        if keep_going = False (if all the lists have been printed out):
            break
        iteration += 1
        print(whattoprint)
                

<br></br>

### <ins>cut()
Description:
* Takes a file whose lines have strings separated by commas. With this format of text, columns can be 
created (ex. the first string in a line before the first comma would be part of the first column). With cut, 
you can cut certain "columns" from this formatted file. The user lists which columns they want to keep, and cut
will delete the other columns.

Parameters:
* Takes optional parameters of "-f" paired with a list of positive ints (1,2,3,4,69), and required file names.

Documentation String:
* remove sections from each line of files

Pseudocode:

    keep = [1]
    if args[0] == -f:
        keep = []
        args.pop(0)
        numbertoremove = ""
        
        for each character in the list of numbers (args[0]):
            if its not a comma:
                numbertoremove += letter
            else:
                keep.append(numbertoremove)
                numbertoremove = ""

        keep.append(numbertoremove0
        args.pop(0) (remove the list from args)
        
    for each file in args
        open it
        for each line in file:
            output = ""
            whattoprint = ""
            comma_count = 0
            for each character in line:
                if it's not a comma:
                    add to output
                else:
                    add 1 to comma_count
                    if comma_count (which is essentially the column) in keep:
                        whattoprint += oupput
                    
                    output = ","

            comma_count += 1
            if comma_count in keep:
                whattoprint += output
            if the first character in whattoprint is a comma:
                remove it and print whattoprint
            else:
                print whattoprint
                

<br></br>

## Phase 2: Implementation

I really had to scratch my brain for the cut and paste functions.


## Phase 3: Testing and Debugging
*(30% of your effort)*

Deliver:

Here are some of the tests I've run for each of the functions:

    ## cat()
        $ python3.11 src/tt.py cat data/num2 data/let3
        1
        2
        a
        b
        c

    This tests if cat prints out the lines from files onto the stardard output.

        $ python3.11 src/tt.py cat nonexistentfile
        Traceback (most recent call last):
          File "C:\Users\bhbri\OneDrive\Desktop\cs1440assn\cs1440-assn2\src\tt.py", line 44, in <module>
            cat(sys.argv)
          File "C:\Users\bhbri\OneDrive\Desktop\cs1440assn\cs1440-assn2\src\Concatenate.py", line 25, in cat
            f = open(file)
                ^^^^^^^^^^
        FileNotFoundError: [Errno 2] No such file or directory: 'nonexistentfile'

This tests if cat raises an error when an incorrect filename is given.

    ## tac()
        $ python3.11 src/tt.py tac data/num2 data/let3
        2
        1
        c
        b
        a

This tests if tac prints the lines of files in reverse order.

        $ python3.11 src/tt.py tac data/num2 nonexistentfile
        2
        1
        Traceback (most recent call last):
          File "C:\Users\bhbri\OneDrive\Desktop\cs1440assn\cs1440-assn2\src\tt.py", line 51, in <module>
            tac(sys.argv)
          File "C:\Users\bhbri\OneDrive\Desktop\cs1440assn\cs1440-assn2\src\Concatenate.py", line 36, in tac
            f = open(file)
                ^^^^^^^^^^
        FileNotFoundError: [Errno 2] No such file or directory: 'nonexistentfile'

This tests if tac raises an error when an incorrect filename is given.

## wc()

        $ python3.11 src/tt.py wc data/names8
        9       9       70      data/names8
    
This tests if wc returns the number of lines, words, and characters in a file.

        $ python3.11 src/tt.py wc data/names8 data/words200
        9       9       70      data/names8
        200     200     1790    data/words200
        209     209     1860    total

This tests if wc is able to total up the numbers of lines, words, and characters in files.

        $ python3.11 src/tt.py wc data/names8 nonexistentfile
        9       9       70      data/names8
        Traceback (most recent call last):
          File "C:\Users\bhbri\OneDrive\Desktop\cs1440assn\cs1440-assn2\src\tt.py", line 58, in <module>
            wc(sys.argv)
          File "C:\Users\bhbri\OneDrive\Desktop\cs1440assn\cs1440-assn2\src\WordCount.py", line 29, in wc
            file = open(file)
                   ^^^^^^^^^^
        FileNotFoundError: [Errno 2] No such file or directory: 'nonexistentfile'

This tests if wc raises an error when an incorrect filename is given.

## grep()

         $ python3.11 src/tt.py grep oo data/words200
        clubroom
        boom
        flooding
        burglarproofed
    
This tests if grep prints lines that have the specified pattern.

        $ python src/tt.py grep a data/ages8 data/colors8 data/let3
        data/colors8:Favorite Color
        data/colors8:Royal Blue
        data/colors8:Light Salmon
        data/colors8:DarkSea Green
        data/colors8:Dark Goldenrod
        data/let3:a

This tests if grep can find all lines containing lowercase 'a' across multiple files.

      $ python src/tt.py grep -v data/let3
      Error: Please provide a pattern and at least one filename

        tt.py grep [-v] PATTERN FILENAME...
            Print lines of files matching PATTERN
            -v  Invert matching; print lines which DO NOT match PATTERN

This tests if grep will raise an error when a pattern isn't provided.

## head()

      $ python src/tt.py head data/words200
      social
      insomniac
      implicitly
      cranky
      opponents
      clubroom
      uttering
      roughen
      easter
      dad
    
This checks to see if head prints the first 10 lines of a file.
  
      $ python src/tt.py head -n 5 data/ages8 data/names8 data/words200
      ==> data/ages8 <==
      Age
      22
      36
      24
      39
      
      ==> data/names8 <==
      Name
      Adrianna
      Julian
      Tiffany
      Savannah
      
      ==> data/words200 <==
      social
      insomniac
      implicitly
      cranky
      opponents
  
This checks to see if head can take a specific number of lines from multiple files and print them out.

        $ python src/tt.py head -n -7
        Error: Number of lines is required
    
            tt.py head|tail [-n N] FILENAME...
                Output the first or last part of files
                -n  Number of lines to print (default N=10)

This makes sure that you can't give a negative value after -n.

  ## tail()
    
        $ python src/tt.py tail data/words200
        convicting
        exacerbating
        indictment
        very
        impersonated
        latching
        reconfigurations
        activates
        autobiographies
        adverbs

This checks to see if tail outputs the last 10 lines in a file by default.

      $ python src/tt.py tail -n 3 data/ages8 data/names8 data/words200
      ==> data/ages8 <==
      23
      29
      17
      
      ==> data/names8 <==
      Michael
      Marcus
      Julianna
      
      ==> data/words200 <==
      activates
      autobiographies
      adverbs

This checks to see if tail can take a specific number of lines at the end of files and print them out.

      $ python src/tt.py tail -n seven
      Error: Number of lines is required
  
          tt.py head|tail [-n N] FILENAME...
              Output the first or last part of files
              -n  Number of lines to print (default N=10)

This checks to see if an error is raised when the value after -n isn't a positive integer.

    ## sort()

        $ python src/tt.py sort data/colors8 data/names10
        Alexa
        Angela
        Antique White
        Bailey
        Dark Goldenrod
        DarkSea Green
        Dodger Blue
        Favorite Color
        Frank
        Hazel
        Isabel
        Jerry
        Kai
        Karen
        Light Salmon
        Midnight Blue
        Mikayla
        Royal Blue
        Snow

This checks to see if sort sorts the lines of files in lexical order.
    

          $ python src/tt.py sort data/let3 DOES_NOT_EXIST data/complexity
          Traceback (most recent call last):
            File "/home/fadein/assn2/src/tt.py", line 32, in <module>
              sort(sys.argv[2:])
            File "/home/fadein/assn2/src/Sorting.py", line 16, in sort
              f = open(fil)
                  ^^^^^^^^^
          FileNotFoundError: [Errno 2] No such file or directory: 'DOES_NOT_EXIST'

This checks to see if an error is raised when an incorrect filename is given.

  ## cut()
    
      $ python src/tt.py cut -f 2,4 data/people.csv
      Age,Locomotion Style
      22,crawl
      36,traipse
      24,push
      39,march
      26,trot
      23,lurch
      29,slink
      17,wriggle

  This checks to see if cut cuts out the correct columns from a file that is formatted in a specific way. It also
  tests if you can select specific columns to cut out using -f and a list of positive integers.

    $ python src/tt.py cut -f 13 data/people.csv
    $
  
  This tests if cut will cut everything except the 13th column in people.csv (there is no 13th column)

    $ python src/tt.py cut -f 0,-1 data/let3
    Error: A comma-separated field specification is required
    
    tt.py cut [-f LIST] FILENAME...
        Remove comma-separated sections from each line of files
        -f  List of comma-separated integers indicating fields to output

  This tests to see if cut raises an error when the user's list of numbers after -f isn't positive integers.


  ## paste()

      $ python src/tt.py paste data/num2 data/let3 data/words5
      1,a,babbles
      2,b,sneakiness
      ,c,trimly
      ,,agree
      ,,frankly
  This tests to see if paste pastes the nth line from each file on one single line with a comma between them.

    $ python3.11 src/tt.py paste data/let3 hi data/num2
    Traceback (most recent call last):
      File "C:\Users\bhbri\OneDrive\Desktop\cs1440assn\cs1440-assn2\src\tt.py", line 132, in <module>
        paste(sys.argv)
      File "C:\Users\bhbri\OneDrive\Desktop\cs1440assn\cs1440-assn2\src\CutPaste.py", line 77, in paste
        file = open(file)
               ^^^^^^^^^^
    FileNotFoundError: [Errno 2] No such file or directory: 'hi'


  This tests to see if an error is raised if an incorrect filename is given.

## Phase 4: Deployment
I've successfully pushed the code to the GitLab server and run through multiple test cases. Everything is working smoothly.

## Phase 5: Maintenance

I'm confident that the programs that I wrote can be understood by others if they take their time trying to understand it.
I'm confident in my knowledge about how each function works and behaves.
If a bug was reported in a few months, I believe that I could fix it is less than thirty minutes.

My documentation is a little confusing and incomplete. I could've put more effort into documentation.
If I were to come back to this project in a few months however, I think that I could understand what I'm getting at in my documentation.

I feel like I could easily add a feature to this program if I wanted to. It isn't that hard to understand and 
can definetly be edited. 

If the next update of python doesn't remove any functions that it already has, I'm sure that it can withstand updates.
This is also true with updates to computer software and hardware.