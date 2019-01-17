from loguru import logger
import pandas as pd
import os

from data import download as DD


def init():
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
    """Function fileexists determines if the parsed file for the given ticker code input argument already exists.

    Input argument is ticker, a string that indicates the financial ticker involved, ie. NPN.JO, AAPL

    Output argument is a boolean, true if the file exists, false if not."""

    logger.info("fileexists method running for " + ticker)

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

    f = []

    if DD.fileexists(ticker):
        f = pd.read_pickle(DD.generateDownloadFilename())
    return f


def parseData(data):
    """Function to parse the data so that it's ready for analysis.

    Input argument is data, the raw CSV as a text string.

    Output argument is the parsed data as a text string."""
    logger.log("TODO", "TODO:1) Parse the JSON data. For now we'll return the string as is in order to test saving the "
                       "file.")
    return data


def saveToDisk(ticker, data):
    """Function to save the data gathered to disk. This function will, in future, also update the index csv file.

    Input arguments are the ticker,  a string that indicates the financial ticker involved, ie. NPN.JO, AAPL,
    data, the data returned by the alpha_vantage time series function."""
    logger.info("Start the savetodisk function.")

    filename = generateParseFilename(ticker)

    logger.info(f"Filename generated: {filename}")

    logger.info("Trying to save file.")
    logger.info(f"File location: {filename}")
    data.to_pickle(filename)
