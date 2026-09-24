# Test Cases — Cybersecurity Asset Inventory System

| # | Test Case | Steps | Expected Result |
|---|-----------|-------|------------------|
| 1 | Add a valid asset | Choose option 1, enter unique Asset ID and valid values for all fields | Asset is added and saved to `data/assets.json`; confirmation message shown |
| 2 | Add asset with duplicate Asset ID | Choose option 1, enter an Asset ID that already exists (e.g. `A101`) | System rejects the entry with "Asset ID already exists" error, asset not added |
| 3 | Add asset with invalid Asset Type / Risk Level / Status | Choose option 1, enter a value outside the allowed list (e.g. Asset Type = "Laptop") | System re-prompts until a valid value from the allowed list is entered |
| 4 | Bulk add assets | Choose option 2, enter number of assets (e.g. 3), fill each asset's details | All 3 assets added sequentially, matching the sample input flow |
| 5 | Display all assets | Choose option 3 with at least one asset in inventory | All assets printed in the required format, followed by the summary section |
| 6 | Display with empty inventory | Choose option 3 with no assets stored | "No assets found in inventory." message is shown, summary shows 0 for all counts |
| 7 | Search by Asset ID | Choose option 4, select "Asset ID", enter `A102` | Web-Server asset details are displayed |
| 8 | Search by Asset Type | Choose option 4, select "Asset Type", enter `Router` | All router-type assets are displayed (Core-Router) |
| 9 | Search with no match | Choose option 4, enter a term with no matches (e.g. `Z999`) | "No matching asset found." message shown |
| 10 | Update an existing asset | Choose option 5, enter `A101`, change Risk Level to `High`, leave other fields blank | Only Risk Level is updated; all other fields unchanged; change persisted to JSON |
| 11 | Update a non-existent asset | Choose option 5, enter an Asset ID that does not exist | "Asset ID not found" error shown, no changes made |
| 12 | Delete an existing asset with confirmation | Choose option 6, enter `A103`, confirm with `y` | Asset removed from inventory and from `data/assets.json` |
| 13 | Delete cancelled | Choose option 6, enter a valid Asset ID, respond `n` to confirmation | Asset is NOT deleted, "Deletion cancelled." message shown |
| 14 | Delete a non-existent asset | Choose option 6, enter an Asset ID that does not exist | "Asset ID not found" error shown |
| 15 | Security summary counts | After loading the 3 sample assets, choose option 3 | Total Assets: 3, Critical Assets: 1, High Risk Assets: 1, Medium Risk Assets: 1, Vulnerable Assets: 1 |
| 16 | Persistence across runs | Add/update/delete an asset, exit the program (option 7), relaunch | Inventory reflects the previously saved state from `data/assets.json` |
| 17 | Input validation — empty required field | Leave Asset Name blank when adding an asset | System re-prompts and does not accept an empty value |
| 18 | Invalid main menu choice | Enter an out-of-range option (e.g. `9`) at the main menu | "Invalid choice" message shown, menu re-displayed |
