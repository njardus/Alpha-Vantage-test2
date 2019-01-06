from loguru import logger
import os

import dataDownload as DD

def init():
    logger.log("TODO", "TODO: 1)a) Create functions to - load the CSV file")
    logger.log("TODO", "TODO: 1)b)                     - parse the JSON file into easier to analyse formats")
    logger.log("TODO", "TODO: 1)c)   *DONE*            - save the parsed data into a new file")

    dirName = "../data"
    if not os.path.exists(dirName):
        os.mkdir(dirName)
        logger.info("Directory ", dirName, " created ")
    else:
        logger.info("Directory ", dirName, " already exists")

def generateParseFilename(ticker):
    filename = '..\\data\\' + 'stock_market_parsed-%s.csv' % ticker
    return filename

def fileExists(ticker):
    """Function fileExists determines if the parsed file for the given ticker code input argument already exists.

    Input argument is ticker, a string that indicates the financial ticker involved, ie. NPN.JO, AAPL

    Output argument is a boolean, true if the file exists, false if not."""

    logger.info("fileExists method running for " + ticker)

    returnValue = True

    # Generate filename
    filename = generateParseFilename(ticker)

    try:
        logger.info("Trying to open file.")
        logger.info("File location: " + filename)
        fh = open(filename, 'r')
    except FileNotFoundError:
        logger.critical("File not found")
        returnValue = False

    return returnValue

def loadFile(ticker):
    """Function to load the unparsed data from file.

    Input argument is ticker, the ticker of the raw data we're looking through."""

    data = []

    if DD.fileExists(ticker):
        f = open(DD.generateDownloadFilename(ticker), "rt")
        data = f.read()
    return data


def parseData(data):
    """Function to parse the data so that it's ready for analysis.

    Input argument is data, the raw CSV as a text string.

    Output argument is the parsed data as a text string."""
    logger.log("TODO", "TODO:1) Parse the JSON data. For now we'll return the string as is in order to test saving the "
                       "file.")
    return data


def saveToDisk(ticker, data):
    """Function to save the parsed data to disk.

    Input arguments are the ticker,  a string that indicates the financial ticker involved, ie. NPN.JO, AAPL,
    parsed_data, the parsed output that we're interested in."""
    logger.info("Start the saveToDisk function.")

    filename = generateParseFilename(ticker)

    logger.info(f"Filename generated: {filename}")

    logger.info("Trying to open file.")
    logger.info(f"File location: {filename}")
    with open(filename, 'w') as f:
        f.write(data)
#        json.dump(meta_data, f, sort_keys=False, indent=4)
 #       json.dump(data, f, sort_keys=False, indent=4)
