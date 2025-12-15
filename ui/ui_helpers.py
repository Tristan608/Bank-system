from rich.console import Console
from rich.panel import Panel
from rich.align import Align
from rich.text import Text
from rich.box import DOUBLE, ROUNDED, HEAVY
from rich.rule import Rule
from rich import box

console = Console()

# Color scheme - Modern cyan/blue gradient theme
COLORS = {
    "primary": "blue",
    "secondary": "bright_blue",
    "accent": "bright_blue",
    "success": "bright_green",
    "warning": "yellow",
    "error": "bright_red",
    "info": "bright_magenta",
    "muted": "grey70",
    "border": "bright_blue"
}

def clear_screen():
    console.clear()

def print_error(message: str):
    console.print(f"\n[{COLORS['error']}]╳ {message}[/{COLORS['error']}]")

def print_success(message: str):
    console.print(f"\n[{COLORS['success']}]✓ {message}[/{COLORS['success']}]")

def print_info(message: str):
    console.print(f"\n[{COLORS['info']}]ℹ {message}[/{COLORS['info']}]")

def print_warning(message: str):
    console.print(f"\n[{COLORS['warning']}]⚠ {message}[/{COLORS['warning']}]")

def pause():
    console.input(f"\n[{COLORS['muted']}]⏎ Press Enter to continue...[/{COLORS['muted']}]")

def show_divider(title: str = ""):
    """Show a stylized divider line"""
    console.print(Rule(title, style=COLORS['border']))

# Modern minimalist logo
LOGO = """
╔═════════════════════════════════════════════════════════════════════════╗
║                                                                         ║
║     ███╗   ███╗██╗███╗   ██╗██╗    ██████╗  █████╗ ███╗   ██╗██╗  ██╗   ║
║     ████╗ ████║██║████╗  ██║██║    ██╔══██╗██╔══██╗████╗  ██║██║ ██╔╝   ║
║     ██╔████╔██║██║██╔██╗ ██║██║    ██████╔╝███████║██╔██╗ ██║█████╔╝    ║
║     ██║╚██╔╝██║██║██║╚██╗██║██║    ██╔══██╗██╔══██║██║╚██╗██║██╔═██╗    ║
║     ██║ ╚═╝ ██║██║██║ ╚████║██║    ██████╔╝██║  ██║██║ ╚████║██║  ██╗   ║
║     ╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝╚═╝    ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝   ║
║                                                                         ║
║                          🏦 BANKING SYSTEM 🏦                           ║
║                                                                         ║
╚═════════════════════════════════════════════════════════════════════════╝
"""

def show_logo():
    """Display the main application logo with enhanced styling"""
    text = Text()
    text.append(LOGO, style=f"bold {COLORS['primary']}")
    
    panel = Panel(
        Align.center(text),
        subtitle=f"[{COLORS['accent']}]🔒 Secure • Reliable • Fast[/{COLORS['accent']}]",
        border_style=COLORS['border'],
        box=DOUBLE,
        padding=(0, 2),
    )
    console.print(panel)
    console.print()  # Add spacing

def show_header(title: str, subtitle: str | None = None, icon: str = "📋"):
    """Display a section header with optional subtitle and icon"""
    header_text = Text()
    header_text.append(f"{icon}  ", style=COLORS['accent'])
    header_text.append(title, style=f"bold {COLORS['primary']}")
    
    panel = Panel(
        Align.center(header_text),
        subtitle=subtitle if subtitle else None,
        border_style=COLORS['border'],
        box=ROUNDED,
        padding=(1, 2)
    )
    console.print(panel)
    console.print()  # Add spacing

def show_welcome_message(user_name: str, role: str):
    """Display personalized welcome message"""
    role_icons = {
        "admin": "👑",
        "user": "👤",
        "guest": "👥"
    }
    icon = role_icons.get(role.lower(), "👤")
    
    welcome_text = Text()
    welcome_text.append(f"{icon} Welcome back, ", style=COLORS['muted'])
    welcome_text.append(user_name, style=f"bold {COLORS['accent']}")
    welcome_text.append(f" ({role.title()})", style=COLORS['primary'])
    
    console.print(Panel(
        Align.center(welcome_text),
        border_style=COLORS['success'],
        box=ROUNDED,
        padding=(0, 2)
    ))
    console.print()

def format_currency(amount: float) -> str:
    """Format amount as currency"""
    return f"${amount:,.2f}"

def show_balance(balance: float):
    """Display account balance with special styling"""
    balance_text = Text()
    balance_text.append("💰 Current Balance: ", style=COLORS['muted'])
    balance_text.append(format_currency(balance), style=f"bold {COLORS['success']}")
    
    console.print(Panel(
        Align.center(balance_text),
        border_style=COLORS['accent'],
        box=ROUNDED,
        padding=(0, 2)
    ))
    console.print()

def full_width_box(content: str):
    panel = Panel(
        Align.left(content),
        border_style=COLORS['border'],
        box=box.ROUNDED,       # or ROUNDED, HEAVY, etc.
        padding=(1, 2),
        expand=True       # makes it fit the full console width
    )
    console.print(panel)




