"""Console script for esbmc_launcher."""
import sys
import click
from soot_wrapper import SootWrapper
from esbmc import EsbmcLauncher
import printable
from download import download
import utils


def check_soot():
    printable.verbose("Checking requirements")
    SootWrapper.check_requirements()


def download_dependencies():
    printable.verbose("Downloading dependencies")
    download([SootWrapper.get_soot_link(), EsbmcLauncher.get_esbmc()], ".")


@click.command()
@click.option('--doctor', is_flag=True, help="Check if the environment is ready.")
@click.option('--get-dependencies', is_flag=True, help="Download any external dependencies.")
@click.option('--esbmc-path', default="esbmc", help="ESBMC tool path")
@click.option('--soot-path', default="soot.jar", help="Soot jar path")
@click.argument('inputs', nargs=-1)
def cli(doctor, esbmc_path, soot_path, get_dependencies, inputs):
    printable.status("Starting ESBMC Launcher")
    if get_dependencies:
        download_dependencies()
        return 0
    if doctor:
        check_soot()
        return 0

    printable.debug(f"Inputs: {inputs}")
    if len(inputs) == 0:
        printable.error("Didn't receive any file inputs (expecting .c, .java, .kt or .apk)")
        return -1
    
    if utils.Mode.getmode(inputs[0]) == utils.Mode.KT_FILE:
        sootWrapper = SootWrapper()
        sootWrapper.generate_jimple(inputs)

    from subprocess import run
    run(["../esbmc/esbmc.exe", "--incremental-bmc", "ast.jimple"])

if __name__ == "__main__":
    sys.exit(cli())  # pragma: no cover
