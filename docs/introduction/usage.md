# Usage

## Steps 

### 1. Prepare Your Folder Structure
- Navigate to the `data` folder of the filter (default path: `data/shapescape_easy_glyphs`).
- Create a folder for each glyph category you want to organize.
  - For example:
    ```
    data/shapescape_easy_glyphs/
    ├── 0_vanilla/
    ├── 1_weapons/
    ├── 2_characters/
    ├── 3_items/
    ```
- **Important:** Do not modify the `0_vanilla` folder, as it contains default vanilla icons for the E1 sheet.

### 2. Add Icons to Category Folders
- Place your glyph icons in their respective category folders.
- To maintain order and avoid Unicode changes when adding new glyphs, name your files with an integer prefix in **2-digit format** (e.g., `01_sword.png`, `02_shield.png`).
  - Each row can hold up to 16 icons, so this naming convention ensures proper alignment.
- Recommended icon size: **32x32 pixels**.

### 3. Run the Filter
- Execute the filter script. The filter will:
  1. Process each category folder in alphabetical order.
  2. Paste all glyphs from a category onto the sheet.
  3. Leave extra space for future additions before moving to the next category.

### 4. Generated Output
- After running the filter, a JSON file will be created at:

`filters_data/hero_glyphs/unicodes.json`

- This JSON file contains mappings of icon names to their corresponding Unicode characters.
- Example format:
  ```
  {
      "1_weapons": {
          "01_sword": "U+E001",
          "02_shield": "U+E002"
      },
      "2_characters": {
          "01_hero": "U+E003",
          "02_villain": "U+E004"
      }
  }
  ```

## Best Practices

- **Keep Backups:** Avoid modifying the `0_vanilla` folder directly. Always work with custom folders for your categories.
- **Use Consistent Naming:** Prefix file names with integers in ascending order (e.g., `01`, `02`, etc.) to ensure proper alignment and avoid conflicts.
- **Plan for Growth:** Leave room in each category by following the filter's automatic spacing logic.
- **Icon Size:** Ensure all icons are sized at 32x32 pixels for compatibility.

## Additional Notes

- The generated JSON file can be copied into any text file or application where you need to display glyphs using their Unicode values.
- If you need to add new glyphs later, simply place them in the appropriate category folder with a proper integer prefix, then rerun the filter.