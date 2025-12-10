# Bank System - Copilot Instructions

## Architecture Overview

This is a **3-layer CLI banking application** with strict separation of concerns:

```
UI Layer (ui/) → Logic Layer (logic/) → Data Layer (data/) → Storage (storage/)
```

- **Models** (`models/`): Plain data classes (User, Account, Transaction) - no business logic
- **Data Layer** (`data/`): JSON persistence via Repository pattern
  - Each repository handles file I/O + dict↔model conversion
  - `DataLayerAPI` aggregates repositories and delegates load/save operations
- **Logic Layer** (`logic/`): Business rules (account operations, validations, user management)
  - `LogicLayerAPI` should aggregate manager classes (UserManager, AccountManager, TransactionManager)
- **UI Layer** (`ui/`): Terminal interface organized by user role (admin/user/guest)

## Critical Patterns

### Repository Pattern
Each repository (e.g., `UserRepository`) implements:
- `read_*_from_file()` → `list[dict]` (JSON → Python dict)
- `write_*_to_file(list[dict])` → None (Python dict → JSON)
- `dict_to_*()` → Model object (dict → dataclass)
- `*_to_dict()` → dict (dataclass → dict)

**Example from `user_repository.py`:**
```python
def dict_to_user(self, user_dict: dict) -> User:
    return User(user_id=user_dict["user_id"], name=user_dict["name"], ...)
```

### Layer Communication
- **Never skip layers**: UI must call Logic API, Logic must call Data API
- **API wrappers**: `DataLayerAPI` and `LogicLayerAPI` serve as single entry points to their layers
- **Stateless operations**: Load data, process, save - no in-memory state retention between operations

### Data Persistence
- All data lives in `storage/*.json` files (users, accounts, transactions)
- Use `json.dump(data, file, indent=4)` for consistency
- Use `.get()` for optional fields (e.g., `transaction_dict.get("sender_id")` returns None if missing)

## User Roles & Permissions
- **Admin**: Create users/accounts, view all system data
- **User**: Deposit, withdraw, transfer, view own balance/history
- **Guest**: Read-only bank information

## Current Implementation Status
⚠️ **Partially implemented** - many files are empty stubs:
- `main.py`, `logic_layer_api.py`, all `*_manager.py`, all `ui/*.py` are not yet implemented
- `DataLayerAPI` methods are defined but contain only `pass` statements
- Repository pattern is fully implemented in `data/` folder

When implementing new features:
1. Start with models if new entities are needed
2. Add repository methods in `data/`
3. Implement business logic in `logic/`
4. Build UI in `ui/` matching user role

## Development Workflow
- **Run**: `python main.py` (once main.py is implemented)
- **No tests currently exist** - manual testing via CLI
- **No external dependencies** - pure Python stdlib (json module only)
