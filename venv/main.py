from loguru import logger
from alpha_vantage.timeseries import TimeSeries
import os

import universe
import dataHandling as DH
import settings

logger.info("Starting " + __file__ )


def initialize():
    logger.info("Initializing and loading settings.")

    todoLogLevel = logger.level("TODO", no=10, color="<blue>")
    logger.info(f"Additional log level added for TODO: {todoLogLevel}")

    ts = TimeSeries(key=os.environ['ALPHAVANTAGE_API_KEY'])

    universe.init()
    DH.init()
    settings.init()

    outstandingIndices = []
    populatedIndices = []

    dataToSave = []

    settings.loadSettings()
    if settings.debugLevel:
        uni = universe.testUniverse()
    else:
        uni = universe.holdings()
    logger.info(f"Universe set to {uni}")

    return outstandingIndices, populatedIndices, uni, dataToSave, ts


if __name__ == "__main__":
    """Run the main program step here

    Step 1: See if any data is (a) populated, and (b) fresh
    Step 2: Determine if any data is outstanding
    Step 3: Pull any outstanding data
    Step 4: Save the data to disk
    Step 5: Do data handling and parsing
    Step 6: Do analysis
    Step 7: Output to file
    Step 8: Output to dashboard"""

    # Initialize:
    outstandingIndices, populatedIndices, uni, dataToSave, ts = initialize()

    #Step 1a: See if any data is populated

    logger.log("TODO", "TODO: 4) Change over from CSV files to a proper database.")
    #Initially we'll do this with CSV's, but we'll port to DB's at some point.

    logger.info("Test if data is populated")

    logger.info("Iterate through the universe")
    for index in uni:
        logger.info(f"Test if {index} has a file populated")
        if DH.fileExists(index):
            logger.info(f"File exists for {index}")
            populatedIndices.append(index)
            logger.info(f"The list of populated indeces is now: {populatedIndices}")
        else:
            #Step 2: Determine if any data is outstanding
            logger.info(f"No file exists for {index}, so mark data as outstanding.")
            outstandingIndices.append(index)
            logger.info(f"The list of outstanding indeces is now: {outstandingIndices}")

    #Step 1b: See if populated data is fresh
    logger.info("Test if populated data is fresh.")

    logger.info("Iterate through the populated universe.")
    for index in populatedIndices:
        logger.info(f"Test if the data on disk for {index} if fresh.")
        if DH.isDataFresh(index,settings.maximumDataAge):
            logger.info(f"Data for {index} is fresh enough.")
        else:
            logger.info(f"Data for {index} is out of date, so add to the outstanding list.")
            outstandingIndices.append(index)
            logger.log("TODO", "TODO: 10) Remove the index from populatedIndices. I don't think that I'll use populatedIndices again in this script, but I should still do this at some point.")
            logger.info(f"The list of outstanding indeces is now: {outstandingIndices}")

    #Step 3: Pull any outstanding data
    logger.info("Pull any outstanding data.")
    for index in outstandingIndices:
        data = []
        meta_data = []

        logger.info(f"Download data for {index}.")
        data, meta_data = ts.get_intraday(index)
        if ((not data) and (not meta_data)):
            logger.critical(f"No data pulled down for {index}.")
        else:
            logger.info(f"Send the data and metadata for {index} to be saved to disk.")
            print(meta_data)
            DH.saveToDisk(index, meta_data, data)

