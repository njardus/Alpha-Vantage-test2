"""universe.py contains a list of all stocks or indicators we consider for analysis.
This is limited by alpha_vantage's universe right now, but it does contain JSE and some crypto's, so it's a good
starting point."""

from loguru import logger


def init():
    logger.log("TODO", "TODO: 5) Rebuild with a) the entire JSE, b) My watchlist, c) my holdings")
    logger.log("TODO", "TODO: 99) New stocks will be listed from time to time. We should automate a universe of 'new' stocks.")


def universe():
    # SP500
    universe = [ 'AMD', 'AAPL', 'GOOGL', 'ABC', 'AMZN']
    return universe


def holdings():
    universe = ["TBS.JO", "CLS.JO", "AVI.JO", "AFX.JO", "SNT.JO", "FSR.JO", "MNK.JO", "CPI.JO", "IMP.JO", "TKG.JO",
                "SPP.JO", "NPN.JO", "MTA.JO", "MND.JO"]
    return universe


def testUniverse():
    universe = ["CPI.JO", "NPN.JO"]
    return universe