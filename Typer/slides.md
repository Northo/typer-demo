---
# try also 'default' to start simple
theme: seriph
# random image from a curated Unsplash collection by Anthony
# like them? see https://unsplash.com/collections/94734566/slidev
background: https://source.unsplash.com/collection/94734566/1920x1080
# apply any windi css classes to the current slide
class: 'text-center'
# https://sli.dev/custom/highlighters.html
highlighter: shiki
# show line numbers in code blocks
lineNumbers: false
# some information about the slides, markdown enabled
info: |
  ## Slidev Starter Template
  Presentation slides for developers.

  Learn more at [Sli.dev](https://sli.dev)
# persist drawings in exports and build
drawings:
  persist: false
# page transition
transition: slide-left
# use UnoCSS
css: unocss
addons:
  - "@lehoczky/vue-termynal"
---

# Typer CLI
Tools meetup May 15th

---
layout: center
---

<div class="p-10 text-2xl rounded bg-gray-500">
Typer, build great CLIs. Easy to code. Based on Python type hints.
</div>

<!--
Created by tiangolo, aka the fast api guy
-->

---

# Demo

<img class="w-2/3 pt-20 mx-auto" src="/demo.gif" />

---

<div class="columns-2">

# What

- Modern Click ( which is modern Argparse (ish) )
- Little to no extra code

# Why
- Explicit
- User friendly

</div>

<!--
Explicit: as opposed to for example use environment variables
-->

---

# Getting started

<v-termynal class="mt-20" forward-button restart-button lazy typeDelay="50" progressDelay="20" lineDelay="1000">
  <vt-input>pip install typer[all]</vt-input>
  <vt-progress />
  <vt-text>Successfully installed typer</vt-text>
</v-termynal>

---

# Getting started

<div class="columns-2">

```python{3-4|all}
import typer

def main(name: str) -> None:
  print(f"Hello, {name}")

typer.run(main)
```
<v-template v-click>

```
$ python simple.py

Usage: simple.py [OPTIONS] NAME
Try 'simple.py --help' for help.
╭─ Error ────────────────────────────────────────╮
│ Missing argument 'NAME'.                       │
╰────────────────────────────────────────────────╯

$ python simple.py Foo

Hello, Foo
```
</v-template>
</div>

---

# Getting started

<div class="columns-2">

```python {8-9|1-7|all}
# simple.py
from typer import Typer


app = Typer()

@app.command()
def do_stuff(name: str) -> None:
  print(f"Hello, {name}")

app()
```

<v-template v-click>

```
$ python simple.py

Usage: simple.py [OPTIONS] NAME
Try 'simple.py --help' for help.
╭─ Error ────────────────────────────────────────╮
│ Missing argument 'NAME'.                       │
╰────────────────────────────────────────────────╯

$ python simple.py Foo

Hello, Foo
```

</v-template>
</div>

---

# Getting started

<div class="columns-2">

```python
# simple.py
from typer import Typer


app = Typer()

@app.command()
def do_stuff(name: str) -> None:
  print(f"Hello, {name}")

@app.command()
def do_more(name: str = "Universe") -> None:
    print(f"Hello, {name}")

app()
```

<v-template v-click>

```
$ python simple.py

Usage: simple.py [OPTIONS] COMMAND [ARGS]...
Try 'simple.py --help' for help.
╭─ Error ────────────────────────────────────────╮
│ Missing command.                               │
╰────────────────────────────────────────────────╯

$ python simple.py --help

....

╭─ Commands ─────────────────────────────────────╮
│ do-more                                        │
│ do-stuff                                       │
╰────────────────────────────────────────────────╯

$ python simple.py do-more

Hello, Universe
```

</v-template>
</div>
---

# ✨ Auto completions ✨

<v-termynal class="mt-20" restart-button lazy lineDelay="500" typeDelay="50">
  <vt-input>pip install typer-cli</vt-input>
  <vt-progress />
  <vt-text>Successfully installed typer-cli</vt-text>
</v-termynal>

---

# ✨ Auto completions ✨

- <material-symbols-sentiment-sad-rounded /> `typer-cli` does not support newest `Typer`
- Installable package with scripts

```toml
# pyproject.toml

...
[tool.poetry.scripts]
rick-portal-gun = "rick_portal_gun.main:app"
```

---

# Intermediate

```python{all|9|10|11|all}
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
```
---

# Intermediate

<div class="columns-2">

```python
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
```

<v-template v-click>

```
 Usage: list_input.py [OPTIONS]                                   
                                                                  
╭─ Options ──────────────────────────────────────────────╮
│ --numbers          INTEGER  [default: None]            │
│ --metric   -m      TEXT     [default: None]            │
│ --help                      Show this message and exit.│
╰────────────────────────────────────────────────────────╯

$ list_input -m MCC -m norm --metric bar
Numbers: []
Metrics: ['MCC', 'norm', 'bar']
```

</v-template>
</div>

---
transition: fade
---

# Difference to Click

The function is left as-is.
We don't have to modify it, beyond annotating the types.

```python
@typer_app.command()
def handle_taco_form(user_id: int, number_of_tacos: int) ->  dict:
  """Register a user order for tacos."""
  return my_shadow_api.order_tacos(
    user_id=user_id,
    number_of_tacos=number_of_tacos,
  )

def some_other_function():
  user_id = users["thorvald"].id
  handle_taco_form(user_id, 42)
```

---

# Difference to Click

The function is left as-is.
We don't have to modify it, beyond annotating the types.

```python
@flask_app.put("/tacos/{user_id}/{number_of_tacos}")
@typer_app.command()
def handle_taco_form(user_id: int, number_of_tacos: int) ->  dict:
  """Register a user order for tacos."""
  return my_shadow_api.order_tacos(
    user_id=user_id,
    number_of_tacos=number_of_tacos,
  )
```

---
layout: image-right
image: https://source.unsplash.com/collection/94734566/1920x1080
---

# Other features

- <carbon-chart-custom /> Custom types
- <material-symbols-terminal-rounded /> Scripts
- <pajamas-progress /> Progress bars
- <material-symbols-question-exchange /> Prompts
- ✨ Nice help section with Rich & Md