from typing import Annotated
import typer
from enum import Enum
from pathlib import Path

class ModelName(str, Enum):
    resnet = "resnet"
    alexnet = "alexnet"
    vgg = "vgg"

app = typer.Typer()

@app.command()
def demo(
    data_dir: Annotated[Path, typer.Argument(..., exists=True)],
    model: Annotated[ModelName, typer.Option()],
    experiment_name: Annotated[str, typer.Option(prompt=True)],
):
    typer.echo(f"Training {model} on {data_dir} with experiment name {experiment_name}")

if __name__ == "__main__":
    app()