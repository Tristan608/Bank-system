from ui.ui_helpers import clear_screen, show_header, COLORS, pause, show_welcome_message, full_width_box
from logic.logic_layer_api import LogicLayerAPI
from rich.prompt import Prompt
from rich.console import Console
console = Console()


class AdminUI:
    def __init__(self, logic_layer: LogicLayerAPI):
        self.ll = logic_layer

     
    def run(self, admin):
        self.current_admin = admin
        while True:
            clear_screen()
            show_welcome_message(admin.name, role="admin")
            show_header("Admin Dashboard", icon="🛠️")

            options = "\n".join([
                "[1] 👤 Create User",
                "[2] 🏦 Create Account",
                "[3] 📋 View All Users",
                "[4] 📂 View All Accounts",
                "[L] 🔐 Logout"
            ])

            panel = full_width_box(options)
            
            console.print()  # Add spacing
            choice = console.input(f"[{COLORS['muted']}]➡ Please select an option (1-4, or L): [/{COLORS['muted']}]").strip()

            if choice == '1':
                self.create_user()
            elif choice == '2':
                self.create_account()
            elif choice == '3':
                self.view_all_users()
            elif choice == '4':
                self.view_all_accounts()
            elif choice.upper() == 'L' or choice.lower() == 'l':
                self.logout()
                break  # Exit the loop and return to main menu
            else:
                console.print(f"[{COLORS['error']}]Invalid choice. Please select a valid option.[/{COLORS['error']}]")
                pause()




    

    def create_user(self):
        clear_screen()
        show_header("Create New User", icon="👤")
        # new user enter name, pin, role
        user_name = Prompt.ask("Enter user name: ") 
        user_pin = Prompt.ask("Enter user PIN: ")
        user_role = Prompt.ask("Enter user role (admin/user): ")

        new_user = self.ll.create_user(user_name, user_pin, user_role)
        console.print()  # Add spacing

        if new_user:
            console.print(f"[{COLORS['success']}]User '{new_user.name}' created successfully with ID: {new_user.user_id}[/{COLORS['success']}]")
        else:
            console.print(f"[{COLORS['error']}]Failed to create user. Please try again.[/{COLORS['error']}]")
        pause()


    def create_account(self):
        clear_screen()
        show_header("Create New Account", icon="🏦")
        # new account enter user id, starting balance
        user_id = Prompt.ask("Enter User ID for the new account: ")
        starting_balance = float(Prompt.ask("Enter starting balance: "))

        new_account = self.ll.create_account(user_id, starting_balance)
        console.print()  # Add spacing
        if new_account:
            console.print(f"[{COLORS['success']}]Account created successfully with Account Number: {new_account.account_id}[/{COLORS['success']}]")
        else:
            console.print(f"[{COLORS['error']}]Failed to create account. Please try again.[/{COLORS['error']}]")
        pause()
        

    def view_all_users(self):
        clear_screen()
        show_header("All Users", icon="📋")

        users = self.ll.view_all_users()

        if not users:
            console.print(f"[{COLORS['muted']}]No users found.[/{COLORS['muted']}]")
            pause()
            return
        
        show_users = "\n".join([f"ID: {user.user_id} | Name: {user.name} | Role: {user.role}" for user in users])
        full_width_box(show_users)
        console.print()  # Add spacing
        pause()


    def view_all_accounts(self):
        clear_screen()
        show_header("All Accounts", icon="📂")

        accounts = self.ll.view_all_accounts()

        if not accounts:
            console.print(f"[{COLORS['muted']}]No accounts found.[/{COLORS['muted']}]")
            pause()
            return
        
        show_accounts = "\n".join([f"Account Number: {acc.account_id} | User ID: {acc.user_id} | Balance: ${acc.balance:,.2f}" for acc in accounts])
        full_width_box(show_accounts)
        console.print()  # Add spacing
        pause()


    def logout(self):
        pass



