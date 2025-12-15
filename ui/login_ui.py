from logic.logic_layer_api import LogicLayerAPI
from ui.ui_helpers import (
    console,
    clear_screen,
    show_header,
    print_error,
    print_success,
    pause,
    COLORS
)
from rich.prompt import Prompt


def show_login_screen(logic_layer: LogicLayerAPI):
    """Display login screen and authenticate user"""

    clear_screen()
    show_header("User Login", icon="🔐")

    # --- Input ---
    try:
        user_id = str(Prompt.ask(
            f"[{COLORS['muted']}]User ID[/{COLORS['muted']}]"
        ))
        pin = str(Prompt.ask(
            f"[{COLORS['muted']}]PIN[/{COLORS['muted']}]",
            password=True
        ))
    except KeyboardInterrupt:
        return None  # user pressed Ctrl+C safely

    # --- Authentication ---
    user = logic_layer.login(user_id, pin)

    # --- Result ---
    if not user:
        print_error("Invalid User ID or PIN.")
        pause()
        return None

    print_success(f"Welcome back, {user.name}!")
    pause()
    return user




    