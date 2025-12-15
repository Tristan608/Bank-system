from ui.ui_helpers import console, clear_screen, show_logo, show_header, COLORS, full_width_box
from rich.table import Table
from rich.panel import Panel
from rich.text import Text
from rich.columns import Columns
from rich.box import ROUNDED
from rich.align import Align


def show_menu():
    """Display the main menu with modern card-based design"""

    options = "\n".join([
        "[1] 🔐 Login",
        "[2] 👤 Continue as Guest",
        "",
        "[E] ❌ Exit"
    ])

    full_width_box(options)
    console.print()  # Add spacing
    choice = console.input(f"[{COLORS['muted']}]➡ Please select an option (1, 2, or E): [/{COLORS['muted']}]")
    return choice.strip()






