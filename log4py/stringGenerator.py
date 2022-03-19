from log4py.timeGenerator import timeGenerator


def stringGenerator(logType, msg, loggerClass):
    t = timeGenerator(loggerClass.timeFormat)
    timeStr = (
        ("[bright_white]" if not loggerClass.useColor else "")
        + "["
        + t
        + "]"
        + ("[/bright_white]" if not loggerClass.useColor else "")
    )
    if logType == 0:
        colorStr = loggerClass.successColor
        typeStr = f" [[{colorStr}]SUCCSESS[/{colorStr}]] "
        fileTypeStr = " [SUCCSESS] "
    elif logType == 1:
        colorStr = loggerClass.infoColor
        typeStr = f" [[{colorStr}]INFO[/{colorStr}]]     "
        fileTypeStr = " [INFO]     "
    elif logType == 2:
        colorStr = loggerClass.warnColor
        typeStr = f" [[{colorStr}]WARN[/{colorStr}]]     "
        fileTypeStr = " [WARN]     "
    elif logType == 3:
        colorStr = loggerClass.errorColor
        typeStr = f" [[{colorStr}]ERROR[/{colorStr}]]    "
        fileTypeStr = " [ERROR]    "
    if not loggerClass.prefix == "":
        prefixStr = "[" + loggerClass.prefix + "] "
    else:
        prefixStr = ""
    if loggerClass.useColor == True:
        messageStr = f" [{colorStr}]{msg}[/{colorStr}]"
    else:
        messageStr = " " + msg
    if not loggerClass.logFile == None:
        with open(loggerClass.logFile, "a+", encoding="UTF-8") as logfile:
            logfile.write(prefixStr + "[" + t + "]" + fileTypeStr + msg + "\n")
    return prefixStr + timeStr + typeStr + messageStr
