#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  3 10:34:46 2017

@author: rmorriss
"""

#import os
#
#rootdir ='../data/jah_data'
#
#for subdir, dirs, files in os.walk(rootdir):
#    for file in files:
#        if 
#        f=open(file,'r')
#        lines=f.readlines()
#        f.close()
#        f=open(file,'w')
#        for line in lines:
#            
#        f.close()
        
import glob
ngrams1 = glob.glob('../data/**/*NGRAMS1.txt', recursive = True)
xml = glob.glob('../data/**/*.xml', recursive = True)
print(len(ngrams1), len(xml))
#print(xml)

dictionaries= []
for ngram in ngrams1:
    fhand = open(ngram, 'r')
    test = fhand.readlines()
    fhand.close()
    dic = {}
    for line in test:
        line2 = line.split()
        key = line2[0]
        val = int(line2[1])
        dic[key] = val
    dictionaries.append(dic)
    
print(len(dictionaries), dictionaries[0])

## make single dictionary from all the individual dictionaries
total_dic = {}
for dic in dictionaries:
    for k, v in dic:
        print(k, v)
        
    

# Put this in thinking that I needed to open and read the file;
# In fact, etree.parse takes the name of the file, not the string.
#def open_xml(file):
#    fhand = open(file)
#    xml_file = fhand.readlines()
#    fhand.close()
#    print("read file")
#    return xml_file


def xml_parse(file):
    # Function to parse the xml files and return the root
    # from here you can navigate and pull out data from the metadata
    import xml.etree.ElementTree as etree
    tree = etree.parse(file)
    print("parsed file")
    root = tree.getroot()
    print(root)

count = 0    
# Canceled out the for loop here; uncomment it to run the parser
# for x in xml:
#    opened = open_xml(x)
#    xml_parse(x)
#    count += 1
#    print(count)
#    


