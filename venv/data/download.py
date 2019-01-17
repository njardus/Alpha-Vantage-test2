from loguru import logger
import pandas as pd
import json
import os


def init():
    logger.info("Initializing dataDownload")

    dirName = "../data"
    if not os.path.exists(dirName):
        os.mkdir(dirName)
        logger.info("Directory ", dirName, " Created ")
    else:
        logger.info("Directory ", dirName, " already exists")


def fileexists(ticker):
    """Function fileexists determines if the csv data file for the given ticker code input argument already exists.

    Input argument is ticker, a string that indicates the financial ticker involved, ie. NPN.JO, AAPL

    Output argument is a boolean, true if the file exists, false if not."""

    logger.info("fileexists method running for " + ticker)

    returnValue = True

    # Generate filename
    filename = generateDownloadFilename(ticker)

    try:
        logger.info("Trying to open file.")
        logger.info("File location: " + filename)
        fh = open(filename, 'r')
    except FileNotFoundError:
        logger.critical("File not found")
        returnValue = False

    return returnValue


def generateDownloadFilename(ticker):
    filename = '..\\data\\' + 'stock_market_data-%s.csv' % ticker
    return filename


def isdatafresh(ticker, age):
    """Function should query the index csv to determine when last a financial ticker's data was updated. The function
    then compares the time passed to some setting that the user set up.

    Input arguments are ticker, a string that indicates the financial ticker involved, ie. NPN.JO, AAPL, and
    age, an integer that indicates the maximum allowable age of data in seconds.

    Output argument is a boolean, true if the data is fresh enough, false if not."""

    logger.log("TODO", "TODO: 2) Create an index csv where we record each data fetch transaction. Col 1 is ticker code,"
                       " Col 2 timestamp, Col 3 success bool. This will assist with the isdatafresh function.")
    logger.info("Complete isdatafresh method. This will require implementing an index csv file.")

    # Dummy return so that we don't *always* pull fresh data until this is implemented properly.
    return True


def savetodisk(ticker, data):
    """Function to save the data gathered to disk. This function will, in future, also update the index csv file.

    Input arguments are the ticker,  a string that indicates the financial ticker involved, ie. NPN.JO, AAPL,
    data, the data returned by the alpha_vantage time series function."""
    logger.info("Start the savetodisk function.")

    filename = generateDownloadFilename(ticker)

    logger.info(f"Filename generated: {filename}")

    logger.info("Trying to save file.")
    logger.info(f"File location: {filename}")

    data.to_pickle(filename)


def loadfile(ticker):
    """Function to load previously saved data from disk.

    Input argument is the ticker,  a string that indicates the financial ticker involved, ie. NPN.JO, AAPL,

    Returns a dataframe with the data.
    """

    logger.info("Start the loadfile function.")

    filename = generateDownloadFilename(ticker)

    logger.info(f"Loading from {filename}.")
    data = pd.read_pickle(filename)

    return data


def cleanclosedata(data):
    """Function to clean closing from Alpha Vantage. The headers from Alpha Vantage are a bit odd, so this will just
    rename them to:
       |--Date--|--Open--|--High--|--Low--|--Close--|--Volume--|

    Input argument is the dataframe."""

    logger.log("TODO", "TODO: 10) Add a check to see if the data columns have been renamed or not.")

    data.index.names = ['Date']
    try:
        data.columns = ['Open', 'High', 'Low', 'Close', 'Volume']
    except ValueError:
        import time
        time.sleep(1)
        logger.error("ValueError in renaming the data columns. "
                     "Current data info is:"
                     ""
                     + data.info() +
                     ""
                     "Current data head is: " + data.head()
                     )

    return data
