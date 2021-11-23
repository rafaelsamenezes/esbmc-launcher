"""Console script for esbmc_launcher."""
import sys
import click


@click.command()
def main(args=None):
    """Console script for esbmc_launcher."""
    click.echo("Replace this message by putting your code into "
               "esbmc_launcher.cli.main")
    click.echo("See click documentation at https://click.palletsprojects.com/")
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
