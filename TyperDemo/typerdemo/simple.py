"""Simple Typer app with two commands.

Demonstrates the use of the Typer object to create a command line application, 
and using default values."""

from typer import Typer

app = Typer()

@app.command()
def do_stuff(name: str) -> None:
    print(f"Hello, {name}")

@app.command()
def do_more(name: str ="Universe") -> None:
    print(f"Hello, {name}")

app()