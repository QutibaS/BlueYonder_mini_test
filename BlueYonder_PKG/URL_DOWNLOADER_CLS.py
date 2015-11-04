# -*- coding: utf-8 -*-
"""
Created on Tue Nov 03 20:08:32 2015

@author: Qutiba
"""

import urllib as Downloader 
import urlparse, mimetypes
import logging
import os
import errno

"""
    This class for fetch URLs that contains images only and 
    store them in local storage.
"""
class URL_DOWNLOADER_CLS:
    
    #*****************************************************************************
    #*************** Class Constructor:Initailization values***********************
    #*****************************************************************************
    def __init__(self,Local_Directory,URLS_FileName):
        logging.info('URL_DOWNLOADER_CLS class initialization')
        if isinstance(Local_Directory, str) and isinstance(URLS_FileName, str):
            self.Local_Directory=Local_Directory
            self.URLS_FileName=URLS_FileName
        
    #*****************************************************************************
    #*************** This function check the target of the URL *******************
    # if it's image or not using mimetypes and urlparse libraries'functions ******
    #** Input: Target URL
    #** Output: boolean value (is Image type or not)
    #*****************************************************************************
    def Check_URL_Img_type(self,url):
        logging.info('Check_URL_Img_type started')
        maintype= mimetypes.guess_type(urlparse.urlparse(url).path)[0]
        if maintype not in ('image/png', 'image/jpeg', 'image/gif'):
            logging.debug( 'URL '+ str(url) + ': invalid type')
            return False
        return True
    
    #*****************************************************************************
    #*************** This function check the local directory if exists ***********
    #************** or it isn't exist and has valid name      ******************
    # Input: Local directory
    #** Output: boolean value (is exists, valid directory or not)
    #****************************************************************************
    def Check_OR_Create_dir(self,directory):
        logging.info('Check_OR_Create_dir started')        
        try:
            os.makedirs(directory)
            return True
        except OSError as exception:
            logging.debug(  'OSError exception')
            if exception.errno != errno.EEXIST:
                logging.debug(  'invalid directory name')                
                raise
 
    #*****************************************************************************
    #*************** This function return file stream ******************
    #*****************************************************************************    
    def get_file(self, path):
        logging.info('get_file function started')
        try:
            return open(path, 'r')
        except IOError as exception:
            logging.debug('Problem when read the text file')
            raise
     
    #*****************************************************************************
    # ************* This fuction get the target URL and fetch the contect 
    #               then store it in a certain path
    # ** Input: Image URL, file path for storage
    #*****************************************************************************
    def fetch_URL_Store_file(self,URL,File_Name):
        logging.info('fetch_URL_Store_file function started')
        file_var = open(File_Name,'wb')
        img_stream=""
        try:
            img_stream=Downloader.urlopen(URL).read()        
        except IOError as exception:
            logging.debug(  'IOError exception')
            if exception.errno != errno.ESOCKTNOSUPPORT:
                logging.debug(  'Connction Problem: Check the Internet connection.')
            raise
        file_var.write(img_stream)
        file_var.close()
    
    
     
    #*****************************************************************************
    #************ This function call and collect all the previuos functionalities
    #************ to perform :
    #                    - Local directory check or create.
    #                    - read text file line by line "URLs" and for each URL:
    #                         - remove the surrounding spaces
    #                         - Check the content type of the target of the URL
    #                              if the content type is image then
    #                                    get the the image name from the URL (last field)
    #                                    concate the local directory with the image name
    #                                    call fetching image function and store it locally
    # ** Input: Local directory for storage, input file path (location + Name)                                 
    # ** Output: Folder of images                         - 
    #*****************************************************************************
    def Call_fetch_and_store_URLs(self,Directory,Input_File_path):
        logging.info('Call_fetch_and_store_URLs function started')
        self.Check_OR_Create_dir(Directory)
        Input_File=self.get_file(Input_File_path)
        for line in Input_File:
            line=line.strip()
            if self.Check_URL_Img_type(line):
                filename=line.split("//" )[-1]
                full_file_path=os.path.join(Directory, filename)        
                self.fetch_URL_Store_file(line,full_file_path)
        Input_File.close()
            

if __name__ == "__main__":
    logging.info('Main started')
    s=URL_DOWNLOADER_CLS("D:\\","D:\\test.txt")
    s.Call_fetch_and_store_URLs(sys.argv[1],sys.argv[2])
    logging.info('Main finished successfully')