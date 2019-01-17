from loguru import logger
import pandas as pd
import os


def init():
    logger.info("Initializing dataProcess")

    dirName = "../data"
    if not os.path.exists(dirName):
        os.mkdir(dirName)
        logger.info("Directory ", dirName, " Created ")
    else:
        logger.info("Directory ", dirName, " already exists")


def sma(df, period):
    """Function calculate the simple moving average for a specified nuber of days, based on the closing prince.

    Input arguments are df, the dataframe of markets data, and
    days, the number of days of SMA required.

    Output is the dataframe with an additional column with new SMA data."""

    logger.info(f"Calculating the SMA of {period} periods.")

    logger.log("TODO", "2) Check if the column already exist, and reuse that column.")
    logger.log("TODO", "2) Rewrite to pull in the Alpha Vantage SMA data.")

    colname = "SMA" + str(period)

    newcol = df['Close'].rolling(period).mean()

    df[colname] = newcol

    return df



