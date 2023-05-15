from typer import Typer

app = Typer()

@app.command()
def do_stuff(name: str) -> None:
    print(f"Hello, {name}")

@app.command()
def do_more(name: str ="Universe") -> None:
    print(f"Hello, {name}")

app()