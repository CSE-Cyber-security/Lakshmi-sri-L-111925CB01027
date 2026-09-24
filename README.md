# Week 01 — Cybersecurity Asset Inventory System

A command-line Python application that lets a security administrator **add, search, update, delete, and display** an organization's IT assets, classified by asset type and security risk level.

## Problem Statement

Organizations manage many IT assets (computers, servers, routers, switches, applications). Tracking them manually makes it hard to identify assets, monitor their security status, and flag which ones need urgent attention. This system centralizes that information in a simple, menu-driven CLI tool.

## Features

- **Add Asset** — add a single asset with validated fields
- **Add Multiple Assets** — bulk entry (mirrors the sample input flow: "Enter number of assets")
- **Display All Assets** — prints the full inventory plus a security summary
- **Search Asset** — search by Asset ID, Asset Name, Asset Type, or Risk Level
- **Update Asset** — edit any field of an existing asset (blank = keep current value)
- **Delete Asset** — remove an asset, with a confirmation prompt
- **Persistence** — all changes are saved to `data/assets.json` automatically

## Data Fields

| Field | Description |
|---|---|
| Asset ID | Unique identifier (e.g. `A101`) |
| Asset Name | Friendly name (e.g. `HR-PC-01`) |
| Asset Type | `Workstation`, `Server`, `Router`, `Switch`, `Application` |
| IP Address | Asset's network address |
| Operating System | OS running on the asset |
| Owner/Department | Department responsible for the asset |
| Risk Level | `Low`, `Medium`, `High`, `Critical` |
| Security Status | `Secure`, `Warning`, `Vulnerable` |

## Repository Structure

```
Week-01-Cybersecurity-Asset-Inventory/
│
├── src/
│   └── asset_inventory.py
│
├── data/
│   └── assets.json
│
├── tests/
│   └── test_cases.md
│
├── screenshots/
│   ├── 01-add-asset.png
│   ├── 02-display-assets.png
│   ├── 03-search-asset.png
│   ├── 04-update-asset.png
│   ├── 05-delete-asset.png
│   ├── 06-security-summary.png
│   └── 07-input-validation.png
│
└── README.md
```

## How to Run

```bash
cd src
python asset_inventory.py
```

You'll see a menu:

```
=========================================
 CYBERSECURITY ASSET INVENTORY SYSTEM
=========================================
1. Add Asset
2. Add Multiple Assets (bulk entry)
3. Display All Assets
4. Search Asset
5. Update Asset
6. Delete Asset
7. Exit
```

The repo ships with `data/assets.json` pre-populated with the 3 sample assets from the assignment, so you can immediately try option 3 (Display All Assets) and see output matching the expected format.

## Sample Output

```
=========================================
 CYBERSECURITY ASSET INVENTORY
=========================================
-----------------------------------------
Asset ID    : A101
Asset Name  : HR-PC-01
Asset Type  : Workstation
IP Address  : 192.168.1.10
OS          : Windows 11
Department  : HR
Risk Level  : Medium
Status      : Secure
-----------------------------------------
Asset ID    : A102
Asset Name  : Web-Server
Asset Type  : Server
IP Address  : 192.168.1.20
OS          : Ubuntu
Department  : IT
Risk Level  : Critical
Status      : Vulnerable
-----------------------------------------
Asset ID    : A103
Asset Name  : Core-Router
Asset Type  : Router
IP Address  : 192.168.1.1
OS          : Cisco IOS
Department  : Network
Risk Level  : High
Status      : Warning
-----------------------------------------
Total Assets : 3
Critical Assets : 1
High Risk Assets : 1
Medium Risk Assets : 1
Vulnerable Assets : 1
=========================================
```

## Testing

See [`tests/test_cases.md`](tests/test_cases.md) for the full list of manual test cases covering valid input, duplicate IDs, invalid categorical values, empty inventory, search misses, update/delete on non-existent IDs, and persistence across runs.

## Screenshots

The `screenshots/` folder is where to place PNG captures of each operation (add, display, search, update, delete, summary, and input validation) when demonstrating the working program.
