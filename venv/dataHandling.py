from loguru import logger

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
        logger.info("File location: " + '.\\data\\' + filename)
        fh = open('..\\data\\' + filename, 'r')
    except FileNotFoundError:
        logger.critical("File not found")
        returnValue = False

    return returnValue


def generateFilename(ticker):
    filename = 'stock_market_data-%s.csv' % ticker
    return filename


def isDataFresh(ticker, age):
    """Function should query the index csv to determine when last a financial ticker's data was updated. The function
    then compares the time passed to some setting that the user set up.

    Input arguments are ticker, a string that indicates the financial ticker involved, ie. NPN.JO, AAPL, and
    age, an integer that indicates the maximum allowable age of data in seconds.

    Output argument is a boolean, true if the data is fresh enough, false if not."""

    logger.log("TODO", "TODO: 2) Create an index csv where we record each data fetch transaction. Col 1 is ticker code, Col 2 timestamp, Col 3 success bool. This will assist with the isDataFresh function.")
    logger.info("Complete isDataFresh method. This will require implimenting an index csv file.")

    ## Dummy for quick initial test:
    return False

