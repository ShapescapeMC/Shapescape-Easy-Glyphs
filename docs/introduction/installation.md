(installation)=
# Installation

## Steps

### 1. Install the filter
Use the following command
```
regolith install shapescape_easy_glyphs
```

You can alternatively use this command:
```
regolith install https://github.com/ShapescapeMC/Shapescape-Easy-Glyphs/shapescape_easy_glyphs
```

### 2. Add filter to a profile
Add the filter to the `filters` list in the `config.json` file of the Regolith project and add the settings:

```json
{
  "filter": "shapescape_easy_glyphs",
  "settings": {
    "scale": 4,
    "glyph_hex": "E1"
  }
}
```