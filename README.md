# Mini Bank System (CLI)

A terminal-based bank management system built in Python using a layered architecture
(UI, Logic, and Data layers).

## Features
- Admin: create users and accounts, view system data
- Customer: deposit, withdraw, transfer, view balance & history
- Guest: view bank information
- File-based persistence (JSON)
- Clean 3-layer architecture with API wrappers

## Project Structure
mini_bank_system/
├── models/
├── data/
├── logic/
├── ui/
└── main.py

## How to Run
1. Clone the repository
2. Run:
```bash
python main.py
