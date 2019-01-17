from loguru import logger

# How to use from other scripts:
# import settings
# ensure loadSettings() is called from main.

def init():
    logger.log("TODO", "TODO: 4) Add saveSettings of updateSetting or something similar. Right now we can only change settings by manually changing this file!")

# Steps to add a new settings value:
# Step 1: Populate limits and defaults here and initialize:
debugLevelDefault = False
debugLevel = False

maximumDataAgeLowerLimit = 60 # Seconds
maximumDataAgeDefault = 4*60*60 # Seconds
maximumDataAgeUpperLimit = 24*60*60 #Seconds
maximumDataAge = maximumDataAgeDefault

# Step 2: Add a setXXXToDefault function here:
def setMaximumDataAgeToDefault():
    logger.info(f"Maximum age of date is being set to {maximumDataAgeDefault} seconds.")
    maximumDataAge = maximumDataAgeDefault

def setDebugLevelToDefault():
    logger.info(f"Debug level is being set to {maximumDataAgeDefault}.")
    debugLevel = debugLevelDefault

# Step 3: Add a call to the setXXXToDefault function in the init function here:
def initSettings():
    logger.info("Settings are all being set to default.")
    setMaximumDataAgeToDefault()
    setDebugLevelToDefault()

def loadSettings():
    logger.info("loadSettings function")

    logger.info("First initialize all the settings.")
    initSettings()

    logger.info("Now load settings from file in order to overwrite the defaults, where applicable.")
    logger.log("TODO","TODO: 3) Load settings file here.")

# Step 4: Add a line printing the current value of the setting to console for debug purposes.
def printSettings():
    logger.debug("---Settings dump---")
    logger.debug(f"Maximum Age of that a data csv is allowed to be: {maximumDataAge}")