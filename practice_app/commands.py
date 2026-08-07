import click

@click.command("hello")
def hello():
    """Print a greeting from the Bench CLI"""
    click.echo("Hello from the custom Bench CLI!")
commands = [hello]