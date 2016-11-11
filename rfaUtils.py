'''
Created on Oct 19, 2016

@author: sashaalexander
@author: team X
'''
from datetime import datetime
import os, sys
from os.path import basename
import pprint

def getLog(location, file_name):
    """
    Creates 'logs' directory, if it doesn't exist,
    creates or opens a log file in 'logs' directory.
    """
    file_base_name = basename(file_name)
    # assign a current working directory + '/logs' to log_dir variable (platform independent)
    log_dir = os.path.join(os.getcwd(), location)
    # or --> script directory: log_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "logs")
    # or --> user directory: log_dir = os.path.join(os.path.expanduser("~"), "logs")

    try:
        # if logs directory(!) doesn't exist, create it
        if not os.path.isdir(log_dir):
            os.makedirs(log_dir)
        # open log file with prefix and timestamp (platform independent) in Append mode
        log = open(os.path.join(log_dir, file_base_name + getCurTime("_%Y%m%d_%H-%M") + ".log"), "a")
        return log
    except (OSError, IOError):
        # return -1 in case of exception
        return -1


def qaPrint(log, message):
    """
    Prints 'timestamp + message' to console and writes it to the log file
    """
    # current date and time as string + message. example: [Oct 25 01:52:33.000001] TC1 - Passed
    log_message = getCurTime("[%b %d %H:%M:%S.%f]") + " " + message
    # prints log_message
    print log_message
    # writes message to a log file
    log.write(log_message + "\n")


def getCurTime(date_time_format):
    """
    Returns current date_time as a string formatted according to date_time_format
    """
    date_time = datetime.now().strftime(date_time_format)
    return date_time
    
    
def getLocalEnv(props_file_name):
    props_dict = {}
    try:
        with open(props_file_name, "r") as f:
            for line in f:
                key, val = line.rstrip().split("=", 1)
                props_dict[key] = val
        return props_dict                  
    except:
        return -1   
        

def getTestCases(trid):
    file_to_read = str(trid) + ".txt"
    names = ['tcid', 'rest_URL', 'HTTP_method', 'HTTP_RC_desired', 'param_list']
    d = {}
    with open(file_to_read, 'r') as f:
        for line in f:
            key, val = line.split('|',1)
            d_inner = {}
            d[key] = d_inner
            val_inner = val.split('|')
            for i, name in list(enumerate(names))[1:]:
                key_inner = names[i]
                d_inner[key_inner] = val_inner[i - 1]
    print(d)
    pprint.pprint(d, width=1)
    return d
    

        
         
    
     

 