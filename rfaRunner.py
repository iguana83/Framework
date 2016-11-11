'''
Created on Oct 19, 2016


@author: sashaalexander
@author: team X
'''

from rfaUtils import getLog,qaPrint,getLocalEnv, getTestCases

import sys

# get the log file handle
props_file_name = '/Users/golova/Downloads/RAF_CODE_02/local.properties'
props_dict = getLocalEnv(props_file_name)
location = props_dict.get('log_dir')
log = getLog(location, sys.argv[0])


# exit if log creation failed
if log == -1:
    sys.exit("Unable to create log file")

message = "It is working, right?"

# call qaPrint to print a message with timestamp and write it to the log file
qaPrint(log, message)
qaPrint(log, "Me like what me see")


# close the log file if it open
if not log.closed:
    log.close()

getLocalEnv('/Users/golova/Downloads/RAF_CODE_02/local.properties')

def getTrid():    
    for arg in sys.argv:
        if arg.lower().startswith('--testrun='): 
            trid = int(arg.split('=')[1])
            if 0<= trid <= 10000:
                print trid
                return trid
                break
    return -1

trid = getTrid()

getTestCases(trid)

