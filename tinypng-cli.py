#!/usr/bin/python3
#
# name     : tinypng-cli, cli for tinypng
# author   : Xu Xiaodong <xxdlhy@gmail.com>; Nikolay Kulchicki
# license  : GPL
# created  : 2014 Jun 15
# fork     : 2014 Sep 18
# modified : 2014 Sep 18
#

import requests
import sys
import os

# main function to run tinny png shrinking
def fileToFile(inFilePath, outFilePath, key):
    print(inFilePath + " --> " + outFilePath);

    #check if directory exists
    saveDir = os.path.dirname(outFilePath);
    if os.path.isdir(saveDir) != True:
        os.makedirs(saveDir);

    url = 'https://api.tinypng.com/shrink'
    auth = requests.auth.HTTPBasicAuth('api', key)
    data = open(inFilePath, 'rb')

    r = requests.post(url, data=data, auth=auth)

    if r.status_code == 201:
        result = r.json()
        input_size = result['input']['size'] / 1024
        output_size = result['output']['size'] / 1024
        output_ratio = result['output']['ratio']
        output_url = result['output']['url']
        print('input size: %s kb\noutput size: %s kb\noutput ratio: %s\noutput url: %s' % (input_size, output_size, output_ratio, output_url))

        data = open(outFilePath, 'wb');
        r = requests.get(output_url);

        if r.status_code == 200:
            data.write(r.content)
        else:
            print('Save image failed :(')
    else:
        print('Compression failed :(')
    print();


# shrink file and store in directory with same name
def fileToDirectory(inFilePath, outFilePath, key):
    onlyFileName = os.path.basename(inFilePath);

    toFilePath = os.path.join(outFilePath, onlyFileName);
    fileToFile(inFilePath, toFilePath, key);

# run shrink from one directory to another (bath mode)
def directoryToDirectory(inDir, outDir, key):
    dirContent = listPngFiles(inDir);
    for f in dirContent:
        relativePath = os.path.relpath(f, inDir);
        fullOutFileName = os.path.join(outDir, relativePath);
        
        #call file to file convertation
        fileToFile(f, fullOutFileName, key);

# recursivly list png files in given directory 
def listPngFiles(inDir):
    return [os.path.join(dp, f) for dp, dn, filenames in os.walk(inDir) for f in filenames if os.path.splitext(f)[1] == '.png'];


def help():
    print("./tinypng-cli.py API_KEY IN OUT");
    print("Where: ");
    print("API_KEY - your api key. Can be obtained at <https://tinypng.com/developers>  ");
    print("IN - input file or directory   ");
    print("OUT - output file or directory  ");
    print("When IN and OUT are files script use IN as input and store result at OUT  ");
    print("When IN is file and OUT is directory script store result in OUT directory with same as IN filename  ");
    print("When IN and OUT are directories in this case script run for each file (including subdirectories in IN) and  ");
    print("store results in OUT (including subdirectories tree) - batch mode.  ");


# Main function
if __name__ == '__main__':
    #check params
    if len(sys.argv) != 4:
        help();
        exit(1); 

    apiKey = sys.argv[1];
    inPath = sys.argv[2];
    outPath = sys.argv[3];

    # check run modes
    isInPathFile = os.path.isfile(inPath);
    isOutPathFile = os.path.isfile(outPath);

    if isInPathFile == True and isOutPathFile == True:
        # file to file convertion
        fileToFile(inPath, outPath, apiKey);
    
    elif isInPathFile == True and isOutPathFile == False:
        # file -> to directory
        fileToDirectory(inPath, outPath, apiKey);
    elif isInPathFile == False and isOutPathFile == False:
        # directory to directory convertion (bath mode)
        directoryToDirectory(inPath, outPath, apiKey);
    else:
        print("Can not convert directory to file");
        help();
        exit(1);
    
    exit(0);
