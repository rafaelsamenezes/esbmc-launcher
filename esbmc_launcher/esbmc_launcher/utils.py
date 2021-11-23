"""Some utilities for all modules"""

from download import download
def is_available(name):
    """Check whether `name` is on PATH and marked as executable."""
    from shutil import which
    tool_path = which(name)
    if not tool_path:
        tool_path = which(name + ".exe")
    if not tool_path:
        return None
    return tool_path



