from rich.console import Console
from rich.panel import Panel
from rich.live import Live
from rich.align import Align
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn
from rich.text import Text
from ui.ui_helpers import COLORS, clear_screen
import time

console = Console()


def play_intro_animation():
    """Play an enhanced intro animation with progress indicators"""
    clear_screen()
    
    # Animated logo reveal
    logo_lines = [
        "        ███╗   ███╗██╗███╗   ██╗██╗    ██████╗  █████╗ ███╗   ██╗██╗  ██╗",
        "        ████╗ ████║██║████╗  ██║██║    ██╔══██╗██╔══██╗████╗  ██║██║ ██╔╝",
        "        ██╔████╔██║██║██╔██╗ ██║██║    ██████╔╝███████║██╔██╗ ██║█████╔╝ ",
        "        ██║╚██╔╝██║██║██║╚██╗██║██║    ██╔══██╗██╔══██║██║╚██╗██║██╔═██╗ ",
        "        ██║ ╚═╝ ██║██║██║ ╚████║██║    ██████╔╝██║  ██║██║ ╚████║██║  ██╗",
        "        ╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝╚═╝    ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝",
    ]
    
    # Reveal logo line by line
    for i, line in enumerate(logo_lines, 1):
        console.print(f"[{COLORS['primary']}]{line}[/{COLORS['primary']}]")
        time.sleep(0.1)
    
    console.print(f"\n[bold {COLORS['accent']}]              🏦 BANKING SYSTEM 🏦[/bold {COLORS['accent']}]\n")
    time.sleep(0.3)
    
    # Loading sequence with progress bar
    tasks = [
        ("🔐 Initializing security protocols", 0.4),
        ("🔗 Establishing secure connection", 0.5),
        ("💾 Loading user database", 0.3),
        ("🏦 Preparing banking services", 0.4),
        ("✓ System ready", 0.3),
    ]
    
    with Progress(
        SpinnerColumn(spinner_name="dots"),
        TextColumn("[progress.description]{task.description}"),
        BarColumn(bar_width=40),
        console=console,
    ) as progress:
        for task_name, duration in tasks:
            task = progress.add_task(f"[{COLORS['primary']}]{task_name}", total=100)
            
            for _ in range(100):
                progress.update(task, advance=1)
                time.sleep(duration / 100)
            
            time.sleep(0.1)
    
    console.print(f"\n[bold {COLORS['success']}]✓ Welcome to Mini Bank! Press Enter to continue...[/bold {COLORS['success']}]")
    console.input()
    


