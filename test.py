from log4py.log4py import logger

log = logger(prefix="Log4py", useColor=True, logFile="./latest.log")

log.success("successful")
log.info("information")
log.warn("warning")
log.error("exception")
