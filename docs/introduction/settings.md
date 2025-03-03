(settings)=
# Settings

## Defaults

```json
{
  "filter": "shapescape_easy_glyphs",
  "settings": {
    "scale": 4,
    "glyph_hex": "E1"
  }
}
```

### Parameters
#### **scale**
Default: 4

This parameter accepts an integer value between 1 and 4, and it defines the resolution of the glyphs.

#### **glyph_hex**
Default: "E1"

This parameter defines the hex code for the output file. The output file follows this naming convention: font/glyph_'glyph_hex'.png. 

The hex code is also used to determine the Unicode for each tile. If you need more information about glyphs, you can refer to the page on wiki.bedrock.dev