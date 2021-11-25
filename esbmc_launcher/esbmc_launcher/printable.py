"""This file contains all the print functions used"""

from rich.console import Console
from rich.style import Style
from functools import partial

class Message:

    """
       0 - Error only
       1 - Warning + 0
       2 - Status + 1
       3 - Progress + 2
       4 - Verbose + 3
       5 - Debug + 4
    """
    VERBOSITY = 5

    error_style = Style(color="red", bold=True)
    warning_style = Style(color="yellow", bold=False)
    status_style = Style(color="green", bold=False)
    progress_style = Style(color="blue", bold=False)
    verbose_style = Style(color="white", bold=False)
    debug_style = Style(color="cyan", bold=False)

    console = Console()

    @staticmethod
    def print(mode, msg: str):
        Message.console.print(msg, style=mode)

    @staticmethod
    def getlog(mode):
        return partial(Message.print, mode)

error = Message.getlog(Message.error_style)
warning = Message.getlog(Message.warning_style)
status =  Message.getlog(Message.status_style)
debug =Message.getlog(Message.debug_style)
verbose = Message.getlog(Message.verbose_style)

