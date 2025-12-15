from ui.menu_ui import show_menu
from ui.ui_helpers import (
    console, clear_screen, show_header, show_logo, print_error, print_success, 
    print_info, pause, show_divider, COLORS
)
from ui.intro_animation import play_intro_animation
from rich.panel import Panel
from rich.align import Align
from rich.text import Text
from logic.logic_layer_api import LogicLayerAPI
from ui.login_ui import show_login_screen
from ui.admin_ui import AdminUI
from ui.user_ui import UserUI
from ui.guest_ui import GuestUI


class MainUI:
    def __init__(self, logic_layer: LogicLayerAPI):
        self.logic_layer = logic_layer
        self.guest_ui = GuestUI(logic_layer)
        self.admin_ui = AdminUI(logic_layer)
        self.user_ui = UserUI(logic_layer)
        self.current_user = None
        self.current_role = None
    
    def run(self):
        """Main application loop with enhanced UI"""
        
        while True:
            clear_screen()
            show_logo()
            show_header("Main Menu", icon="🏠") 
            choice = show_menu()

            if choice == '1':
                user = show_login_screen(self.logic_layer)

                if user:
                    self.current_user = user

                    if user.role == 'admin':
                        clear_screen()
                        self.admin_ui.run(user)
                    else:
                        clear_screen()
                        self.user_ui.run(user)

                    

            elif choice == '2':
                clear_screen()
                self.guest_ui.run()
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
        pause()