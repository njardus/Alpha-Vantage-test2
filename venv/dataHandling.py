from loguru import logger
import json
import codecs

def init():
    logger.info("Nothing to initialize in dataHandling *yet*.")

def fileExists(ticker):
    """Function fileExists determines if the csv data file for the given ticker code input argument already exists.

    Input argument is ticker, a string that indicates the financial ticker involved, ie. NPN.JO, AAPL

    Output argument is a boolean, true if the file exists, false if not."""

    logger.info("fileExists method running for " + ticker)

    returnValue = True

    # Generate filename
    filename = generateFilename(ticker)

    try:
        logger.info("Trying to open file.")
        logger.info("File location: " + filename)
        fh = open(filename, 'r')
    except FileNotFoundError:
        logger.critical("File not found")
        returnValue = False

    return returnValue


def generateFilename(ticker):
    filename = '..\\data\\' + 'stock_market_data-%s.csv' % ticker
    return filename


def isDataFresh(ticker, age):
    """Function should query the index csv to determine when last a financial ticker's data was updated. The function
    then compares the time passed to some setting that the user set up.

    Input arguments are ticker, a string that indicates the financial ticker involved, ie. NPN.JO, AAPL, and
    age, an integer that indicates the maximum allowable age of data in seconds.

    Output argument is a boolean, true if the data is fresh enough, false if not."""

    logger.log("TODO", "TODO: 2) Create an index csv where we record each data fetch transaction. Col 1 is ticker code, Col 2 timestamp, Col 3 success bool. This will assist with the isDataFresh function.")
    logger.info("Complete isDataFresh method. This will require implimenting an index csv file.")

    ## Dummy return so that we *always* pull fresh data until this is implimented properly.
    return False


def saveToDisk(ticker, meta_data, data):
    """Function to save the data gathered to disk. This function will, in future, also update the index csv file.

    Input arguments are the ticker,  a string that indicates the financial ticker involved, ie. NPN.JO, AAPL,
    meta_data, the metadata returned by the alpha_vantage time series function, and
    data, the data returned by the alpha_vantage time series function."""
    logger.info("Start the saveToDisk function.")

    filename = generateFilename(ticker)

    logger.info(f"Filename generated: {filename}")
    with open(filename, 'wb') as f:
        json.dump(meta_data, f, sort_keys=False, indent=4)
        json.dump(data, f, sort_keys=False, indent=4)