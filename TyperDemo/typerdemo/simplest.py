"""The simplest Typer app."""

import typer

def main(name: str) -> None:
    typer.echo(f"Hello, {name}")

if __name__ == "__main__":
    typer.run(main)