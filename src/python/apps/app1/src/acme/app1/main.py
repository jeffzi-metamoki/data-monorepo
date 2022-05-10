from pathlib import Path
from pydoc import describe
from .app1_module1 import app1_func1
import typer

app = typer.Typer(name="app1")


@app.command()
def main(
    conf: Path = typer.Argument(
        ...,
        exists=True,
        file_okay=True,
        readable=True,
        resolve_path=True,
        help="Config path",
    )
):
    typer.echo(f"Config file at {conf}")
    app1_func1()


if __name__ == "__main__":
    app()
