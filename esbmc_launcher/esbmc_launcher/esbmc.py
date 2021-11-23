"""Main module."""

class EsbmcLauncher:
    """Configurations, setup and launch of ESBMC"""

    def __init__(self, esbmc_bin="esbmc"):
        self.esbmc_bin = esbmc_bin
        self.files = []
        self.args = []

    def load_json_args(self, json_file: str):
        """Loads a json file as esbmc options"""
        pass

    def show_loops(self):
        pass

    def show_goto_program(self):
        pass

    @staticmethod
    def get_esbmc() -> str:
        windows_link = "https://github.com/esbmc/esbmc/releases//latest/download/ESBMC-Windows.zip"
        macos_link = "https://github.com/esbmc/esbmc/releases/latest/download/ESBMC-Darwin.sh"
        linux_link = "https://github.com/esbmc/esbmc/releases/latest/download/ESBMC-Linux.sh"
        return linux_link

    def run(self):
        pass
