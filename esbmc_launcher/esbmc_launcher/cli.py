"""Console script for esbmc_launcher."""
import sys
import click
from soot_wrapper import SootWrapper
from esbmc import EsbmcLauncher
from printable import Message
from download import download


def check_soot():
    Message.verbose("Checking requirements")
    SootWrapper.check_requirements()


def download_dependencies():
    Message.verbose("Downloading dependencies")
    download([SootWrapper.get_soot_link(), EsbmcLauncher.get_esbmc()], ".")


@click.command()
@click.option('--doctor', is_flag=True, help="Check if the environment is ready.")
@click.option('--get-dependencies', is_flag=True, help="Download any external dependencies.")
@click.option('--esbmc-path', default="esbmc", help="ESBMC tool path")
@click.option('--soot-path', default="soot.jar", help="Soot jar path")
@click.argument('inputs', nargs=-1)
def cli(doctor, esbmc_path, soot_path, get_dependencies, inputs):
    Message.status("Starting ESBMC Launcher")
    if get_dependencies:
        download_dependencies()
        return 0
    if doctor:
        check_soot()
        return 0

    Message.debug(f"Inputs: {inputs}")
    # TODO: select mode
    sootWrapper = SootWrapper()
    sootWrapper.generate_jimple(inputs)

if __name__ == "__main__":
    sys.exit(cli())  # pragma: no cover
