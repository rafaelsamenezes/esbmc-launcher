"""This file contains all the print functions used"""

from rich.console import Console
from rich.style import Style


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
    def print(msg: str, mode):
        Message.console.log(msg, style=mode)

    @staticmethod
    def error(msg: str):
        Message.print(msg, Message.error_style)

    @staticmethod
    def warning(msg: str):
        Message.print(msg, Message.warning_style)

    @staticmethod
    def status(msg: str):
        Message.print(msg, Message.status_style)

    @staticmethod
    def debug(msg: str):
        Message.print(msg, Message.debug_style)

    @staticmethod
    def verbose(msg: str):
        Message.print(msg, Message.verbose_style)

