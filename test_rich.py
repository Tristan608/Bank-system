from rich.console import Console
from rich.panel import Panel
from rich.columns import Columns
from rich import box

console = Console()

styles = [
    ("SQUARE", box.SQUARE),
    ("ROUNDED", box.ROUNDED),
    ("DOUBLE", box.DOUBLE),
    ("HEAVY", box.HEAVY),
    ("MINIMAL", box.MINIMAL),
    ("MINIMAL_HEAVY", box.MINIMAL_HEAVY_HEAD),
    ("SIMPLE", box.SIMPLE),
    ("SIMPLE_HEAD", box.SIMPLE_HEAD),
    ("ASCII", box.ASCII),
    ("ASCII_DOUBLE_HEAD", box.ASCII_DOUBLE_HEAD),
    ("HORIZONTALS", box.HORIZONTALS),
]

panels = [
    Panel(f"{name}\n(Example content)", box=style, border_style="cyan", padding=(1, 2), expand=True)
    for name, style in styles
]

console.print(Columns(panels, expand=True))