# -*- coding: utf-8 -*-
"""
Created on Wed Nov 04 10:31:43 2015

@author: qutiba
"""
import argparse
import logging
from BlueYonder_PKG import URL_DOWNLOADER_CLS as pkg
import sys

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('LocalDirectory', type=str, nargs='*',metavar='Dir',
                   help='Local Directory for storing the downloaded images')
    parser.add_argument('URLsFile', type=str, nargs='*',metavar='file',
                   help='URLs\' plain text file')
    

    args = parser.parse_args()

    logging.info('Main started')
    
    s=pkg.URL_DOWNLOADER_CLS("D:\\","D:\\test.txt")
    if len(sys.argv) == 3:
        s.Call_fetch_and_store_URLs(sys.argv[1],sys.argv[2])
    else:
        print ' '
        print 'This script takes two arguments.. For help please type: main.py --h '
    
    logging.info('Main finished successfully')