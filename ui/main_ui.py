from ui.menu_ui import show_menu
from ui.ui_helpers import (
    console, clear_screen, show_logo, print_error, print_success, 
    print_info, pause, show_divider, COLORS
)
from ui.intro_animation import play_intro_animation
from rich.panel import Panel
from rich.align import Align
from rich.text import Text
from logic.logic_layer_api import LogicLayerAPI
from ui.login_ui import show_login_screen


class MainUI:
    def __init__(self, logic_layer: LogicLayerAPI):
        self.logic_layer = logic_layer
        self.current_user = None
        self.current_role = None
    
    def run(self):
        """Main application loop with enhanced UI"""
        
        while True:
            clear_screen()
            show_logo()
            choice = show_menu()

            if choice == '1':
                user = show_login_screen(self.logic_layer)

                if user:
                    self.current_user = user

                    if user.role == 'admin':
                        self.run_admin_ui()
                    else:
                        self.run_user_ui()
                    

            elif choice == '2':
                self.continue_as_guest()
            elif choice == 'E' or choice == 'e':
                self.exit_application()
                break
            else:
                print_error("Invalid choice. Please select 1, 2, or E.")
                pause()

    
   
    def exit_application(self):
        """Display farewell message and exit"""
        clear_screen()
        
        farewell_text = Text()
        farewell_text.append("\n\n")
        farewell_text.append("Thank you for using Mini Bank!\n\n", style=f"bold {COLORS['primary']}")
        farewell_text.append("Your trusted banking partner.\n", style=COLORS['muted'])
        farewell_text.append("See you soon! 👋\n\n", style=COLORS['accent'])
        
        panel = Panel(
            Align.center(farewell_text),
            border_style=COLORS['success'],
            padding=(1, 4)
        )
        console.print(panel)
        console.print()
