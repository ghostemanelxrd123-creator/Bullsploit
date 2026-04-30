
#basic module description
def description():
    return ".Py payload builder"

#basic module rank
def rank():
    return "Good"

#basic module date
def date():
    return "30.04.2026"

#set arguments
def depargs():
    return {
        "host": "Reverse IPv4",
        "port": "Reverse port",
        "module": "Path to the required post module"
    }

#imports
from StrFuncs import err, evnt, datetime
import ast, os, sys, time

#main function
def main():
    pass

#launch func
def launch(args):
    currdir = os.path.dirname(os.path.abspath(__file__))
    payloadspath = os.path.join(currdir, '..', 'payloads')
    for filename 

            

