"""Intermediate Typer demo.

Demonstrates more complex data types, and annotations for options and arguments.
"""
from pathlib import Path
from enum import Enum
from typing import Annotated

import typer

app = typer.Typer()

class ModelName(str, Enum):
    resnet = "resnet"
    alexnet = "alexnet"
    vgg = "vgg"


@app.command()
def train_test(
    data_dir: Path,
    model: ModelName = ModelName.resnet,
    setup_file: Annotated[Path, typer.Option(exists=True)] = Path("setup.yml"),
    gamma: float = 1.2,
) -> None:
    print(f"Training on {data_dir} with {setup_file} and lambda={gamma}")

@app.command()
def sanity_check(data_dir: Path) -> None:
    """Sanity check the data in data_dir."""
    print(f"Sanity checking {data_dir}")

app()