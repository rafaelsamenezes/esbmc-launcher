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


class Mode:    
    C_FILE = 0
    KT_FILE = 1
    JAVA_FILE = 2
    APK_FILE = 3

    _MODES = {
        ".c": C_FILE,
        ".h": C_FILE,
        ".kt": KT_FILE,
        ".java": JAVA_FILE,
        ".apk": APK_FILE
    }

    @staticmethod
    def getmode(input: str):
        import os
        _, file_extension = os.path.splitext(input)
        return Mode._MODES[file_extension]