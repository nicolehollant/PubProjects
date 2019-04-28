#!/usr/bin/python3

import sys
import numpy
import cv2 as cv
    

if __name__ == "__main__":
    if len(sys.argv) > 1 and (sys.argv[1] == "-h" or sys.argv[1] == "--help"):
        print("To run:\tresize.py INPUTFILE OUTPUTIMAGE SCALE\nOr:\tresize.py INPUTFILE SCALE")
        sys.exit()
    if len(sys.argv) < 3:
        print("Must provide an input file and a scale factor")
        print("To run:\tresize.py INPUTFILE OUTPUTIMAGE SCALE\nor\tresize.py INPUTFILE SCALE")
        sys.exit()
    
    inFile = sys.argv[1]
    scale = sys.argv[2]
    outFile = "RESIZED_"+inFile

    if len(sys.argv) == 4:
        scale = sys.argv[3]
        outFile = sys.argv[2]
    
    scale = float(scale)
    image = cv.imread(inFile)
    height, width = image.shape[:2]
    res = cv.resize(image,(int(scale*width), int(scale*height)), interpolation = cv.INTER_CUBIC)
    cv.imwrite(outFile,res)
