tinypng-cli.py
==============

Advanced command line client to tinypng.com

### Usage

    ./tinypng-cli.py API_KEY IN OUT

Where 
    API_KEY - your api key. Can be obtained at <https://tinypng.com/developers>
    IN - input file or directory 
    OUT - output file or directory
    When IN and OUT are files script use IN as input and store result at OUT
    When IN is file and OUT is directory script store result in OUT directory with same as IN filename
    When IN and OUT are directories in this case script run for each file (including subdirectories in IN) and 
    store results in OUT (including subdirectories tree) - batch mode.

### Examples:
    ./tinypng-cli.py 2354425 /media/data/in/infile.png /media/data/in/outfile.png
    Convert file "/media/data/in/infile.png" and store results in "/media/data/in/outfile.png" 

    ./tinypng-cli.py 2354425 /media/data/in/infile.png /media/data/in/
    This is equvalent to :
    ./tinypng-cli.py 2354425 /media/data/in/infile.png /media/data/in/infile.png

    ./tinypng-cli.py 2354425 /media/data/in/ /media/data/in/
    Run convert for each file in "/media/data/in/" and store result in "/media/data/in/" 

    

Output:

    input size: 203 kb
    output size: 62 kb
    output ratio: 0.3076
    output url: https://api.tinypng.com/output/4jjna274387m8o2k.png 

### See also:

    <https://tinypng.com>
