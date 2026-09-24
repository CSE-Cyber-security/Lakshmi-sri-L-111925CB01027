"""
Cybersecurity Asset Inventory System
--------------------------------------
Allows a security administrator to add, search, update, delete, and
display information about an organization's IT assets, classified by
asset type and security risk level.

Data is persisted to ../data/assets.json so the inventory survives
between runs.
"""

import json
import os

DATA_FILE = os.path.join(os.path.dirname(__file__), "..", "data", "assets.json")

ASSET_TYPES = ["Workstation", "Server", "Router", "Switch", "Application"]
RISK_LEVELS = ["Low", "Medium", "High", "Critical"]
SECURITY_STATUSES = ["Secure", "Warning", "Vulnerable"]


# --------------------------------------------------------------------------
# Persistence helpers
# --------------------------------------------------------------------------

def load_assets():
    """Load assets from the JSON data file. Returns an empty list if missing."""
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        return []


def save_assets(assets):
    """Persist the current list of assets to the JSON data file."""
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
    with open(DATA_FILE, "w") as f:
        json.dump(assets, f, indent=4)


# --------------------------------------------------------------------------
# Input validation helpers
# --------------------------------------------------------------------------

def prompt_choice(prompt_text, choices):
    """Prompt the user until they enter a value from the allowed choices
    (case-insensitive), then return the canonical (properly-cased) value."""
    lookup = {c.lower(): c for c in choices}
    while True:
        value = input(f"{prompt_text} ({'/'.join(choices)}): ").strip()
        if value.lower() in lookup:
            return lookup[value.lower()]
        print(f"Invalid input. Please choose one of: {', '.join(choices)}")


def prompt_non_empty(prompt_text):
    """Prompt the user until they enter a non-empty value."""
    while True:
        value = input(f"{prompt_text}: ").strip()
        if value:
            return value
        print("This field cannot be empty. Please try again.")


def asset_id_exists(assets, asset_id):
    return any(a["Asset ID"].lower() == asset_id.lower() for a in assets)


# --------------------------------------------------------------------------
# Core operations
# --------------------------------------------------------------------------

def add_asset(assets):
    print("\n--- Add New Asset ---")
    asset_id = prompt_non_empty("Asset ID")
    if asset_id_exists(assets, asset_id):
        print(f"Error: Asset ID '{asset_id}' already exists. Asset not added.")
        return

    asset_name = prompt_non_empty("Asset Name")
    asset_type = prompt_choice("Asset Type", ASSET_TYPES)
    ip_address = prompt_non_empty("IP Address")
    operating_system = prompt_non_empty("Operating System")
    department = prompt_non_empty("Owner/Department")
    risk_level = prompt_choice("Risk Level", RISK_LEVELS)
    security_status = prompt_choice("Security Status", SECURITY_STATUSES)

    asset = {
        "Asset ID": asset_id,
        "Asset Name": asset_name,
        "Asset Type": asset_type,
        "IP Address": ip_address,
        "Operating System": operating_system,
        "Department": department,
        "Risk Level": risk_level,
        "Security Status": security_status,
    }
    assets.append(asset)
    save_assets(assets)
    print(f"Asset '{asset_id}' added successfully.")


def display_asset(asset):
    print("-----------------------------------------")
    print(f"Asset ID    : {asset['Asset ID']}")
    print(f"Asset Name  : {asset['Asset Name']}")
    print(f"Asset Type  : {asset['Asset Type']}")
    print(f"IP Address  : {asset['IP Address']}")
    print(f"OS          : {asset['Operating System']}")
    print(f"Department  : {asset['Department']}")
    print(f"Risk Level  : {asset['Risk Level']}")
    print(f"Status      : {asset['Security Status']}")


def display_all_assets(assets):
    print("=========================================")
    print(" CYBERSECURITY ASSET INVENTORY")
    print("=========================================")
    if not assets:
        print("No assets found in inventory.")
    else:
        for asset in assets:
            display_asset(asset)
    print("-----------------------------------------")
    print_summary(assets)


def print_summary(assets):
    total = len(assets)
    critical = sum(1 for a in assets if a["Risk Level"] == "Critical")
    high = sum(1 for a in assets if a["Risk Level"] == "High")
    medium = sum(1 for a in assets if a["Risk Level"] == "Medium")
    vulnerable = sum(1 for a in assets if a["Security Status"] == "Vulnerable")

    print(f"Total Assets : {total}")
    print(f"Critical Assets : {critical}")
    print(f"High Risk Assets : {high}")
    print(f"Medium Risk Assets : {medium}")
    print(f"Vulnerable Assets : {vulnerable}")
    print("=========================================")


def search_asset(assets):
    print("\n--- Search Asset ---")
    print("Search by: 1) Asset ID  2) Asset Name  3) Asset Type  4) Risk Level")
    choice = input("Enter choice (1-4): ").strip()

    field_map = {
        "1": "Asset ID",
        "2": "Asset Name",
        "3": "Asset Type",
        "4": "Risk Level",
    }
    field = field_map.get(choice)
    if not field:
        print("Invalid choice.")
        return

    term = input(f"Enter {field} to search for: ").strip().lower()
    results = [a for a in assets if term in a[field].lower()]

    if results:
        print(f"\nFound {len(results)} matching asset(s):")
        for asset in results:
            display_asset(asset)
        print("-----------------------------------------")
    else:
        print("No matching asset found.")


def find_asset_by_id(assets, asset_id):
    for asset in assets:
        if asset["Asset ID"].lower() == asset_id.lower():
            return asset
    return None


def update_asset(assets):
    print("\n--- Update Asset ---")
    asset_id = prompt_non_empty("Enter Asset ID to update")
    asset = find_asset_by_id(assets, asset_id)
    if not asset:
        print(f"Error: Asset ID '{asset_id}' not found.")
        return

    print("Leave a field blank to keep its current value.")
    print(f"Current Asset Name [{asset['Asset Name']}]")
    new_name = input("New Asset Name: ").strip()
    if new_name:
        asset["Asset Name"] = new_name

    print(f"Current Asset Type [{asset['Asset Type']}]")
    new_type = input(f"New Asset Type ({'/'.join(ASSET_TYPES)}) or blank: ").strip()
    if new_type:
        lookup = {c.lower(): c for c in ASSET_TYPES}
        if new_type.lower() in lookup:
            asset["Asset Type"] = lookup[new_type.lower()]
        else:
            print("Invalid asset type. Keeping previous value.")

    print(f"Current IP Address [{asset['IP Address']}]")
    new_ip = input("New IP Address: ").strip()
    if new_ip:
        asset["IP Address"] = new_ip

    print(f"Current Operating System [{asset['Operating System']}]")
    new_os = input("New Operating System: ").strip()
    if new_os:
        asset["Operating System"] = new_os

    print(f"Current Department [{asset['Department']}]")
    new_dept = input("New Department: ").strip()
    if new_dept:
        asset["Department"] = new_dept

    print(f"Current Risk Level [{asset['Risk Level']}]")
    new_risk = input(f"New Risk Level ({'/'.join(RISK_LEVELS)}) or blank: ").strip()
    if new_risk:
        lookup = {c.lower(): c for c in RISK_LEVELS}
        if new_risk.lower() in lookup:
            asset["Risk Level"] = lookup[new_risk.lower()]
        else:
            print("Invalid risk level. Keeping previous value.")

    print(f"Current Security Status [{asset['Security Status']}]")
    new_status = input(f"New Security Status ({'/'.join(SECURITY_STATUSES)}) or blank: ").strip()
    if new_status:
        lookup = {c.lower(): c for c in SECURITY_STATUSES}
        if new_status.lower() in lookup:
            asset["Security Status"] = lookup[new_status.lower()]
        else:
            print("Invalid security status. Keeping previous value.")

    save_assets(assets)
    print(f"Asset '{asset_id}' updated successfully.")


def delete_asset(assets):
    print("\n--- Delete Asset ---")
    asset_id = prompt_non_empty("Enter Asset ID to delete")
    asset = find_asset_by_id(assets, asset_id)
    if not asset:
        print(f"Error: Asset ID '{asset_id}' not found.")
        return

    confirm = input(f"Are you sure you want to delete '{asset_id}'? (y/n): ").strip().lower()
    if confirm == "y":
        assets.remove(asset)
        save_assets(assets)
        print(f"Asset '{asset_id}' deleted successfully.")
    else:
        print("Deletion cancelled.")


def bulk_add_assets(assets):
    """Optional convenience: matches the sample-input style where the user
    specifies how many assets to enter up front."""
    try:
        count = int(input("Enter number of assets: ").strip())
    except ValueError:
        print("Invalid number.")
        return

    for i in range(1, count + 1):
        print(f"\nAsset {i}")
        add_asset(assets)


# --------------------------------------------------------------------------
# Menu / main loop
# --------------------------------------------------------------------------

def print_menu():
    print("\n=========================================")
    print(" CYBERSECURITY ASSET INVENTORY SYSTEM")
    print("=========================================")
    print("1. Add Asset")
    print("2. Add Multiple Assets (bulk entry)")
    print("3. Display All Assets")
    print("4. Search Asset")
    print("5. Update Asset")
    print("6. Delete Asset")
    print("7. Exit")


def main():
    assets = load_assets()

    while True:
        print_menu()
        choice = input("Enter your choice (1-7): ").strip()

        if choice == "1":
            add_asset(assets)
        elif choice == "2":
            bulk_add_assets(assets)
        elif choice == "3":
            display_all_assets(assets)
        elif choice == "4":
            search_asset(assets)
        elif choice == "5":
            update_asset(assets)
        elif choice == "6":
            delete_asset(assets)
        elif choice == "7":
            print("Exiting Cybersecurity Asset Inventory System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")


if __name__ == "__main__":
    main()
