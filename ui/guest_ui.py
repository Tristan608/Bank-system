from ui.ui_helpers import console, clear_screen, show_header, COLORS, pause, full_width_box
from logic.logic_layer_api import LogicLayerAPI


class GuestUI:
    def __init__(self, logic_layer: LogicLayerAPI = None):
        self.ll = logic_layer


    def run(self):
        while True:
            clear_screen()
            show_header("Guest Access", icon="👤")

            options = "\n".join([
                " [1] 📖 View Bank Information",
                " [2] 📝 Read System Instructions",
                " ",
                " [E] 🚪 Exit to Main Menu"
            ])
            

            full_width_box(options)
            console.print()  # Add spacing

            choice = console.input(f"[{COLORS['muted']}]➡ Please select an option (1, 2, or E): [/{COLORS['muted']}]").strip()

            if choice == '1':
                self.view_bank_info()
            elif choice == '2':
                self.read_system_instructions()
            elif choice.upper() == 'E' or choice.lower() == 'e':
                break  # Exit to main menu
            else:
                console.print(f"[{COLORS['error']}]Invalid choice. Please select a valid option.[/{COLORS['error']}]")
                pause()
        
    def view_bank_info(self):
        clear_screen()
        info = self.ll.view_bank_info()
        # name, version, currency
        options = "\n".join([
            f"🏦 Bank Name: {info['name']}",
            f"🛠️ Version: {info['version']}",
            f"💰 Currency: {info['currency']}"
        ])
        full_width_box(options)
        pause()
    
    def read_system_instructions(self):
        clear_screen()
        instructions = self.ll.read_system_instructions()
        full_width_box(instructions)
        pause()
    

        
    

        

 

