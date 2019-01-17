from loguru import logger
from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.techindicators import TechIndicators
import os
import pandas as pd

import universe
import dataDownload as dataDl
import dataProcess as dataP

from drawup import drawmain

import settings


logger.info("Starting " + __file__)


def initialize():
    logger.info("Initializing and loading settings.")

    todo_log_level = logger.level("TODO", no=10, color="<blue>")
    logger.info(f"Additional log level added for TODO: {todo_log_level}")

    init_ts = TimeSeries(key=os.environ['ALPHAVANTAGE_API_KEY'], output_format='pandas', indexing_type='date')
    init_tech = TechIndicators(key=os.environ['ALPHAVANTAGE_API_KEY'], output_format='pandas', indexing_type='date')

    universe.init()
    dataDl.init()
    dataP.init()
    settings.init()

    outstanding_indices = []
    populated_indices = []

    data_to_save = []

    settings.loadSettings()
    if settings.debugLevel:
        init_uni = universe.testUniverse()
    else:
        init_uni = universe.holdings()
    logger.info(f"Universe set to {init_uni}")

    return outstanding_indices, populated_indices, init_uni, data_to_save, init_ts, init_tech


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
    outstandingIndices, populatedIndices, uni, dataToSave, ts, tech = initialize()

    # Step 1a: See if any data is populated

    logger.log("TODO", "TODO: 4) Implement local database.")
    # Initially we'll do this with CSV's, but we'll port to DB's at some point.

    logger.info("Test if data is populated")

    logger.info("Iterate through the universe")
    for index in uni:
        logger.info(f"Test if {index} has a file populated")
        if dataDl.fileexists(index):
            logger.info(f"File exists for {index}")
            populatedIndices.append(index)
            logger.info(f"The list of populated indeces is now: {populatedIndices}")
        else:
            # Step 2: Determine if any data is outstanding
            logger.info(f"No file exists for {index}, so mark data as outstanding.")
            outstandingIndices.append(index)
            logger.info(f"The list of outstanding indeces is now: {outstandingIndices}")

    # Step 1b: See if populated data is fresh
    logger.info("Test if populated data is fresh.")

    logger.info("Iterate through the populated universe.")
    for index in populatedIndices:
        logger.info(f"Test if the data on disk for {index} if fresh.")
        if dataDl.isdatafresh(index, settings.maximumDataAge):
            logger.info(f"Data for {index} is fresh enough.")
        else:
            logger.info(f"Data for {index} is out of date, so add to the outstanding list.")
            outstandingIndices.append(index)
            logger.log("TODO", "TODO: 10) Remove the index from populatedIndices. I don't think that I'll use"
                               " populatedIndices again in this script, but I should still do this at some point.")
            logger.info(f"The list of outstanding indices is now: {outstandingIndices}")

    # Step 3: Pull any outstanding data
    logger.info("Pull any outstanding data.")
    for index in outstandingIndices:
        logger.info(f"Download data for {index}.")

        data, meta_data = ts.get_daily(index)

        if (data.empty) and (meta_data.empty):
            logger.critical(f"No data pulled down for {index}.")
        else:
            logger.info(f"Clean out the data for {index}")
            # Step 5: Do data handling and parsing
            data = dataDl.cleanclosedata(data)
            logger.info(f"Send the data and metadata for {index} to be saved to disk.")

        # Step 6: Do analysis
        # Write a couple of analysis functions, start with Simple Moving Average, year-on-year growth on a specific date.
        SMA15, meta_data = tech.get_sma(index, time_period=15)
        data['SMA015'] = SMA15
        SMA50, meta_data = tech.get_sma(index, time_period=50)
        data['SMA050'] = SMA50
        SMA200, meta_data = tech.get_sma(index, time_period=200)
        data['SMA200'] = SMA200

        # Step 4: Save the data to disk
        # Also:
        # Step 7: Output to file
        # Output all analysis and resulting signals to a new file.
        dataDl.savetodisk(index, data)

    for index in uni:
        import time
        time.sleep(0.1)  # Just to ensure that our output is neat

        data = dataDl.loadfile(index)

        # print(data.head())
        # print()
        # print()
        # print(data.close)

        # data.info()

        drawmain.drawtest(data)




    # Step 8: Output to dashboard
    # Load up output file
    # Process data into dashboard information
    # Write to  dashboard