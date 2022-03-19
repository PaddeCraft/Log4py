from rich import print
from log4py.stringGenerator import stringGenerator


class logger:
    def __init__(
        self,
        timeFormat="%H:%M",
        useColor=True,
        prefix="",
        logFile=None,
        colors={
            "success": "bright_green",
            "info": "bright_white",
            "warn": "bright_yellow",
            "error": "bright_red",
        },
    ):
        """
        Creates an logger instance.
        More information about time codes can be found here: https://cutt.ly/TSkPc2b
        More information about color codes can be found here: https://cutt.ly/7SkSoSC
        """
        self.timeFormat = timeFormat
        self.useColor = useColor
        self.successColor = colors["success"] if useColor else "bright_white"
        self.infoColor = colors["info"] if useColor else "bright_white"
        self.warnColor = colors["warn"] if useColor else "bright_white"
        self.errorColor = colors["error"] if useColor else "bright_white"
        self.prefix = prefix
        self.logFile = logFile

    def success(self, msg):
        print(stringGenerator(0, msg, self))

    def info(self, msg):
        print(stringGenerator(1, msg, self))

    def warn(self, msg):
        print(stringGenerator(2, msg, self))

    def error(self, msg):
        print(stringGenerator(3, msg, self))
