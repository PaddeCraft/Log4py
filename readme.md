![GitHub repo size](https://img.shields.io/github/repo-size/PaddeCraft/Log4py?label=total%20size) ![Lines of code](https://img.shields.io/tokei/lines/github/PaddeCraft/Log4py) ![GitHub issues](https://img.shields.io/github/issues-raw/PaddeCraft/Log4py?label=issues)

# Log4py

Log4py is a simple logging package written in python. It´s very simple to use, and only consists of one class.

## Example:

```py
from log4py.log4py import logger

log = logger(prefix="Log4py", useColor=False, logFile="./latest.log")

log.success("successful")
log.info("information")
log.warn("warning")
log.error("exception")
```
```
[Log4py] [11:51] [SUCCSESS]  successful
[Log4py] [11:51] [INFO]      information
[Log4py] [11:51] [WARN]      warning    
[Log4py] [11:51] [ERROR]     exception
```