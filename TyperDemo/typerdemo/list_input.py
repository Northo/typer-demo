from typing import Optional, Annotated

import typer

def demo_list_input(
    numbers: Optional[list[int]] = None,
    metrics: Annotated[
        Optional[list[str]],
        typer.Option("--metric", "-m")
    ] = None,
) -> None:
    typer.echo(f"Numbers: {numbers}")
    typer.echo(f"Metrics: {metrics}")

if __name__ == "__main__":
    typer.run(demo_list_input)