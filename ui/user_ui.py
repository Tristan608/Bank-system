from models import user
from ui.ui_helpers import console, clear_screen, full_width_box, show_header, COLORS, pause, full_width_box 
from logic.logic_layer_api import LogicLayerAPI
from rich.prompt import Prompt


class UserUI:
    def __init__(self, logic_layer: LogicLayerAPI):
        self.ll = logic_layer
        self.current_user = None


    def run(self, user):
        self.current_user = user
        while True:
            clear_screen()
            show_header("User Dashboard", icon="👤")
            # view balance, deposit, withdraw, transfer, view transaction history, logout
            options = "\n".join([
                "[1] 💰 View Balance",
                "[2] ➕ Deposit Funds",
                "[3] ➖ Withdraw Funds",
                "[4] 🔄 Transfer Funds",
                "[5] 📜 View Transaction History",
                "[L] 🔐 Logout"
            ])
            full_width_box(options)
            console.print()  # Add spacing

            choice = console.input(f"[{COLORS['muted']}]➡ Please select an option (1-5, or L): [/{COLORS['muted']}]").strip()

            if choice == '1':
                self.view_balance()
            elif choice == '2':
                self.deposit()
            elif choice == '3':
                self.withdraw()
            elif choice == '4':
                self.transfer()
            elif choice == '5':
                self.view_transaction_history()
            elif choice.upper() == 'L' or choice.lower() == 'l':
                self.logout()
                break  # Exit to main menu
            else:
                console.print(f"[{COLORS['error']}]Invalid choice. Please select a valid option.[/{COLORS['error']}]")
                pause()

            

    def view_balance(self):
        clear_screen()
        show_header("Account Balance", icon="💰")
        user_id = None  # You would get the user ID from the logged-in user context
        balance = self.ll.view_balance(user_id)
        options = f"💰 Your current balance is: ${balance}"
        full_width_box(options)
        pause()

    def deposit(self):
        clear_screen()
        show_header("Deposit Funds", icon="➕")

        my_accounts = self.ll.get_user_account(self.current_user.user_id)
        if not my_accounts:
            console.print(f"[{COLORS['error']}]No accounts found for deposit.[/{COLORS['error']}]")
            pause()
            return
        
        if len(my_accounts) == 1:
            account = my_accounts[0]
        else:
            console.print("Select an account to deposit into: ")
            for i, acc in enumerate(my_accounts):
                console.print(f"[{i+1}] Account ID: {acc.account_id} | Balance: ${acc.balance}")
            choice = int(Prompt.ask("Enter the number of the account: ")) - 1
            account = my_accounts[choice]
        
        amount = float(Prompt.ask("Enter amount to deposit: "))
        success = self.ll.deposit(account.account_id, amount)
        console.print()  # Add spacing
        if success:
            console.print(f"[{COLORS['success']}]Successfully deposited ${amount} into account {account.account_id}.[/{COLORS['success']}]")
        else:
            console.print(f"[{COLORS['error']}]Failed to deposit funds. Please try again.[/{COLORS['error']}]")
        pause()



    def withdraw(self):
        clear_screen()
        show_header("Withdraw Funds", icon="➖")

        my_accounts = self.ll.get_user_account(self.current_user.user_id)
        if not my_accounts:
            console.print(f"[{COLORS['error']}]No accounts found for withdrawal.[/{COLORS['error']}]")
            pause()
            return
        
        if len(my_accounts) == 1:
            account = my_accounts[0]
        else:
            console.print("Select an account to withdraw from: ")
            for i, acc in enumerate(my_accounts):
                console.print(f"[{i+1}] Account ID: {acc.account_id} | Balance: ${acc.balance}")
            choice = int(Prompt.ask("Enter the number of the account: ")) - 1
            account = my_accounts[choice]
        
        amount = float(Prompt.ask("Enter amount to withdraw: "))
        success = self.ll.withdraw(account.account_id, amount)
        console.print()  # Add spacing
        if success:
            console.print(f"[{COLORS['success']}]Successfully withdrew ${amount} from account {account.account_id}.[/{COLORS['success']}]")
        else:
            console.print(f"[{COLORS['error']}]Failed to withdraw funds. Please try again.[/{COLORS['error']}]")
        pause()

    def transfer(self):
        clear_screen()
        show_header("Transfer Funds", icon="🔄")

        my_accounts = self.ll.get_user_account(self.current_user.user_id)
        if not my_accounts:
            console.print(f"[{COLORS['error']}]No accounts found for transfer.[/{COLORS['error']}]")
            pause()
            return
        
        if len(my_accounts) == 1:
            from_account = my_accounts[0]
        else:
            console.print("Select an account to transfer from: ")
            for i, acc in enumerate(my_accounts):
                console.print(f"[{i+1}] Account ID: {acc.account_id} | Balance: ${acc.balance}")
            choice = int(Prompt.ask("Enter the number of the account: ")) - 1
            from_account = my_accounts[choice]
        
        to_account_id = Prompt.ask("Enter the Account ID to transfer to: ").strip()
        try:
            amount = float(Prompt.ask("Enter amount to transfer: "))
        except ValueError:
            console.print(f"[{COLORS['error']}]Invalid amount entered.[/{COLORS['error']}]")
            pause()
            return
        success = self.ll.transfer(from_account.account_id, to_account_id, amount)
        console.print()  # Add spacing
        if success:
            console.print(f"[{COLORS['success']}]Successfully transferred ${amount} from account {from_account.account_id} to account {to_account_id}.[/{COLORS['success']}]")
        else:
            console.print(f"[{COLORS['error']}]Failed to transfer funds. Please check the account IDs and balance, then try again.[/{COLORS['error']}]")
        pause()


    def view_transaction_history(self):
        clear_screen()
        show_header("Transaction History", icon="📜")

        my_accounts = self.ll.get_user_account(self.current_user.user_id)
        if not my_accounts:
            console.print(f"[{COLORS['error']}]No accounts found for transaction history.[/{COLORS['error']}]")
            pause()
            return
        
        if len(my_accounts) == 1:
            account = my_accounts[0]
        else:
            console.print("Select an account to view transaction history: ")
            for i, acc in enumerate(my_accounts):
                console.print(f"[{i+1}] Account ID: {acc.account_id} | Balance: ${acc.balance}")
            while True:
                user_input = Prompt.ask("Enter the number of the account: ").strip()
                if not user_input.isdigit() or not (1 <= int(user_input) <= len(my_accounts)):
                    console.print(f"[{COLORS['error']}]Invalid input. Please enter a valid number between 1 and {len(my_accounts)}.[/{COLORS['error']}]")
                    continue
                choice = int(user_input) - 1
                account = my_accounts[choice]
                break
        
        transactions = self.ll.view_transaction_history(account.account_id)
        if not transactions:
            console.print(f"[{COLORS['muted']}]No transactions found for account {account.account_id}.[/{COLORS['muted']}]")
            pause()
            return
        
        transaction_lines = []
        for tx in transactions:
            # Use correct attribute names and handle missing description/date
            tx_type = getattr(tx, 'transaction_type', 'N/A')
            tx_date = getattr(tx, 'timestamp', 'N/A')
            tx_desc = getattr(tx, 'description', '')
            transaction_lines.append(f"ID: {tx.transaction_id} | Type: {tx_type} | Amount: ${tx.amount} | Date: {tx_date} | Description: {tx_desc}")
        full_width_box("\n".join(transaction_lines))
        pause()

    def logout(self):
        console.print(f"[{COLORS['success']}]You have been logged out successfully.[/{COLORS['success']}]")
        pause()
        




